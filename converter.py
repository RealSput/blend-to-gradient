import json
import bpy
import os
import pyperclip

temp_objs_path = "" # Set the path to store temporary OBJ files here

if not os.path.exists(temp_objs_path): os.makedirs(temp_objs_path)

def convert_frame_to_obj(frame_number):
    obj_path = os.path.join(temp_objs_path, f"frame_{frame_number}.obj")
    bpy.ops.wm.obj_export(
        filepath=obj_path
    )
    return obj_path

def read_delete_append(obj_path, obj_list):
    with open(obj_path, 'r') as obj_file:
        obj_data = obj_file.read()
        obj_list.append(obj_data)
    os.remove(obj_path)    

frame_start = bpy.context.scene.frame_start
frame_end = bpy.context.scene.frame_end
obj_list = []

for frame_number in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame_number)
    obj_path = convert_frame_to_obj(frame_number)
    read_delete_append(obj_path, obj_list)

pyperclip.copy(json.dumps(obj_list))
