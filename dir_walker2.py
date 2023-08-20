import os
import sys
import pymeshlab as ml
import subprocess
import json

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]
destPath = argv[1]

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

tiltdirs = []

for root, dirs, files in os.walk(inputPath):
    '''
    for file in files:
        if (file.endswith("obj")):
            inputUrl = os.path.join(inputPath, file)
            outputUrl = changeExtension(inputUrl, ".ply")
            ms = ml.MeshSet()
            ms.load_new_mesh(inputUrl)
            ms.save_current_mesh(outputUrl)    
    '''
    if "TILT" in dirs:
        with open(os.path.combine(root, "data.json")) as data_file:    
            data = json.load(data_file)
            print(data["license"])
        #runCmd(["mv", root, destPath])

