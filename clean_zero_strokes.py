import os
import sys
import subprocess
import json
import latk

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
    numTiltFiles = 0

    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if (file.endswith("tilt")):
                numTiltFiles += 1

    print("Found " + str(numTiltFiles) + ".")

    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if (file.endswith("tilt")):
                counter += 1
                print("\nEvaluating " + str(counter) + " / " + str(numTiltFiles) + " ...")
                oldPath = os.path.join(root, file)
                print(oldPath)          
                strokeCount = 0
                la = latk.Latk()

                try:
                    la.readTiltBrush(oldPath)
                    strokeCount = len(la.layers[0].frames[0].strokes)
                except:
                    pass

                print("Found " + str(strokeCount) + " strokes.")

                if (strokeCount < 1):
                    newPath = os.path.join("reject", file)
                    #print("Moving to " + newPath)
                    runCmd(["mv", oldPath, newPath])

if __name__ == "__main__":
    main()




