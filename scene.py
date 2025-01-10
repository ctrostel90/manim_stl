from manim import *
from math import atan2,sin,cos,sqrt
import numpy as np

class CreateCircle(Scene):
	def construct(self):
		
		pointList = [
			[-3,-1,0],
			[-1,0,1],
			[-1,2,2],
			[1,3,3],
			[2,1,1],
			[1.5,-1,3],
			[-2,-2.5,-1],
			[-4,-2,0]
		]

		p1 = Dot(point=pointList[0], color=PINK).set_stroke(YELLOW)
		p2 = Dot(point=pointList[1], color = GREEN).set_stroke(ORANGE)
		p3 = Dot(point=pointList[2], color = BLUE).set_stroke(WHITE)
		
		dots = []
		for pt in pointList:
			dots.append(Dot(point=pt))
		path = []
		width = 1.5
		start = get_two_point(
			get_inverse(pointList[0],pointList[1]),
			pointList[0],
			pointList[1],
			width
		)
		edge_dots=[]
		edge_dots.append([Dot(point=start[0]),Dot(point=start[1])])
		for i in range(0,len(dots) - 1):
			path.append(Line(dots[i],dots[i+1],color = PURPLE))
		for i in range(0,len(pointList) - 2):
			points = get_two_point(
				pointList[i],
				pointList[i+1],
				pointList[i+2],
				width
			)
			print(get_distance(points[0],points[1]))
			edge_dots.append([Dot(point=points[0]),Dot(point=points[1])])
		end = get_two_point(
			pointList[len(pointList)-2],
			pointList[len(pointList)-1],
			get_inverse(pointList[len(pointList) - 1],pointList[len(pointList)-2]),
			width
		)
		edge_dots.append([Dot(point=end[0]),Dot(point=end[1])])
		v1 = Line(pointList[0],pointList[1],color = PURPLE)
		v2 = Line(pointList[1],pointList[2],color = PURPLE)


		left,right = zip(*edge_dots)
		right = reversed(right)
		new_flat = list(left) + list(right)
		pt_list =[]
		for itm in new_flat:
			pt_list.append(itm.get_point_mobject().points[0])

		pipe = Polygon(
			*pt_list,
			color = PURPLE
		)
		pipe.fill_color = PURPLE
		
		

		for dot in dots:
			self.play(Create(dot),run_time = 0.5)
		for idx,p in enumerate(path):
			self.play(Create(p),rate_func = rate_functions.linear, run_time = 0.5 / (idx + 1))
			
		self.wait(1)
		for edge_group in edge_dots:
			self.play(Create(edge_group[0]),Create(edge_group[1]),run_time = 0.35)
		creation = Create(pipe)
		creation.set_run_time = 5.0
		self.play(creation, run_time = 5)
		self.wait(2)


def get_two_point(p1,p2,p3,width):
	vec21 = np.subtract(p2,p1)
	vec23 = np.subtract(p2,p3)
	angle = get_angle_between(vec21,vec23)
	if round(angle,2) == round(PI,2):
		return[
			unit_vector([-vec21[1],vec21[0],vec21[2]]) * -width / 2.0 + p2,
			unit_vector([-vec21[1],vec21[0],vec21[2]]) * width / 2.0 + p2
		]
	tmp = unit_vector(vec21) + unit_vector(vec23)
	
	angle23 = atan2(vec21[1],vec21[0]) - atan2(vec23[1],vec23[0])
	
	#normalize within pi,-pi
	if angle23 >= PI:
		angle23 -= 2 * PI
	elif angle23 <= -PI:
		angle23 += 2 * PI
	
	side = 1
	#correct for the side
	if angle23 < 0:
		side *= -1
	
	return [
		unit_vector(tmp) * side * width / 2.0 + p2,
		unit_vector(tmp) * side * -width / 2.0 + p2
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
		(p2[2] - p1[2]) * -1 + p1[2]		
	]

def get_distance(p1,p2):
	return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

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


