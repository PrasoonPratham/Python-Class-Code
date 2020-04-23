import pgzrun
from random import randint

apple = Actor('apple.png')

def draw():
	screen.clear()
	apple.draw()

def apple_place():
	apple.x = randint(10,300)
	apple.y = randint(10,200)

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print("Good Shot!")
		apple_place()
	else:
		print("You missed, noob.")	
		quit()
apple_place()

pgzrun.go()