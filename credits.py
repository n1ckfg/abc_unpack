import os
import sys
import subprocess
import json

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]

appendWorkIds = True

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

fullNameList = []
uniqueNameList = []
uniqueNameListWithIds = []

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if (file.endswith("json")):
            f = open(os.path.join(root, file))
            data = json.load(f)
            
            if (appendWorkIds == True):
                newName = data["authorName"]
            else:
                newName = data["authorName"] + "\r"
            

            fullNameList.append(newName)
            
            addToUniqueList = True

            for name in uniqueNameList:
                if (newName == name):
                    addToUniqueList = False
                    break

            if (addToUniqueList == True):
                if (data["license"].lower() == "creative_commons_by"):
                    uniqueNameList.append(newName)
                    uniqueNameListWithIds.append(newName)
                else:
                    print("Error: Wrong license info!")

print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
uniqueLen = str(len(uniqueNameList))
uniqueIdLen = str(len(uniqueNameListWithIds))
fullLen = str(len(fullNameList))
print("Found " + uniqueLen + " (" + uniqueIdLen + ") " + "unique names out of " + fullLen + " total names.")

if (appendWorkIds == True):
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if (file.endswith("json")):
                f = open(os.path.join(root, file))
                data = json.load(f)
                newName = data["authorName"]
                
                for i in range(0, len(uniqueNameList)):
                    if (newName == uniqueNameList[i]):
                        uniqueNameListWithIds[i] += ", " + file.split(".")[0]

    for i in range(0, len(uniqueNameListWithIds)):
        uniqueNameListWithIds[i] += "\r"

    f = open("tiltset_credits_unique_" + uniqueIdLen + ".csv", "w")
    f.writelines(uniqueNameListWithIds)
    f.close()

for i in range(0, len(fullNameList)):
    fullNameList[i] += "\r"

f = open("tiltset_credits_full_" + fullLen + ".txt", "w")
f.writelines(fullNameList)
f.close()

for i in range(0, len(uniqueNameList)):
    uniqueNameList[i] += "\r"

f = open("tiltset_credits_unique_" + uniqueLen + ".txt", "w")
f.writelines(uniqueNameList)
f.close()
