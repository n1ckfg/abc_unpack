import os
import sys
import trimesh as tm
import subprocess
import json

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]

def runCmd(cmd):
    returns = ""
    try:
        returns = subprocess.check_output(cmd, text=True)
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

objCounter = 0
glbCounter = 0

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("obj")):
            objCounter += 1
            print("Found " + str(objCounter) + " obj files.")

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("obj")):
            inputUrl = os.path.join(root, file)
            outputUrl = changeExtension(inputUrl, ".glb")

            try:
                mesh = tm.load_mesh(inputUrl)
                mesh.export(outputUrl)  
                runCmd(["mv", outputUrl, "output/"])
                glbCounter += 1
            except:
                pass
            
            print("Processed " + str(glbCounter) + " / " + str(objCounter)  + " gltf files.")

            runCmd(["rm", inputUrl])

print("Finished.")