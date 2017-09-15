def fileOpen(filename):
    inStream = open(str(filename), "r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("occupations.csv")

#print fileInfo

def tidify(jobsList):
    counter = 0
    for string in jobsList:
        jobsList[counter] = string.strip("\r\n")
        counter += 1
    return jobsList

fileInfo = tidify(fileInfo)               

def listify(jobsList):
    counter = 0
    for string in jobsList:
        if string[0] == '"':
            jobsList[counter] = string.split(",")
            while len(jobsList[counter]) != 2:
                jobsList[counter][0] =  jobsList[counter][0] + "," + jobsList[counter][1]
                jobsList[counter].pop(1)
        else :
            jobsList[counter] = string.split(",")
        counter += 1
    return jobsList
    

fileInfo =  listify(fileInfo)
                
