import os
from pyunpack import Archive
import subprocess
import sys

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

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(inputPath):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        runCmd(["mv", "*.obj", ".."])
        print(len(path) * '---', file)

# Archive('data.7z').extractall("<output path>")