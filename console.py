import os # For use with directories
import pandas as pd # Main statistic and data tabulation capabilities

def openData():
    try:
        os.chdir('data')
        fileValues = pd.read_csv('test_data.csv')
        return fileValues
    except FileNotFoundError:
      exit()

flightData = openData()

#print(flightData.head())
#print(flightData['SEATS'])
#print(flightData.iloc[0:4, 3])
 # [row] [column]
#print(flightData.iloc[0, 18])

rows = len(flightData.index)

#print(flightData)




#print(len(destList))
#print(destList[0:3])
