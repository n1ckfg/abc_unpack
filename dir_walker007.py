import os
import sys
import pymeshlab as ml
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

def main():
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            workDirName = root.split("/")[1]
            oldPath = os.path.join(root, file)
            print("\n" + oldPath)
            if (file == "sketch.tilt"):
                newPath = os.path.join(root, workDirName + ".tilt")
                print(newPath)
                runCmd(["mv", oldPath, newPath])
            elif (file == "data.json"):
                newPath = os.path.join(root, workDirName + ".json")
                print(newPath)
                runCmd(["mv", oldPath, newPath])
            elif (file == "thumbnail.png"):
                newPath = os.path.join(root, workDirName + ".png")
                print(newPath)
                runCmd(["mv", oldPath, newPath])


if __name__ == "__main__":
    main()




