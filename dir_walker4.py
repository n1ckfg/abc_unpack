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
        if "TILT" in dirs:           
            with open(os.path.join(root, "data.json")) as data_file:    
                data = json.load(data_file)

                tiltFile = data["formats"][1]["root"]["relativePath"]
                if (tiltFile.endswith("tilt") == False):
                    tiltFile = data["formats"][0]["root"]["relativePath"]
                oldPath = os.path.join(root, "TILT")
                oldPath2 = os.path.join(oldPath, tiltFile)
                newPath = os.path.join(root, tiltFile)
                print(oldPath + ", " + newPath)
                runCmd(["mv", oldPath2, newPath])


if __name__ == "__main__":
    main()




