def fileOpen(filename):
    inStream = open(str(filename), "r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("occupations.csv")

#print fileInfo

def tidify(jobsList):
    counter = 0;
    for string in jobsList:
        jobsList[counter] = string.strip("\r\n")
        counter += 1
    return jobsList

print tidify(fileInfo)               
