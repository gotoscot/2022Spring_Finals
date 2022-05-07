


def simulation(text='standard'):
    if text == 'standard':
        standard_simulation = """
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
            plt.title(f'Chicago River Dyeing Simulation'\n't={i}')
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
"""
        return standard_simulation
    else:
        river_l = int(round(input('Enter the river length:')))
        river_w = int(round(input('Enter the river width:')))
        num_simulate = 20
        custom_simulation = f"""
total_time = 0
fail_count = 0
total_percentage = 0

for s in range({num_simulate}):
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
            plt.title(f'Chicago River Dyeing Simulation'\n't={{i}}')
            # plt.show()
            plt.pause(0.3)
        i += 1
        percentage = s_river.r_plot[s_river.r_plot < 0.8 * 2.426*10**-4].size / s_river.r_plot.size
        if percentage <= 0.05 and time_95 == 0:
            time_95 = i
            total_time += time_95
            print(f'Complete the {{s+1}}th simulation in {{time_95}} seconds.')
            go = False
        elif i > 7200:
            fail_count += 1
            total_percentage += percentage
            print(f'Fail the {{s+1}}th simulation.')
            go = False
        # if (s_river.r_plot >= 0.8*2.426*10**-4).all() or i > 7200:
avg_time = round(total_time / (10 - fail_count), 0)
print('The average time to dye the river is:', format_timespan(avg_time))
if fail_count != 0:
    avg_percentage = 1 - round(total_percentage / fail_count, 2)
    print(f'There are {{fail_count}} simulations fail to cover the river with an average {{avg_percentage:.2%}} coverage rate.')
plt.ioff()
plt.show()
"""
        return custom_simulation


if __name__ == '__main__':
    # exec(simulation())
    print(simulation(123))
