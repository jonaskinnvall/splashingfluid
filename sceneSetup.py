import maya.cmds as cmds
import random
#Create new scene
cmds.file(f=True, new=True)

#Create ground polyCube
cmds.polyCube(w=10, d=10, h=0.01, sx=10, sy=10, sz=10, name='ground')

#Create wall polyCubes
wall = cmds.polyCube(w=10, d=0.01, h=2, sx=10, sy=10, sz=10, name='wall1')
cmds.move(0, 1, -5, wall)
wall = cmds.polyCube(w=10, d=0.01, h=2, sx=10, sy=10, sz=10, name='wall2')
cmds.move(0, 1, 5, wall)
wall = cmds.polyCube(w=0.01, d=10, h=2, sx=10, sy=10, sz=10, name='wall3')
cmds.move(-5, 1, 0, wall)
wall = cmds.polyCube(w=0.01, d=10, h=2, sx=10, sy=10, sz=10, name='wall4')
cmds.move(5, 1, 0, wall)


width = 5
depth = 5
height = 2


for w in range (-5, width):
    for d in range (-5, depth):
        for h in range (height):
            particles = cmds.polySphere(r=0.3, name='par#')
            cmds.move(w+ 0.5, h +0.5, d+ 0.5, particles)
            
            
cmds.group('par*', name='AllParticles')
cmds.gravity(m= 9.82, dx = 0, dy =-1 , dz = 0, vsh = 'none', name='grav')

cmds.connectDynamic(f='grav', 'AllParticles')
            