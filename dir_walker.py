import os
import sys
import pymeshlab as ml

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]

def changeExtension(_url, _newExt):
    returns = ""
    returnsPathArray = _url.split(".")
    for i in range(0, len(returnsPathArray)-1):
        returns += returnsPathArray[i]
    returns += _newExt
    return returns

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("obj")):
            inputUrl = os.path.join(inputPath, file)
            outputUrl = changeExtension(inputUrl, ".ply")
            ms = ml.MeshSet()
            ms.load_new_mesh(inputUrl)
            ms.save_current_mesh(outputUrl)        
