from sumopy.interface import SumoController
from constants import *
import math

# Convert screen coordinates to a new coordinate system with origin the
# bottom-middle of the screen.
def screen_to_local(pixel_x, pixel_y):
	return (pixel_x - IMAGE_WIDTH / 2, IMAGE_HEIGHT - pixel_y)


def distance_y(pixels):
	return (1.0 / (float(pixels * A1) + B1)) * C1 + D1

def distance_x(pixels_x, pixels_y):
	pixels_per_cm = (1.0 / (float(pixels_y * A2) + B2)) * C2
	return pixels_x / pixels_per_cm

def move_to_point(delta_x, delta_y, speed, verbose=False):
	if delta_y > 0:
		angle = math.degrees(math.tan(float(delta_x) / float(delta_y)))
		path_length = delta_y#get_path_length(delta_x, delta_y)
		duration = get_duration(speed, path_length)
		angle_per_sec = float(angle) / float(duration)
		turn_speed = get_turnspeed(angle_per_sec)

		controller = SumoController()
		controller.move(speed, 0, duration)

		if verbose:
			print "Pathlenght = " + str(path_length)
			print "Duration = " + str(duration)
			print "Speed = " + str(speed)
			print "Angle(degrees) = " + str(angle)
			print "Turnspeed = " + str(turn_speed)

def turn(angle, speed):
	return true

# This should roughly give the correct distance
def get_distance(speed, time):
	return (speed * DISTANCE_CONSTANT) * time + speed * STOP_CONSTANT

# This is a rewrite of the above formula
def get_duration(speed, distance):
	return float(distance - (speed * STOP_CONSTANT)) / float(speed * DISTANCE_CONSTANT)


def circle_radius(delta_x, delta_y):
	return math.sqrt((float(delta_x**2) + float(delta_y**2))/2.0)

# TODO not so sure about this
def get_path_length(delta_x, delta_y):
	radius = circle_radius(delta_x, delta_y)
	# we use a 90 degree angle, so we always have one quarter of the circle
	return 0.25 * 2 * math.pi * radius

def get_turnspeed(angle_per_sec):
	return BASIC_TURNSPEED * angle_per_sec

# Take a picture from the sumo
def picture(controller, name):
	controller.store_pic()
	pic = controller.get_pic()
	with open(name, 'wb') as f:
		f.write(controller.get_pic())

if __name__ == "__main__":
  move_to_point(0,100,50)
