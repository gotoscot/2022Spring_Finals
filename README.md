# Chicago River Dyeing Monte Carlo Simulation
![Chicago River Dye](https://user-images.githubusercontent.com/63265733/166620957-35c910e8-a8bf-43b8-b17b-e130286ce070.jpeg)
## Team Member
Jiren Mao, ShengWen Wang, Zicheng Li
## Background
In this project, our group simulates how long it takes for the Chicago River to dye green on St Patrick’s Day. St Patrick’s day is designed to memorialize Saint Patrick and celebrate the culture of the Irish. Chicago started to celebrate St Patrick’s Day by dyeing the river because of city workers’ misoperation. Since that dyeing, the Chicago River has become a traditional activity on St Patrick's Day. Therefore, we want to know whether **boat speed, dyeing spreading strategy, and boat movement** would influence the dyeing time
## Hypothesis
* Increased boat speed will speed up the dyeing speed
* Spread the dye faster will reduce dyeing time
* Straight-lin sailing will slow down the dyeing time
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
## Demo
![Beginning of the Simulation](https://user-images.githubusercontent.com/63265733/167282604-5a64817b-7421-4fba-9594-ee8f1dd503ae.jpeg)
![Ending of Simulation](https://user-images.githubusercontent.com/63265733/167282609-9fff3267-b1b1-47ba-bd4b-6a1da23b7a7c.jpeg)
## Conclusion
![Examples for testing hypothesis](https://user-images.githubusercontent.com/63265733/167282527-72584cc2-8233-4013-8cf6-d1c26234a852.jpg)
* Increased boat speed will speed up the dyeing speed
    - Boats speeds B: 2 m/s; S: 4 m/s
    - The average time to dye the river is: **41 minutes and 49 seconds** in red
    - Faster boat speed will increase the dyeing speed
* Spread the dye faster will reduce dyeing time
    - Increase dye spreading B: 7.5 g/s; S: 2.5 g/s
    - The average time to dye the river is: **1 hour, 31 minutes and 24 seconds**
    - Decrease spreading B: 4.5 g/s; Increase spreading S: 2.1 g/s
    - The average time to dye the river is: **1 hour, 34 minutes and 30 seconds**
    - There are 9 simulations fail to cover the river with an average 94.00% coverage rate.
    - Increasing dye spreading speed on the small boat will slower the dyeing speed
    - The change in dye spreading speed of big boat has less influence. Need more simulation to find a trend. 
* Straight-lin sailing will slow down the dyeing time
    - Change the big boat movement to straight sailing
    - The average time to dye the river is: **42 minutes and 36 seconds**
    - The straight sailing will in fact increase the dyeing speed
## Limitation and Future work
* Limitation
	- Ignore turbulence cause by the boat movement
	- Ignore river bend
	- Ignore dye decomposition
* Future work
	- Improve simulation speed: 15 mins for 100 simulation 
	- Add to 3D model
	- Custom boat movement style
## Reference
-  Andrew, S. (2022, March 17). Why Chicago Dyes Its River Green for st. patrick's day. CNN. Retrieved May 7, 2022, from
	https://www.cnn.com/2022/03/17/us/chicago-river-dyed-green-st-patricks-day-explained-cec/index.html
- Dolgopolova E. Turbulent Diffusion and Eddy Scales in Rivers. Water Resources. 46:S11-S19. doi:10.1134/S0097807819070042
- García, Marcelo. (2008). Sediment Transport and Morphodynamics. 10.1061/9780784408148.ch02
- Measuring Gravity Currents in the Chicago River, Chicago, Illinois - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Cross-section-of-Chicago-River-at-Columbus-Drive-Chicago-IL-Vertical-scale-exaggerated_fig2_4326253
- St. Patrick's day chicago: Top ways to celebrate. Choose Chicago. (2022, March 8). Retrieved May 7, 2022, from 		https://www.choosechicago.com/articles/holidays/st-patricks-day-chicago/ 
- USGS 05536123 CHICAGO RIVER AT COLUMBUS DRIVE AT CHICAGO, IL. USGS Water Resources. (n.d.). Retrieved from https://waterdata.usgs.gov/nwis/uv?cb_72254=on&amp;format=gif&amp;site_no=05536123&amp;period=&amp;begin_date=2022-03-01&amp;end_date=2022-03-31 
- Wood, J. M. (2022, March 17). How do they dye the Chicago River Green for st. patrick's day? Mental Floss. Retrieved May 7, 2022, from 			https://www.mentalfloss.com/article/62220/what-do-they-use-dye-chicago-river-green-st-patricks-day
