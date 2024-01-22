import json
import bpy
import os

def dupframe():
    original_objects = tuple(bpy.context.scene.objects)
    bpy.ops.object.select_all(action='DESELECT')
    duplicated_meshes = []

    def dupmesh(original_mesh):
        if original_mesh.type == 'MESH':
            original_mesh.select_set(True)
            bpy.context.view_layer.objects.active = original_mesh
            bpy.ops.object.duplicate(linked=False)
            duplicate = bpy.context.active_object
            duplicate.animation_data_clear()
            duplicate.select_set(True)
            duplicated_meshes.append(duplicate)

    for obj in original_objects:
        dupmesh(obj)
        bpy.ops.object.select_all(action='DESELECT')

    for duplicate_mesh in duplicated_meshes:
        duplicate_mesh.animation_data_clear()
        duplicate_mesh.select_set(True)

    bpy.context.view_layer.objects.active = duplicated_meshes[0] 
    bpy.ops.object.join()   

temp_objs_path = "" # insert path to temp objs folder
output_file = "" # insert path to output JSON file

if not os.path.exists(temp_objs_path): os.makedirs(temp_objs_path)

def convert_frame_to_obj(frame_number):
    obj_path = os.path.join(temp_objs_path, f"frame_{frame_number}.obj")
    dupframe()
    bpy.ops.wm.obj_export(
        filepath=obj_path,
        export_triangulated_mesh=True,
        export_selected_objects=True
    )
    bpy.ops.object.delete()
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

res = json.dumps(final_res)
with open(output_file, 'w') as file:
    file.write(res)
