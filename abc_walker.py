import os
from pyunpack import Archive

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        os.system("mv *.obj ..")
        #print(len(path) * '---', file)

# Archive('data.7z').extractall("<output path>")