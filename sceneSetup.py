import maya.cmds as cmds

container = cmds.polyCube(w=1, h=1, d=1, sx=5, sy=1, sz=5,
                          ax=(0, 1, 0), cuv=4, ch=1)
cmds.move(0, 0.5, 0, container)