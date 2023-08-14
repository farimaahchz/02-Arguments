# 02-Arguments
# Functions
Part 1: Greet Template

Define a function greet in main.py that takes these arguments, in this order:

A name (str)
A greeting template (str). Set this template parameter to 'Hello, <name>!' by default.
greet should return a string where <name> in the greeting template is replaced by the name given in the first parameter. 

Part 2: Force

Read this up to and including "Example: how much force to hold an apple with a mass of 0.1 kg?":

Math Is Fun -- Gravity
You should now understand the formula:

force = mass × gravity

Open up this page for reference:

Planetary Facts Sheet(opens in a new tab)
Write a function force that takes two arguments:

mass (float)
body (str), with 'earth' as its default. Your implementation should support all 10 bodies listed on the reference website given above (in lowercase). Make sure you process these bodies with the correlated gravity factor in a dictionary. Before using the gravity of a celestial body round its gravity factor to 1 decimal (if it's not already like that in the given data). You can "hardcode" this, for example: the gravity of Earth becomes 9.8.
The arguments should be named exactly as listed so that we can call them with keyword arguments. force should return the force that is exerted given the mass and body.

Part 3: Gravity

Write a function pull that takes three arguments:

m1 An object's mass in kg (float)
m2 Another object's mass in kg (float)
d Their distance in meters (float)
pull should return the gravitional pull that these two objects have on each other. You can test your function by entering in the examples given on the website



# Skills
Creating and indexing dictionaries;

Writing functions and function arguments;

Using various operators.
