from manim import *
from math import atan2,sin,cos
import numpy as np

class CreateCircle(Scene):
	def construct(self):
		
		pointList = [
			[1,-2,0],
			[-1,0,0],
			[1,2,0]
		]

		p1 = Dot(point=pointList[0], color=PINK).set_stroke(YELLOW)
		p2 = Dot(point=pointList[1], color = GREEN).set_stroke(ORANGE)
		p3 = Dot(point=pointList[2], color = BLUE).set_stroke(WHITE)
		
		v1 = Line(pointList[0],pointList[1],color = PURPLE)
		v2 = Line(pointList[1],pointList[2],color = PURPLE)

		width = 1

		left_right = get_two_point(
						get_inverse(pointList[0],pointList[1]),
						pointList[0],
						pointList[1],
						width)
		p1_l = Dot(
			point=left_right[1],
			color=GREEN_A,
			stroke_width=2)
		p1_l.stroke_color = YELLOW
		p1_r = Dot(
			point=left_right[0],
			color=PINK,
			stroke_width=2)
		p1_r.stroke_color = YELLOW

		left_right = get_two_point(pointList[0],pointList[1],pointList[2],width)
		p2_l = Dot(
			point=left_right[1],
			color=GREEN_A,
			stroke_width=2)
		p2_l.stroke_color = ORANGE
		p2_r = Dot(
			point=left_right[0],
			color=PINK,
			stroke_width=2)
		p2_r.stroke_color = ORANGE

		left_right = get_two_point(
						pointList[1],
						pointList[2],
						get_inverse(pointList[2],pointList[1]),
						width)
		p3_l = Dot(
			point=left_right[1],
			color=GREEN_A,
			stroke_width=2)
		p3_l.stroke_color = WHITE
		p3_r = Dot(
			point=left_right[0],
			color=PINK,
			stroke_width=2)
		p3_r.stroke_color = WHITE

		pt_list =[
			p3_r.get_point_mobject().points[0],
			p2_r.get_point_mobject().points[0],
			p1_r.get_point_mobject().points[0],
			p1_l.get_point_mobject().points[0],
			p2_l.get_point_mobject().points[0],
			p3_l.get_point_mobject().points[0]]
		
		pipe = Polygon(
			*pt_list,
			color = PURPLE
		)
		pipe.fill_color = PURPLE
		
		self.add(p1,p2,p3,p1_l,p1_r,p2_l,p2_r,p3_l,p3_r)
		self.play(Create(v1))
		self.play(Create(v2))
		self.wait(1)
		creation = Create(pipe)
		creation.set_run_time = 5.0
		self.play(creation)
		self.wait(2)


def get_two_point(p1,p2,p3,width):
	vec21 = np.subtract(p2,p1)
	vec23 = np.subtract(p2,p3)
	angle = get_angle_between(vec21,vec23)
	if round(angle,2) == round(PI,2):
		if 
		return[
			unit_vector(np.array([-vec21[1],vec21[0],vec21[2]])) * -width / 2 + p2,
			unit_vector(np.array([-vec21[1],vec21[0],vec21[2]])) * width / 2 + p2
		]
	tmp = unit_vector(vec21) + unit_vector(vec23)
	print(f"tmp: {tmp} angle:{angle*180/PI}")
	return [
		tmp * width / 2 + p2,
		tmp * -width / 2 + p2
	]

def rotate_vector(vector,rotation):
	return [
		vector[0] * cos(rotation) - vector[1] * sin(rotation),
		vector[0] * sin(rotation) + vector[1] * cos(rotation),
		vector[2]
	]

def get_inverse(p1,p2):
	return [ 
		(p2[0] - p1[0]) * -1 + p1[0],
		(p2[1] - p1[1]) * -1 + p1[1],
		0		
	]

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def get_angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


