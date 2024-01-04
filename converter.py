import json
import bpy
import os
import pyperclip

# Set the path to store temporary OBJ files
temp_objs_path = "C:\\Users\\Diego\\Downloads\\temp_objs"

# Create the directory if it doesn't exist
if not os.path.exists(temp_objs_path):
    os.makedirs(temp_objs_path)

# Function to convert each frame to OBJ and store it temporarily
def convert_frame_to_obj(frame_number):
    # Set the output OBJ file path
    obj_path = os.path.join(temp_objs_path, f"frame_{frame_number}.obj")

    # Set the output folder for the OBJ export
    bpy.ops.wm.obj_export(
        filepath=obj_path
    )

    return obj_path

def read_delete(path):
    dat = ""
    with open(path, 'r') as file:
        data = file.read()
        dat = data
    os.remove(path)
    return dat
        
def read_delete_append(obj_path, obj_list):
    r = read_delete(obj_path)
    obj_list.append(r)
    
def copy_list_to_clipboard(obj_list):
    pyperclip.copy(json.dumps(obj_list))

# Example usage
frame_start = bpy.context.scene.frame_start
frame_end = bpy.context.scene.frame_end
obj_list = []
final_res = []

for frame_number in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame_number)
    obj_path = convert_frame_to_obj(frame_number)
    read_delete_append(obj_path, obj_list)

mtl_res = read_delete(os.path.join(temp_objs_path, f"frame_{frame_number}.mtl"))
final_res.append(mtl_res)
final_res.append(obj_list)

# Copy the list to the clipboard
copy_list_to_clipboard(final_res)
 
