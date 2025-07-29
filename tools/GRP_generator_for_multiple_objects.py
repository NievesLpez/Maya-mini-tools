"""
Author: Nieves López

May 2025

Description : For selected objects (CTRLS) creates the main CTRL structure.
"""
import maya.cmds as cmds

selObj = cmds.ls(sl=True)
if len(selObj) == 0:
    cmds.warning("No objects selected")
else:
    for i in range(len(selObj)):
        
        # Get the position and pivot of the selection
        objRot = cmds.xform(selObj[i], q=True, ws=True, ro=True)
        objTrans = cmds.xform(selObj[i], q=True, ws=True, t=True)
        objScale = cmds.xform(selObj[i], q=True, r=True, s=True)
        objWSRotPivot = cmds.xform(selObj[i], q=True, ws=True, rp=True)
        objWSScalePivot = cmds.xform(selObj[i], q=True, ws=True, sp=True)
        
        # Group one time
        GRP1 = cmds.createNode("transform", name=selObj[i] + "_ANIM")
        cmds.xform(GRP1, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP1, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(selObj[i], GRP1)
        
        # Group second time
        GRP2 = cmds.createNode("transform", name=selObj[i] + "_SDK")
        cmds.xform(GRP2, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP2, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP1, GRP2)
        
        # Group third time
        GRP3 = cmds.createNode("transform", name=selObj[i] + "_OFF")
        cmds.xform(GRP3, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP3, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP2, GRP3)
        
        # Group fourth time
        GRP4 = cmds.createNode("transform", name=selObj[i] + "_SPC")
        cmds.xform(GRP4, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP4, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP3, GRP4)
        
        # Group fifth time
        GRP5 = cmds.createNode("transform", name=selObj[i] + "_GRP")
        cmds.xform(GRP5, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP5, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP4, GRP5)
        
        cmds.rename(selObj[i], f"{selObj[i]}_CTL")

cmds.select(cl=True)
