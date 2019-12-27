import docx
import os
import dir
file = docx.Document("code.docx")
pathList = os.listdir(dir.code_path)
i=1;
for fileName in pathList :
    p = dir.code_path+"\\"+fileName
    print(p)
    print(os.path.isfile(p))
    isFile = os.path.isfile(p)
    i = i + 1
    print(i)
    if i == 7:
        break
    if isFile == False :
        moduleCodePathList =  os.listdir(p)
        for  moduleCodeFileName in moduleCodePathList:


            codeFileName = p+"\\"+moduleCodeFileName
            codeF = open(codeFileName,"r",encoding="utf-8")
            for line in codeF:
                # print(line)
                file.add_paragraph(line)
            codeF.close()





file.save("code.docx")



