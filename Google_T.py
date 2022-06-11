def google_pho():
	import turtle as t
	root=t.Turtle()
	#t.speed(0)
	for x in range(1,5):
		if x==1:
			co="#D92E13"
		elif x==2:
			co="#4165BE"
		elif x==3:
			co="#03921C"
		elif x==4:
			co="#F6BB09"
		t.bgcolor("black")
		root.color(co)
		root.begin_fill()
		for i in range(400):
			if i==200:
				root.right(90)
				root.forward(130)
				root.penup()
				root.backward(130)
				root.right(90)
				root.pendown()
				break
			else:
				root.right(0.90)
				root.forward(1)
		root.end_fill()
		root.color("skyblue")
		root.begin_fill()
		root.forward(130)
		root.right(90)
	t.done()
def mistake_ani_sq():
	import turtle as t
	root=t.Turtle()
	for x in range(4):
		t.bgcolor("black")
		root.color("red")
		root.begin_fill()
		for i in range(400):
			if i==200:
				root.right(90)
				root.forward(130)
				root.penup()
				root.backward(130)
				root.right(90)
				root.pendown()
				break
			else:
				root.right(0.90)
				root.forward(1)
			root.end_fill()
			root.color("skyblue")
			root.begin_fill()
			root.forward(130)
			root.right(90)
	t.done()
def youtube():
	import turtle as t
	root=t.Turtle()
	root.color("red")
	root.begin_fill()
	for i in range(2):
		root.forward(145)
		for k in range(40):
			if k>30:
				pass
			else:
				root.right(3)
				root.forward(4)
		root.left(3)
		root.forward(140)
		for j in range(40):
			if j>30:
				pass
			else:
				root.right(3)
				root.forward(4)
		root.left(3)
		root.forward(145)
	root.end_fill()
	root.pencolor("red")
	root.left(180)
	root.forward(50)
	root.left(90)
	root.forward(80)
	root.pencolor("white")
	root.color('white')
	root.begin_fill()
	root.forward(140)
	root.left(120)
	root.forward(140)
	root.left(120)
	root.forward(140)
	root.end_fill()
	t.done()
def assistent():
	import turtle as t
	root=t.Turtle()
	root.penup()
	root.backward(130)
	root.pendown()
	root.color("#287CF5")
	root.begin_fill()
	root.circle(140)
	root.end_fill()
	root.penup()
	root.forward(220)
	
	root.pendown()
	root.color("#EB4014")
	root.begin_fill()
	root.circle(65)
	root.end_fill()
	
	root.right(90)
	root.penup()
	root.forward(180)
	root.pendown()
	root.color("#FBBF04")
	root.begin_fill()
	root.left(90)
	root.circle(78)
	root.left(68)
	root.penup()
	root.forward(150)
	root.end_fill()
	root.forward(200)
	root.pendown()
	root.color("green")
	root.begin_fill()
	root.circle(35)
	root.end_fill()
	t.done()
	
if __name__=="__main__":
	#youtube()
	#google_pho()
	assistent()
	
	#mistake_ani_sq()
