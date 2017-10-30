import turtle

def draw_shape():
	window = turtle.Screen()
	window.bgcolor("grey")
	brad = turtle.Turtle()
	brad.shape(None)
	brad.color("blue")
	brad.speed(30)
	index = 0
	while index < 36:
		for i in [0,1,2,3]:
			brad.fd(100)
			brad.lt(90)
		brad.fd(10)
		brad.lt(10)
		index +=1

	angie = turtle.Turtle()
	angie.shape(None)
	angie.speed(20)
	angie.color("yellow")
	index = 0
	while index < 36:
		angie.circle(30)
		angie.fd(10)
		angie.lt(10)
		index +=1

	john = turtle.Turtle()
	john.shape("turtle")
	john.color("green")
	john.speed(15)
	john.rt(90)
	john.fd(200)	
	john.rt(90)
	index = 0
	while index < 210:
		john.fd(100)
		john.rt (180)
		john.fd(100)
		john.rt(180)
		john.rt(30)
		index +=30

	window.exitonclick()

draw_shape()