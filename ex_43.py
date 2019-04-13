from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

	def enter(self):
	    print("This scene is not yet configured.")
	    print("Subclass it and implement enter().")
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
		    next_scene_name = current_scene.enter()
		    current_scene = self.scene_map.next_scene(next_scene_name)
		    
		# be sure to print out the last scene
		current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud, if she were smarter.",
        "Such a loser.",
        "I have a small puppy that is better at this.",
        "You're worse than your dad's jokes."
        ]
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print(dedent("""
    		The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member anbd your last missions is to get the neutron destruct bomb from the weapons armory, put it in the bridge and blowl the ship up after getting into an escape pod.
    		
    		You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about pull a weapon to blast you.
		"""))
		action = input("> ")
		
		if action == "shoot!":
		    print(dedent("""
		        Quick on the draw, you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you.
		    """))
		return "death"
		
	elif action == "dodge!":
	    print(dedent("""
	    
	    """))
	


class LaserWeaponArmory(Scene):

	def enter(self):
		pass


class EscapePod(Scene):

	def enter(self):
		pass


class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


