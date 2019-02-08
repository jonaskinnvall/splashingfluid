import maya.cmds as cmds
import maya.mel
#Create new scene
cmds.file(f=True, new=True)

#Create bowl
cmds.polySphere(r=3, ax=[0,1,0], cuv=2, name='bowl')
cmds.move(0,3,0, 'bowl')
#remove top
cmds.select('bowl.f[180:359]', 'bowl.f[380:399]')
cmds.delete()
cmds.select('bowl')
cmds.setAttr('lambert1.transparency', 0.9, 0.9, 0.9, type='double3')
maya.mel.eval("makeCollideNCloth")

#Create Rod
cmds.polyCube(w=4, h=0.5, d=0.3, name='rod')
cmds.move(0,0.25,0, 'rod')
cmds.select('rod')
cmds.rotate(0,45,0)
maya.mel.eval("makeCollideNCloth")

#Create liquid1
#cmds.nParticle( ll=[-1.4,5,-1.4], ur=[-1,35,-1], grs=0.2)
cmds.nParticle(ll=[-0.2, 5, -0.2], ur=[0.2, 100, 0.2], grs=0.2)
cmds.select('nParticleShape1')
cmds.setAttr('nParticleShape1.radius', 0.1)
cmds.setAttr('nParticleShape1.enableSPH', 1)
cmds.setAttr('nParticleShape1.selfCollide', 0)
cmds.setAttr('nParticleShape1.particleRenderType', 7)
cmds.setAttr('nParticleShape1.surfaceTension', 1)

cmds.setAttr('nParticleShape1.incompressibility', 3)
cmds.setAttr('nParticleShape1.viscosity', 0.01)
cmds.setAttr('nParticleShape1.radiusScaleSPH', 0.8)
cmds.setAttr('nParticleShape1.friction', 0.1)
cmds.setAttr('nParticleShape1.maxSelfCollisionIterations', 10)
cmds.setAttr('nParticleShape1.restDensity', 2.5)

#Create liquid2
cmds.nParticle( ll=[-1.4,5,-1.4], ur=[-1,35,-1], grs=0.2)
cmds.select('nParticleShape2')
cmds.setAttr('nParticleShape2.radius', 0.1)
cmds.setAttr('nParticleShape2.enableSPH', 1)
cmds.setAttr('nParticleShape2.selfCollide', 0)
cmds.setAttr('nParticleShape2.particleRenderType', 7)
cmds.setAttr('nParticleShape2.surfaceTension', 1)

cmds.setAttr('nParticleShape2.incompressibility', 3)
cmds.setAttr('nParticleShape2.viscosity', 0.01)
cmds.setAttr('nParticleShape2.radiusScaleSPH', 0.8)
cmds.setAttr('nParticleShape2.friction', 0.1)
cmds.setAttr('nParticleShape2.maxSelfCollisionIterations', 10)
cmds.setAttr('nParticleShape2.restDensity', 2.5)

#Animation
#keyFrames = 150
#cmds.playbackOptions( playbackSpeed = 0, maxPlaybackSpeed = 1, min = 1, max = 150 )
#startTime = cmds.playbackOptions( query = True, minTime = True )
#endTime = cmds.playbackOptions( query = True, maxTime = True )
#time = startTime
#keyStep = 1
