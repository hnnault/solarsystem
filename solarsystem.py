import turtle
import math
import random

# Solar System class where the planets and stuff will be stored
class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle() # creates the turtle
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen() # creates the screen
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0) # the dimentions of the screen
        self.ssscreen.tracer(50) # traces the circles or the orbit.

    # set thesun variable to the sun
    def addSun(self, asun):
        self.thesun = asun

    def addPlanets(self, aplanet):
        self.planets.append(aplanet) # add planet to the planets array
    
    def movePlanets(self):
        G = .1
        dt = .001
        #some crazy math stuff to make the planets move
        for p in self.planets:
            # move the planet based on vel and position
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())
            
            # calculates position in relation of the sun
            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)

            #gravitational pull of the sun
            gravityx = G * self.thesun.getMass()*rx/r**3
            gravityy = G * self.thesun.getMass()*ry/r**3

            # sets the new x and y veloctiy based on the pull of the sun
            p.setXVel(p.getXVel() + dt * gravityx)
            p.setYVel(p.getYVel() + dt * gravityy)
        
class Sun:
    def __init__(self, sname, srad, smass):
        self.name = sname # name of sun
        self.radius = srad # radius of the sun
        self.mass = smass # mass of the sun
        self.x = 0 # center of the screen
        self.y = 0 # center of the screen

        # create yellow circle
        self.sturtle = turtle.Turtle() 
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")
        self.sturtle.shapesize(3,3,1)

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

# Create planets
class Planet:
    def __init__(self, pname, prad, pmass, pdist, pvx, pvy, pcolor):
        self.name = pname
        self.radius = prad
        self.mass = pmass
        self.distance = pdist
        self.x = pdist
        self.y = 0
        self.velocityx = pvx
        self.velocityy = pvy
        self.color = pcolor

        self.pturtle = turtle.Turtle()
        self.pturtle.up() # so there is no line from 0,0 to wherever the planet is
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.shapesize(self.radius,self.radius,1)
        self.pturtle.down() # add line again when the position is corrected
            

    def getName(self):
        return self.name
    def getRadius(self):
        return self.radius
    def getMass(self):
        return self.mass
    def getDistance(self):
        return self.distance
    def getXPos(self):
        return self.x
    def getYPos(self):
        return self.y
    def getXVel(self):
        return self.velocityx
    def getYVel(self):
        return self.velocityy

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)
    
    def setXVel(self, newvelx):
        self.velocityx = newvelx

    def setYVel(self, newvely):
        self.velocityy = newvely

    # Add moon to planet
    def addMoons(self, amoon):
        self.moons.append(amoon) # add moon to the moons array

# Create the stars in the universe
def createStars():
    star = turtle.Turtle()
    star.up() # get rid of line 
    star.color("white")
    star.shape("circle")
    star.shapesize(0.1,0.1,1) # small
    star.setpos(random.uniform(-2,2),random.uniform(-2,2)) # random float position between -2 and 2, x and y. 


def createSSandAnimate(): # function that actually creates the solar system
    ss = SolarSystem(2,2)
    turtle.bgcolor("black")

    #create 200 stars
    for i in range(200):
        createStars()
    
    # Add the sun
    sun = Sun("SUN", 5000, 10) 
    ss.addSun(sun)

    #c reate earth
    m = Planet("EARTH", 1.1, 5000, 0.36, 0, 1.75, "green") # name, radius, mass, distance, velocity x&y, color
    ss.addPlanets(m)

    # create mars
    mars = Planet("MARS", 0.8, 5000, 0.6, 0, 1.3, "orange")
    ss.addPlanets(mars)

    # create mercury
    mercury = Planet("MERCURY", 0.5, 5000, 0.24, 0, 1.9, "gray")
    ss.addPlanets(mercury)

    # create venus
    venus = Planet("VENUS", 0.9, 5000, 0.29, 0, 1.9, "yellow")
    ss.addPlanets(venus)

    # create jupiter
    jupiter = Planet("JUPITER", 1.5, 5000, 0.75, 0, 1.16, "yellow")
    ss.addPlanets(jupiter)

    # create saturn
    saturn = Planet("SATURN", 1.3, 5000, 0.85, 0, 1.1, "orange")
    ss.addPlanets(saturn)

    numTimePeriods = 200000
    for amove in range(numTimePeriods): # move the planets
        ss.movePlanets()

createSSandAnimate() # run the function to start

turtle.mainloop() # make sure it doesn't close instantly