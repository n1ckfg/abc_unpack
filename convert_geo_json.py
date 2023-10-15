import os
import sys
import subprocess
import json
import bpy

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]

def runCmd(cmd, shell=False):
    returns = ""
    try:
        returns = subprocess.check_output(cmd, text=True, shell=shell)
    except subprocess.CalledProcessError as e:
        returns = f"Command failed with return code {e.returncode}"
    print(returns)
    return returns  

#runCmd(["command", "arg1", "arg2"])

def changeExtension(_url, _newExt):
    returns = ""
    returnsPathArray = _url.split(".")
    for i in range(0, len(returnsPathArray)-1):
        returns += returnsPathArray[i]
    returns += _newExt
    return returns

jsonCounter = 0
dracoCounter = 0

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith(".json.zip")):
            jsonCounter += 1
            print("Found " + str(jsonCounter) + " zipped geometry json files.")

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("zip")):
            inputUrl = os.path.join(root, file)

            runCmd(["unzip", inputUrl, "-d", "output"])
            
            outputUrl = inputUrl.replace("input", "output").replace(".zip", "")
            #outputUrl = os.path.join(os.getcwd(), outputUrl)

            runCmd(["python2", "geometry_json_to_obj.py", outputUrl])
            runCmd(["rm", outputUrl])

            outputUrl2 = changeExtension(outputUrl, ".obj")
            outputUrl3 = changeExtension(outputUrl, ".glb")
            outputUrl4 = changeExtension(outputUrl, "_draco.glb")
            
            bpy.ops.wm.obj_import(filepath=outputUrl2)
            bpy.ops.export_scene.gltf(filepath=outputUrl3, use_selection=True, export_draco_mesh_compression_enable=False)
            #bpy.ops.export_scene.gltf(filepath=outputUrl4, use_selection=True, export_draco_mesh_compression_enable=True)
            bpy.ops.wm.read_homefile(app_template="") # reset the Blender scene to default, saves undo memory vs. delete
            runCmd("gltf-pipeline -i " + outputUrl3 + " -o " + outputUrl4 + " -d", True)
            runCmd(["rm", outputUrl2])

            dracoCounter += 1
            
            print("Processed " + str(dracoCounter) + " / " + str(jsonCounter)  + " json files.")

print("Finished.")
