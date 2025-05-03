"""
Created by Nieves López 
Date: 2025 May

Description : tool that connects an attribute to another attribute of the selected object/s so you can avoid connecting them manually.

"""

import maya.cmds as cmds

def connect_with_inputs():
    source_input = cmds.promptDialog(
        title="Attribute connector tool",
        message="Enter name + . + attribute:",
        button=["OK", "Cancel"],
        defaultButton="OK",
        cancelButton="Cancel",
        dismissString="Cancel"
    )
    
    if source_input == "Cancel":
        return  
    
    source_plug = cmds.promptDialog(query=True, text=True)
    
    target_attr = cmds.promptDialog(
        title="Target Attribute",
        message="Enter target attribute:",
        button=["OK", "Cancel"],
        defaultButton="OK",
        cancelButton="Cancel",
        dismissString="Cancel",
    )
    
    if target_attr == "Cancel":
        return
    
    target_attr = cmds.promptDialog(query=True, text=True)
    
    selected_objects = cmds.ls(selection=True)  
    
    if not selected_objects:
        cmds.warning("Invalid selection")
        return
    
    for obj in selected_objects:
        target_plug = f"{obj}.{target_attr}"
        try:
            cmds.connectAttr(source_plug, target_plug, force=True)
            print(f"Connected: {source_plug} → {target_plug}")
        except Exception as e:
            cmds.warning(f" Failed to connect {source_plug} to {target_plug}: {str(e)}")

connect_with_inputs()
