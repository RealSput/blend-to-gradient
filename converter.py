import json
import bpy
import os
import pyperclip

# Set the path to store temporary OBJ and MTL files
temp_objs_path = ""

if not os.path.exists(temp_objs_path): os.makedirs(temp_objs_path)

def convert_frame_to_obj(frame_number):
    obj_path = os.path.join(temp_objs_path, f"frame_{frame_number}.obj")
    bpy.ops.wm.obj_export(
        filepath=obj_path,
        export_triangulated_mesh=True
    )
    return obj_path

def read_delete(path):
    dat = ""
    with open(path, 'r') as file:
        data = file.read()
        dat = data
    os.remove(path)
    return dat

frame_start = bpy.context.scene.frame_start
frame_end = bpy.context.scene.frame_end
obj_list = []
final_res = []

for frame_number in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame_number)
    obj_path = convert_frame_to_obj(frame_number)
    r = read_delete(obj_path)
    obj_list.append(r)

mtl_res = read_delete(os.path.join(temp_objs_path, f"frame_{frame_number}.mtl"))
final_res.append(mtl_res)
final_res.append(obj_list)

pyperclip.copy(json.dumps(final_res)) 
