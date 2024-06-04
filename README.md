# OBD Digital Gauge Cluster

This project was created by Rory Lange in December 2021 for a Programming Languages and Automata class at Wayne State University. This class was very challenging and the final 
project asked that I take myself out of my comfort zone and create a project in a language that I have never used before or am not familliar with. I chose to use Python and Pygame
for this project. I am somewhat familliar with python and I had heard of a free library named Pygame to create graphics for python applications. I used this library to create the 
project in this repository.

Unfortunately, the project did not go well. I did end up getting an A on the project for my effort, however, I had a lot of issues when trying to read data from my USB-A to OBDII 
scanner. I have never used one before and I did not know how to properly read the data from the car's OBDII port. Halfway into the project I came to the very real concern that if 
I ended up messing something up with the code or reading values from the OBDII scanner I could potentially brick the ECU in my car (my daily driver), thus, this project held too
much risk to continue any further.

Perhaps with more experience and research I will return to this project in the future. My dream for this project was to create an open source, DIY, and inexpensive alternative 
to the gauge view on a COBB AccessPort, just without all the ECU tuning capabilities that the comes with the AccessPort. I wanted to create a digital gauge cluster that could 
monitor certain diagnostics like Air/Fuel ratio, boost pressure, engine load, and oil temp with more precision than the secondary gauge cluster on my 2017 Ford Focus ST.

From this project I learned how to set achievable goals, conduct efficient research, and how to break down personal projects into smaller, achievable pieces. As I am wiriting this 
I am a Senior at Wayne State and I may return to this project in the near future, however, for the time being, this example gauge cluster is all I have to show for this passion 
project.

## Tech Stack

Python
Pygame
OBDII 
Raspberry PI
Linux CLI
