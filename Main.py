# setup
from mpl_toolkits import mplot3d
import numpy as np
import random
import matplotlib.pyplot as plt
from time import *

plt.ion()
fig = plt.figure()
ax = plt.axes(projection='3d')

# variables
# units in cm, rad
targetpoint = [0,0,0]
axis1height = 5
axis2length = 50
axis3length = 50
axis4length = 10
axis5length = 10
axis6length = 10
yaw = 1
pitch = 1
roll = 0 #not used as it is inconsequencial to the coordinates of any of the lines
origin = [0,0,0]
base = [0,0,-axis1height]
joint1 = [0,0,0]
joint2 = [0,0,0]
joint3 = [0,0,0]
axis1angle = 0
axis2angle = 0
axis3angle = 0

plt.xlim((axis2length+axis3length+axis4length+axis5length+axis6length+10)*-1, axis2length+axis3length+axis4length+axis5length+axis6length+10)
plt.ylim((axis2length+axis3length+axis4length+axis5length+axis6length+10)*-1, axis2length+axis3length+axis4length+axis5length+axis6length+10)
ax.set_zlim((axis2length+axis3length+axis4length+axis5length+axis6length+10)*-1, axis2length+axis3length+axis4length+axis5length+axis6length+10)

# Functions
def mainloop():
	global targetpoint

	while True: 
		create_line(origin, base)
		create_line(origin, joint3)
		create_line(joint3, joint2)
		create_line(joint2, joint1)
		create_line(joint1, targetpoint)
		fig.canvas.draw()
		fig.canvas.flush_events()
		ax.lines.clear()
		calc_angles()
		calc_points()

def calc_points(): 
	global joint1
	global joint2
	global joint3

	joint1 = [targetpoint[0]-np.sin(yaw)*np.cos(pitch)*(axis5length+axis6length), targetpoint[1]-np.cos(yaw)*np.cos(pitch)*(axis5length+axis6length), targetpoint[2]-np.sin(pitch)*(axis5length+axis6length)]
	joint2 = [joint1[0]-np.sign(joint1[0])*np.cos(np.arctan(joint1[1]/joint1[0]))*np.cos(pitch)*axis4length,joint1[1]-(joint1[0]/np.absolute(joint1[0]))*np.sin(np.arctan(joint1[1]/joint1[0]))*np.cos(pitch)*axis4length,joint1[2]-np.sin(pitch)*axis4length]
	joint3 = [np.sin(axis1angle)*np.cos(axis2angle)*axis2length,np.cos(axis1angle)*np.cos(axis2angle)*axis2length,np.sin(axis2angle)*axis2length]

def create_line(point1, point2):
	lines = ax.plot([point1[0],point2[0]],[point1[1],point2[1]], [point1[2],point2[2]])

def calc_angles():
	global axis1angle
	global axis2angle
	global axis3angle
	if joint2[0] != 0 and joint2[1] != 0:
		if joint2[1] == 0:
			axis1angle = np.pi/2*np.sign(joint2[0])
			axis2angle = np.arccos((axis2length**2+joint2[0]**2+joint2[1]**2+joint2[2]**2-axis3length**2)/(2*axis2length*np.sqrt(joint2[0]**2+joint2[1]**2+joint2[2]**2)))+np.pi/2
		else:
			axis1angle = np.arctan(joint2[0]/joint2[1])+(1-np.absolute(joint2[1])/joint2[1])/2*np.pi
			axis2angle = np.arccos((axis2length**2+joint2[0]**2+joint2[1]**2+joint2[2]**2-axis3length**2)/(2*axis2length*np.sqrt(joint2[0]**2+joint2[1]**2+joint2[2]**2)))+np.arctan(joint2[2]/np.sqrt(joint2[0]**2+joint2[1]**2))
		axis3angle = np.arccos((axis2length**2-joint2[0]**2-joint2[1]**2-joint2[2]**2+axis3length**2)/(2*axis2length*axis3length))

def move(event):
	global targetpoint
	global yaw
	global pitch

	if event.key == '1':
		targetpoint[0] -= 1
	if event.key == '2':
		targetpoint[0] += 1
	if event.key == '3':
		targetpoint[1] -= 1
	if event.key == '4':
		targetpoint[1] += 1
	if event.key == '5':
		targetpoint[2] -= 1
	if event.key == '6':
		targetpoint[2] += 1
	if event.key == '7':
		yaw += np.pi/45
	if event.key == '8':
		yaw -= np.pi/45
	if event.key == '9':
		pitch += np.pi/45
	if event.key == '0':
		pitch -= np.pi/45

# Main
fig.canvas.mpl_connect('key_press_event', move)
mainloop()
