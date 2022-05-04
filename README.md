# Title Chicago River Dyeing Monte Carlo Simulation
![Chicago River Dye](https://user-images.githubusercontent.com/63265733/166620957-35c910e8-a8bf-43b8-b17b-e130286ce070.jpeg)
## Team Member
Jiren Mao, ShengWen Wang, Zicheng Li
## Background:
In this project, our group simulates how long it takes for the Chicago River to dye green on St Patrick’s Day. St Patrick’s day is designed to memorialize Saint Patrick and celebrate the culture of the Irish. Chicago started to celebrate St Patrick’s Day by dyeing the river because of city workers’ misoperation. Since that dyeing, the Chicago River has become a traditional activity on St Patrick's Day. Therefore, we want to know whether **boat speed, dyeing spreading strategy, and boat movement** would influence the time of dyeing. 
## Hypothesis
* Boat spreed has associaltion with the time of dyeing 
* Dyeing spreading strategy has association with the time of dyeing
* Boat movement has association with the time of dyeing
## Assumptions of River
![Assumptions](https://user-images.githubusercontent.com/63265733/166622358-bd209fdc-1e7b-4611-a752-bd4c0ce5f4cd.jpeg)
* River Size: Length 545m, Width 70m, Depth 1m
* The water flow affects dissolving process is based on the flow speed and depth (average depth of 7)
* Dissolve effect has boundaries on both ends of the river 
## Assumption of Boat
* A small boat and a large boat will spread dye in river
* The boats carries **45 pounds** of dye powder in total
* The **velocity** of the boats is a constant
* Boats behavior:
	- Straight sailing back and forth along the river
	- Zigzag sailing back and forth along the river
	- Randomized sailing (high intention to low concentration areas)
## Assumptiona of Dye and Dissovle 
* Dye powder dissovles into water instanlty
* Dye weight/ Concentration **converstion ratio**
	- Concentration = Dye weight  / 100^3 * 1000
* Least Visible Dye concentration (LVC)
	- LVC = Total Dye Weight / (Length * Width * Depth) * 1000
* Dye spreading speed
	- Speed = mean + white noise
## Simplified Variables
* Dye diffusion coefficient
* Water flow speed in simulation is defined by:
	- V = mean + white noise 
* Ignore bend of the river
* Ignore disturbance of the boat
* Ignore dye decomposition
* Ignore vertical dimension dissolve effect
## Randomize Variables
* Diffusion effect through time
* Flow effect on diffusion through time
* Dye spreading speed
* Boats behaviour
## Standard Simulation
* Variable used
	1. 45 pounds of dye
		- Big boat : 5.67 g/s
		- Small boat: 1.89 g/s
	2. 2 boats
		- Big boat: speed 1.4 m/s, zigzag movement, spread dye with 3m width
		- Small boat: speed 2.8 m/s random movement, spread  dye with 1m width
	3. River size:  70m width * 545m length
* Complete: 95% of the pixels meet visible concentration
* Failure: cannot complete in 2 hours (7200 sec)
* Simulate 100 times
* The average time to dye the river is: **57 minutes and 52 seconds**
## Conclusion
* Different faster boat speed would dye the river faste
	- Boats speeds B: 2 m/s; S: 4 m/s
	- The average time to dye the river is: **41 minutes and 49 seconds** in red
* Different spreading strategy
	- Increase dye spreading B: 7.5 g/s; S: 2.5 g/s
	- The average time to dye the river is: **1 hour, 31 minutes and 24 seconds**
	- Decrease spreading B: 4.5 g/s; Increase spreading S: 2.1 g/s
	- The average time to dye the river is: **1 hour, 34 minutes and 30 seconds**
	- There are 9 simulations fail to cover the river with an average 94.00% coverage rate.
* Different boats movement
	- Change the big boat movement to straight sailing
	- The average time to dye the river is: **42 minutes and 36 seconds**
## Limitation and Future work
* Limitation
	- Ignore turbulence cause by the boat movement
	- Ignore river bend
	- Ignore dye decomposition
* Future work
	- Improve simulation speed: 15 mins for 100 simulation 
	- Add to 3D model
	- Custom boat movement style
