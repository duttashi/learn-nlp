# In this example the data is loaded from a remote loaction.
# Then using list comprehension data is converted to dictionary format
# first; assign remote data location path
filePath = 'C:/Users/Ashoo/PycharmProjects/pydata/data'
fileName = 'usagov_bitly_data2012-03-16-1331923249.txt'
# second: open the data file and ave to a temporary object
import json
import os

fileToRead = os.chdir(filePath)
if os.path.exists(filePath):
    obj1 = open(fileName).readline()
    print obj1
    records = [json.loads(line) for line in open(fileName)]  # list comprehension
    print records
else:
    print "File path does not exists"
