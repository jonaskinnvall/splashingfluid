import maya.cmds as cmds
# import random
# Create new scene
cmds.file(f=True, new=True)

# Create ground polyCube
cmds.polyPlane(w=20, h=20, sx=10, sy=10, name='ground')


# Create wall polyCubes
wall = cmds.polyPlane(w=20, h=2, sx=10, sy=10, name='wall1')
cmds.move(0, 1, -10, wall)
cmds.rotate('90deg', 0, 0, r=True)

wall = cmds.polyPlane(w=20, h=2, sx=10, sy=10, name='wall2')
cmds.move(0, 1, 10, wall)
cmds.rotate('-90deg', 0, 0, r=True)

wall = cmds.polyPlane(w=2, h=20, sx=10, sy=10, name='wall3')
cmds.move(-10, 1, 0, wall)
cmds.rotate(0, 0, '-90deg', r=True)

wall = cmds.polyPlane(w=2, h=20, sx=10, sy=10, name='wall4')
cmds.move(10, 1, 0, wall)
cmds.rotate(0, 0, '90deg', r=True)

cmds.group('ground', 'wall1', 'wall2', 'wall3', 'wall4', name='box')
cmds.select('box')
cmds.rotate('15deg', 0, 0, r=True)
cmds.rigidBody(passive=True, name='rigidBodyBox')

cmds.gravity(pos=[0, 0, 0], m=9.82, dx=0, dy=-1, dz=0, vsh='none', name='grav')

width = 5
depth = 5
height = 8


for w in range(-5, -3):
    for d in range(-5, depth):
        for h in range(2, height):
            particles = cmds.polySphere(r=0.3, name='par#')
            cmds.move(w+0.5, h, d+0.5, particles)
            cmds.connectDynamic(particles, f='grav')

for w in range(3, 5):
    for d in range(-5, depth):
        for h in range(2, height):
            particles = cmds.polySphere(r=0.3, name='par#')
            cmds.move(w+0.5, h, d+0.5, particles)
            cmds.connectDynamic(particles, f='grav')

cmds.group('par*', name='AllParticles')