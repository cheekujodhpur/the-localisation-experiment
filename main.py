#!/usr/bin/env/python

import numpy as np

k = 1		#base wavenumber
dk = 0.01	#the variation

#create each of the waves
psi = []
for i in range(-50,50):
	ran = (k+i*dk)*np.array(range(-100,100))
	psi.append(np.sin(ran))

#add all waves to get wavefunction
psi = np.array(sum(psi))
#normalize it
psi = psi/np.sqrt(sum(psi.conjugate()*psi))

#We have the normalized wave function

#get expectation value of x
exp_x = []
for i in range(-100,100):
	exp_x.append(psi.conjugate()[i+100]*i*psi[i+100])
exp_x = sum(exp_x)

#get expectation value of x^2
exp_xs = []
for i in range(-100,100):
	exp_xs.append(psi.conjugate()[i+100]*i*i*psi[i+100])
exp_xs = sum(exp_xs)

#get deviation in x 
del_x = np.sqrt(exp_xs-exp_x**2)
