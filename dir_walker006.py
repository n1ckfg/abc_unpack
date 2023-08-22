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
    counter = 0
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if (file.endswith("tilt") and file != "sketch.tilt"):
                counter += 1
                print(str(counter))
                oldPath = os.path.join(root, file)
                newPath = os.path.join(root, "sketch.tilt")
                print(oldPath + ", " + newPath)
                runCmd(["mv", oldPath, newPath])


if __name__ == "__main__":
    main()




