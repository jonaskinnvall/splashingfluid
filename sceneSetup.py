import maya.cmds as cmds
import maya.mel
#Create new scene
cmds.file(f=True, new=True)

#Create polyCube
cmds.polyCube(w=3, h=2, d=3, name='box')
cmds.move(0,1,0, 'box')
#remove lid
cmds.select('box.f[1]')
cmds.delete()
cmds.select('box')
cmds.setAttr('lambert1.transparency', 0.9, 0.9, 0.9, type='double3')
maya.mel.eval("makeCollideNCloth")

cmds.nParticle( ll=[-1,5,-1], ur=[1,9,1], grs=0.2)
cmds.select('nParticleShape1')
cmds.setAttr('nParticleShape1.radius', 0.1)