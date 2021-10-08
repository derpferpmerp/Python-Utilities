from scipy import interpolate
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def smooth(xl, yl):
	x_new = np.linspace(min(xl), max(xl), 1000)
	spl = interpolate.make_interp_spline(xl, yl)
	y_new = spl(x_new)
	return x_new, y_new, spl
	
def generateColor(bounds=[0,255], amount=3, PLACES=2, norm=True):
	outlist = []
	for x in range(amount):
		outlist.append(random.randrange(bounds[0], bounds[1]))
	if not norm: bounds[1] = 1
	return tuple(list(map(lambda x: round(x / bounds[1], PLACES), outlist)))
	

		
	
