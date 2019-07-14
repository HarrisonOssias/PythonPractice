import json

def getJSON(filePath):
    with open(filePath, 'r') as fp:
        return json.load(fp)

data_A = getJSON('/Users/stanleyossias/Desktop/Python Practice/PythonPractice/Difference_Sensor _Data/humidity.json').get('a_sensor',[])
data_B = getJSON('/Users/stanleyossias/Desktop/Python Practice/PythonPractice/Difference_Sensor _Data/humidity.json').get('b_sensor',[])

def findDiff (sense_A, sense_B):
    legnth = len(sense_A)
    diffData = []
    for i in range (legnth):
        diff = sense_A[i] - sense_B[i]
        diffData.append(abs(diff))
    print (diffData)

findDiff(data_A, data_B)