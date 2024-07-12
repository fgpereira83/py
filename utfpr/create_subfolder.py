import os
import shutil

folderName= "testeFuncionamento"

if not os.path.exists(folderName):
    os.mkdir(folderName)
    for i in range(10):
        os.mkdir(folderName+"/{}".format(i))

if os.path.exists(folderName):
    shutil.rmtree(folderName)
else:
    print("pasta nao existe")

