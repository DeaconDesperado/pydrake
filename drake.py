__author__ = 'deacondesperado'

import random
import math

def drake(map):
	if type(map)==list:
		map = drakify(map)
	print 'Number of stars in the Milky Way %f' % map['R']
	print 'Fraction of stars with planetary systems %f' % map['Fp']
	print 'Number of planets suitable for life %f' % map['Ne']
	print 'Fraction of suitable planets that develop life %f' %  map['Fl']
	print 'Fraction of life that becomes sentient and eventually intelligent %f' % map['Fi']
	print 'Fraction of intelligent life that advances to the point of communication %f' %  map['Fc']
	print 'Adjustment for incidence of self-destruction %g' % map['L']
	N = map['R']*map['Fp']*map['Ne']*map['Fl']*map['Fi']*map['Fc']*map['L']
	print N
	return N


def drakify(vals):
	vars = ['R','Fp','Ne','Fl','Fi','Fc','L']
	map = dict()

	if len(vals)!=len(vars):
		raise Exception('Invalid number of values passed')

	for key in range(len(vars)):
		map[vars[key]]=vals[key]
	return map

def genrand():
	vals = dict()
	vals['R'] = 1E11
	vals['Fp'] = random.uniform(0.1,0.3)
	vals['Ne'] = random.randrange(1,5)
	vals['Fl'] = random.uniform(0.1,0.5)
	vals['Fi'] = random.uniform(0.01,0.2)
	vals['Fc'] = random.uniform(0.01,0.2)
	vals['L'] = daysearth()
	return vals

def daysearth():
	age = 4.54E7
	indays = age*365
	cc = 50*365
	L = cc/indays
	return L


if __name__ == '__main__':
	sagan_vals = [1E11,.25,2,.5,.1,.1,1E-8]
	N = drake(genrand())
	print math.floor(N)
