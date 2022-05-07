import numpy as np
from matplotlib import pyplot as plt
import random
from humanfriendly import format_timespan

# The Boat will spread dye powder to the river
# Possible features can be added: the diffusion speed affected by the boat (unit distance around)
# Possible features can be added: the route of the boat, can be straight or s-shaped
# The sailing speed is around 1 m/s
"""
There are three classes and one simulation function to practice this simulation.
"Boat" class is designed for the behaviors of a boat, including spreading dye, different moving styles, 
and the weight of random movement.
"Dye" class is used to hold the concentration information and do the unit conversion.
"River" Class can calculate the diffusion and water flow effect on the dye concentration. Each execution will update
the river concentration for 1 second.
The simulation function setup the environment to run the Monte Carlo simulation. 
"""

class Boat:
    def __init__(self, river_size, dye_weight=45, velocity=2, dye_spread_v=1.89, min_dye=25):
        """
        This is the constructor of the boat class, which initialize a boat object when created. The given river size is
        used for sailing.
        :param river_size: The size of the river
        :param dye_weight: the weight of dye powder the boat is carrying in pounds
        :param velocity: the velocity of the boat in m/s
        :param dye_spread_v: the weight of dye can be spread in g/s
        :param min_dye: minimum dye need to dye the whole river in pounds
        >>> b = Boat([10,5])
        >>> print('River size: {}, Dye_weight: {}, Velocity: {}, dye_spread_v: {}'.format(b.river_size,b.dye_weight,b.velocity,b.dye_spread_v))
        River size: [10, 5], Dye_weight: 20411.65665, Velocity: 2, dye_spread_v: 1.89
        >>> b = Boat([10,5], 30,3,1.55,25)
        >>> print('River size: {}, Dye_weight: {}, Velocity: {}, dye_spread_v: {}'.format(b.river_size,b.dye_weight,b.velocity,b.dye_spread_v))
        River size: [10, 5], Dye_weight: 13607.7711, Velocity: 3, dye_spread_v: 1.55
        """
        self.river_size = river_size
        # initial boat location is on the top middle of the given river
        self.loc = [1, river_size[1]//2]
        # store the raw location of the boat when the movement is not integer
        self.raw_loc = [1, river_size[1]//2]
        # convert pound to gram
        self.dye_weight = dye_weight * 453.59237
        self.velocity = velocity
        self.dye_spread_v = dye_spread_v
        # vertical direction parameters for boat movement
        self.vdir = 0.5
        # horizontal direction parameters for boat movement
        self.hdir = 1
        # vertical movement indicator for straight sailing
        self.vmove = -1
        # connect class Dye to the boat for concentration calculation
        self.dye = Dye(min_dye)
        # weight list for random movement: equal in all direction if didn't run get_random_weight
        self.weight_list = [1, 1, 1, 1, 99, 1, 1, 1, 1]

    def spread_dye(self, boat_width=1):
        """
        Update the concentration added to the boat location and the remain dye weight
        :param boat_width: the weight of the boat width that can affect the dyeing range
        :return: return the concentration of the point that the boat spread dye
        >>> b = Boat([10,5])
        >>> b.spread_dye()
        0.00189
        >>> b.dye_weight = 0.0001
        >>> b.spread_dye()
        1.0000000000000001e-07
        >>> b.spread_dye()
        0
        """
        if self.dye_weight > 0:
            if self.dye_weight > self.dye_spread_v * boat_width:
                self.dye_weight -= self.dye_spread_v * boat_width
                # turn 1meter^3 into liter base concentration
                return self.dye.to_concerntration(self.dye_spread_v)
            else:
                # print(self.dye_weight)
                last = self.dye_weight / boat_width
                self.dye_weight = 0
                return self.dye.to_concerntration(last)
        return 0

    def straight_sailing(self, h_time=20):
        """
        The boat sail straight down the river and turn right and sails for 20 second than turn upstream in straight line.
        In case the boat meet the right bank, it will turn to the left bank.
        :param h_time: horizontal movement time when a straight sailing boat meet the end of the river
        :return: the location in next timestamp
        >>> b = Boat([10,5])
        >>> b.straight_sailing()
        [3, 2]
        >>> b.loc = [10,2]
        >>> b.straight_sailing()
        [7, 2]
        """
        if self.loc[0] < 2:
            self.vdir = 1
            if self.loc[1] < 2:
                self.hdir = 1
            elif self.loc[1] > self.river_size[1] - 2:
                self.hdir = -1
            if self.vmove and h_time == 20:
                self.vmove = self.vmove * -1
        if self.loc[0] > self.river_size[0] - 2:
            self.vdir = -1
            if self.loc[1] < 2:
                self.hdir = 1
            elif self.loc[1] > self.river_size[1] - 2:
                self.hdir = -1
            if self.vmove and h_time == 20:
                self.vmove = self.vmove * -1
        if self.vmove == -1:
            self.loc[1] += self.hdir * self.velocity
            h_time -= 1
        else:
            self.loc[0] += self.vdir * self.velocity
        if h_time == 0:
            h_time = 20
        return [min(round(self.loc[0]), self.river_size[0] - 3), min(round(self.loc[1]), self.river_size[1] -3)]

    def zip_sailing(self, right=True, down=True):
        """
        Assume the boat sail 45 degree from the horizontal line, and turn 90 degree when the boat is less than 2m
        start from going right and down ward.
        :param right: start the zip sailing from right direction, if not start from going left.
        :param down:  start the zip sailing from down direction. Cannot change to False if start from top of the river.
        :return: the location in next timestamp
        >>> b = Boat([10,5])
        >>> b.zip_sailing()
        (False, True, [2, 3])
        >>> b.loc = [10,2]
        >>> b.zip_sailing()
        (False, True, [4, 5])

        """
        move = np.sqrt(self.velocity**2/2)
        if right:
            self.raw_loc[1] += move
            self.loc[1] = int(round(self.raw_loc[1],0))
            if (self.river_size[1] - 1) - max(self.raw_loc[1], self.loc[1]) - 2 < move:
                right = False
        else:
            self.raw_loc[1] -= move
            self.loc[1] = int(round(self.raw_loc[1], 0))
            if min(self.raw_loc[1], self.loc[1]) - 1 - 2 < move:
                right = True
        if down:
            self.raw_loc[0] += move
            self.loc[0] = int(round(self.raw_loc[0], 0))
            if (self.river_size[0] - 1) - max(self.raw_loc[0], self.loc[0]) - 2 < move:
                down = False
        else:
            self.raw_loc[0] -= move
            self.loc[0] = int(round(self.raw_loc[0], 0))
            if min(self.raw_loc[0], self.loc[0]) - 1 - 2 < move:
                down = True
        return right, down, self.loc

    def zigzag_sailing(self):
        """
        Assume the boat sail twice the speed in horizontal direction than vertical direction. The boat sails in a
        zigzag way.
        :return: the location in next timestamp
        >>>
        """
        if self.loc[0] < 2:
            self.vdir = 0.5
        if self.loc[0] > self.river_size[0] - 2:
            self.vdir = -0.5
        if self.loc[1] < 2:
            self.hdir = 1
        if self.loc[1] > self.river_size[1] - 2:
            self.hdir = -1
        self.loc[0] += self.vdir * self.velocity
        self.loc[1] += self.hdir * self.velocity
        return [min(round(self.loc[0]), self.river_size[0] - 3), min(round(self.loc[1]), self.river_size[1] - 3)]

    def random_sailing(self):
        """
        uniform probability to move to any direction
        [ 0, 1, 2
          3, X, 4
          5, 6, 7 ]
        Each number represent a direction. The direction is randomly choice with a weight list that can be obtain by
        get_random_weight function.
        :return: the location in next timestamp
        """
        # print(self.loc)
        direction_array = np.array([0, 1, 2, 3, 99, 4, 5, 6, 7], dtype=int).reshape(3, 3)
        weight_array = np.array(self.weight_list).reshape(3, 3)
        if self.loc[0] - 2 <= self.velocity:
            direction_array = direction_array[1:, :]
            weight_array = weight_array[1:, :]
        if self.river_size[0] - self.loc[0] <= self.velocity:
            direction_array = direction_array[:-1, :]
            weight_array = weight_array[:-1, :]
        if self.loc[1] - 2 <= self.velocity:
            direction_array = direction_array[:, 1:]
            weight_array = weight_array[:, 1:]
        if self.river_size[1] - self.loc[1] <= self.velocity:
            direction_array = direction_array[:, :-1]
            weight_array = weight_array[:, :-1]
        direction_list = direction_array.reshape(1, -1).tolist()[0]
        weight_list = weight_array.reshape(1,-1).tolist()[0]
        direction_list.remove(99)
        weight_list.remove(99)
        # print(weight_list, direction_list)
        direction = random.choices(direction_list, weights=weight_list, k=1)[0]
        # print(direction)
        if direction in [1, 2, 5, 7]:
            move = np.sqrt(self.velocity ** 2 / 2)
        else:
            move = self.velocity
        if direction == 0:
            self.raw_loc[0] -= move
            self.raw_loc[1] -= move
        elif direction == 1:
            self.raw_loc[0] -= move
        elif direction == 2:
            self.raw_loc[0] -= move
            self.raw_loc[1] += move
        elif direction == 3:
            self.raw_loc[1] -= move
        elif direction == 4:
            self.raw_loc[1] += move
        elif direction == 5:
            self.raw_loc[0] += move
            self.raw_loc[1] -= move
        elif direction == 6:
            self.raw_loc[0] += move
        else:
            self.raw_loc[0] += move
            self.raw_loc[1] += move
        self.loc = [int(round(self.raw_loc[0], 0)), int(round(self.raw_loc[1], 0))]
        # print(self.loc)
        return self.loc

    def get_random_weight(self, river):
        """
        update the weight of each random sailing direction. The Weight is calculate by counting the percentage of the
        pixels that are under the visible concentration.
        :param river: the current river concentration
        :return: a list of weight for each direction from [0-7] in random_sailing
        """
        x = self.loc[1] - 1
        y = self.loc[0] - 1
        try:
            self.weight_list.append(river[:y,:x][river[:y,:x] < self.dye.visible_concentration].size/river[:y,:x].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[:y,x][river[:y,x] < self.dye.visible_concentration].size/river[:y,x].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[:y,x+1:][river[:y,x+1:] < self.dye.visible_concentration].size/river[:y,x+1:].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[y,:x][river[y,:x] < self.dye.visible_concentration].size/river[y,:x].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        self.weight_list.append(99)
        try:
            self.weight_list.append(river[y,x+1:][river[y,x+1:] < self.dye.visible_concentration].size/river[y,x+1:].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[y+1:,:x][river[y+1:,:x] < self.dye.visible_concentration].size/river[y+1:,:x].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[y+1:,x][river[y+1:,x] < self.dye.visible_concentration].size/river[y+1:,x].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        try:
            self.weight_list.append(river[y+1:,x+1:][river[y+1:,x+1:] < self.dye.visible_concentration].size/river[y+1:,x+1:].size)
        except ZeroDivisionError:
            self.weight_list.append(0)
        # percentage = s_river.r_plot[s_river.r_plot < self.visible_concentration].size / s_river.r_plot.size
        # print(self.loc, self.weight_list[9:])
        self.weight_list = self.weight_list[9:]


class Dye:
    def __init__(self, min_dye):
        """
        :param min_dye: minimum dye need to dye the whole river
        dye information:
        https://www.irishcentral.com/culture/craic/st-patricks-day-chicago-river-green
        """
        self.visible_concentration = min_dye * 0.8 * 453.59237 / (85*550*1 * 100**3) * 1000

    def to_concerntration(self,dye_g):
        """
        turn weight of dye into the concentration
        Percent weight-volume (%(w/v)) = 100 x (g of solute / ml of solution)
        :param dye_g: the weight of dye in gram.
        :return: the concentration in g / m^3
        """
        return dye_g / 100 ** 3 * 1000


class River:
    def __init__(self, length, w, d, flow_rate):
        """
        Here we just assume that the river is a large rectangular tank.
        :param length: length of the river
        :param w: width of the river
        :param d: depth of the river
        """
        self.length = length
        self.w = w
        # self.d = d
        # self.r = np.zeros((l,w,d))
        self.r = np.zeros((length+2, w+2)).astype('float64')
        # "+2" is used for setting boundary value same as the boundary
        self.flow_rate = flow_rate
        self.r_plot = self.r[1:-1, 1:-1]

    def diffusion(self):
        """

        :return:
        """
        # set normal distribution random variable with mean=3, sd=1 and rescale the mean to 1
        # water diffusion coefficient reference: https://dtrx.de/od/diff/index.html#tab7 used 8 degree celsius
        diffusion_rand_x = abs(np.random.normal(loc=3,scale=1,size=(self.r.shape[0], self.r.shape[1])) / 3 * (9.7 * 10**(-3)))
        diffusion_rand_y = abs(np.random.normal(loc=3,scale=1,size=(self.r.shape[0], self.r.shape[1])) / 3 * (9.7 * 10**(-3)))
        # Cx,t+1 = d * Cx+1,t + ( 1 - 2d ) * Cx,t + Cx-1, t
        # process edge first, four point didn't processed
        diffusion_x = np.multiply(self.r, diffusion_rand_x)
        diffusion_y = np.multiply(self.r, diffusion_rand_y)
        x_and_1 = diffusion_x[1:,:]
        x_and_1 = np.vstack((x_and_1, diffusion_x[-1,:]))
        x_minus_1 = diffusion_x[0:-1,:]
        x_minus_1 = np.vstack((diffusion_x[0, :], x_minus_1))
        y_left = diffusion_y[:,1:]
        y_left = np.hstack((y_left, diffusion_y[:,-1].reshape(-1,1)))
        y_right = diffusion_y[:,:-1]
        y_right = np.hstack((diffusion_y[:,0].reshape(-1,1), y_right))
        self.reserve = self.r
        self.r = (x_and_1 + x_minus_1) + (y_left + y_right) + (self.r - 2 * diffusion_x - 2 *diffusion_y)
        self.r_plot = self.r[1:-1, 1:-1]

    def flow_effect(self):
        """

        :return: the shifted matrix
        """
        # C^(n+1)_i,j=(C^n_i-1,j-C^n_i+1,j)/2dx*dt*u^n_i,j
        # u: water velocity
        # https://waterdata.usgs.gov/nwis/uv?period=&begin_date=2022-03-01&end_date=2022-03-31&cb_72254=on&site_no=05536123&format=gif_mult_sites
        flow_rand_x = np.random.normal(loc=0.0025, scale=0.0205, size=(self.r.shape[0], self.r.shape[1]))
        c_and_1 = self.reserve[1:, :]
        c_and_1 = np.vstack((c_and_1, self.reserve[-1, :]))
        c_minus_1 = self.reserve[0:-1, :]
        c_minus_1 = np.vstack((self.reserve[0, :], c_minus_1))
        self.r += np.multiply((c_minus_1 - c_and_1) / 2, flow_rand_x)
        self.r_plot = self.r[1:-1, 1:-1]
        # self.r = scipy.ndimage.interpolation.shift(self.r, [self.flow_rate, 0], cval=0.0)


def simulate():
    total_time = 0
    fail_count = 0
    total_percentage = 0
    for s in range(10):
        # usual length 550 2022 60th 1280
        s_river = River(545, 70, 1, 1)
        # print(s_river.r, s_river.r.shape)
        b_boat = Boat([545, 70], 33.75, 2 ** (1 / 2), 1.89, 25)
        s_boat = Boat([545, 70], 11.25, 2 * 2 ** (1 / 2), 1.89, 25)
        go = True
        i = 0
        time_95 = 0
        right, down, loc = b_boat.zip_sailing()
        plt.ion()
        loc2 = None
        while go:
            if s_boat.dye_weight != 0:
                s_boat.get_random_weight(s_river.r_plot)
                # loc = b_boat.zigzag_sailing()
                # loc = b_boat.straight_sailing()
                loc2 = s_boat.random_sailing()
                s_river.r[loc[0], loc[1]-1:loc[1]+2] += b_boat.spread_dye(3)
                s_river.r[loc2[0], loc2[1]] += s_boat.spread_dye()
                right, down, loc = b_boat.zip_sailing(right, down)
                # print(i, s_boat.dye_weight, b_boat.dye_weight)
            s_river.diffusion()
            s_river.flow_effect()
            if i % 100 == 0 and s == 0:
                # print(i, dye, loc)
                plt.clf()
                if loc2:plt.scatter([loc2[1]], [loc2[0]], color='white', s=20)  # 随机船位置
                plt.scatter([loc[1]], [loc[0]], color='r', s=20)  # 折线船位置
                plt.imshow(np.clip(s_river.r_plot, 0, 2.426 * 10 ** -4))
                plt.title(f'Chicago River Dyeing Simulation\nt={i}')
                # plt.show()
                plt.pause(0.3)
            i += 1
            percentage = s_river.r_plot[s_river.r_plot < 0.8 * 2.426*10**-4].size / s_river.r_plot.size
            if percentage <= 0.05 and time_95 == 0:
                time_95 = i
                total_time += time_95
                print(f'Complete the {s+1}th simulation in {time_95} seconds.')
                go = False
            elif i > 7200:
                fail_count += 1
                total_percentage += percentage
                print(f'Fail the {s+1}th simulation.')
                go = False
            # if (s_river.r_plot >= 0.8*2.426*10**-4).all() or i > 7200:
    avg_time = round(total_time / (10 - fail_count), 0)
    print('The average time to dye the river is:', format_timespan(avg_time))
    if fail_count != 0:
        avg_percentage = 1 - round(total_percentage / fail_count, 2)
        print(f'There are {fail_count} simulations fail to cover the river with an average {avg_percentage:.2%} coverage rate.')
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    simulate()