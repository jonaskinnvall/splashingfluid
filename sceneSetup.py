import maya.cmds as cmds

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
