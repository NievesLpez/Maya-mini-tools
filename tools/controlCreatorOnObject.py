"""
Author: Nieves López

June 2025

Description : Creates a NURBS curve and its control hierarchy for selected objects, using each object's name and position.
"""

import maya.cmds as cmds

selObj = cmds.ls(sl=True)
if len(selObj) == 0:
    cmds.warning("No objects selected")
else:
    for i in range(len(selObj)):
        
        # Get the values of the object
        objRot = cmds.xform(selObj[i], q=True, ws=True, ro=True)
        objTrans = cmds.xform(selObj[i], q=True, ws=True, t=True)
        objScale = cmds.xform(selObj[i], q=True, r=True, s=True)
        objWSRotPivot = cmds.xform(selObj[i], q=True, ws=True, rp=True)
        objWSScalePivot = cmds.xform(selObj[i], q=True, ws=True, sp=True)
        
        # Get base name by removing everything after the last underscore
        objName = selObj[i]
        
        if "_" in objName:
            # Find the last underscore and take everything before it
            lastUnderscore = objName.rfind("_")
            baseName = objName[:lastUnderscore]
        else:
            # If no underscore, use the whole name
            baseName = objName
        
        # Create circle control with CTL naming
        ctlName = baseName + "_CTL"
        
        # Create circle control
        circleCtl = cmds.circle(name=ctlName, normal=(0, 1, 0), radius=1)[0]
        
        # Position the circle control at the object's location
        cmds.xform(circleCtl, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(circleCtl, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        
        # Group one time
        GRP1 = cmds.createNode("transform", name=baseName + "_ANIM")
        cmds.xform(GRP1, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP1, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(circleCtl, GRP1)
        
        # Group second time
        GRP2 = cmds.createNode("transform", name=baseName + "_SDK")
        cmds.xform(GRP2, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP2, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP1, GRP2)
        
        # Group third time
        GRP3 = cmds.createNode("transform", name=baseName + "_OFF")
        cmds.xform(GRP3, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP3, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP2, GRP3)
        
        # Group fourth time
        GRP4 = cmds.createNode("transform", name=baseName + "_SPC")
        cmds.xform(GRP4, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP4, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP3, GRP4)
        
        # Group fifth time
        GRP5 = cmds.createNode("transform", name=baseName + "_GRP")
        cmds.xform(GRP5, ws=True, t=objTrans, ro=objRot, s=objScale)
        cmds.xform(GRP5, p=True, ws=True, rp=objWSRotPivot, sp=objWSScalePivot)
        cmds.parent(GRP4, GRP5)
        
        cmds.select(cl=True)
