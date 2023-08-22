import os
import sys
import pymeshlab as ml
import subprocess
import json

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]
destPath = "temp"
nameList = [ "GLTF", "FBX", "GLTF2", "OBJ" ]

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

def moveDir(name, root, counter):
    path1 = os.path.join(root, name)
    path2 = os.path.join(destPath, name + str(counter))
    runCmd(["mv", path1, path2])
    print(path1 + ", " + path2)
    counter += 1
    return counter

def main():
    counter = 0
    for root, dirs, files in os.walk(inputPath):
        for name in nameList:
            if name in dirs:
                counter = moveDir(name, root, counter)

if __name__ == "__main__":
    main()




