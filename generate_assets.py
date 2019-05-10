import os
onlyfiles = os.listdir('/Users/admin/desktop/iOS')
formattedFiles = []
orginalNames = []
for file in onlyfiles:
    if "@" not in file:
        arr = list(file.lower())
        for idx, val in enumerate(arr):
            if val == " " or val == "-":
                arr[idx] = "_"
        newname = "".join(arr)
        newname = newname[:-4]
        formattedFiles.append(newname)
        orginalNames.append(file[:-4])

f = open("images.js", "w+")
for idx, name in enumerate(formattedFiles):
    f.write( name + ": require('./images/" + orginalNames[idx] + ".png'),\n")

f.close() 
