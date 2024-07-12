import os

folderName= "exemploPasta"

if not os.path.exists(folderName):
    os.mkdir(folderName)

if os.path.exists(folderName):
    os.rmdir(folderName)
else:
    print("pasta nao existe")

