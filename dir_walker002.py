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

glbCounter = 0
dracoCounter = 0

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("glb")):
            glbCounter += 1
            print("Found " + str(glbCounter) + " gltf files.")

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("glb")):
            inputUrl = os.path.join(root, file)
            outputUrl = changeExtension(inputUrl, "_draco.glb")

            try:
                runCmd(["gltf-pipeline", "-i " + inputUrl, "-o " + outputUrl, "-d"])
                runCmd(["mv", outputUrl, "output/"])
                dracoCounter += 1
            except:
                pass
            
            print("Processed " + str(dracoCounter) + " / " + str(glbCounter)  + " gltf files.")

            #runCmd(["rm", inputUrl])

print("Finished.")