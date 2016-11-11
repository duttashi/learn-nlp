# In this example the data is loaded from a remote loaction.
# Then using list comprehension data is converted to dictionary format
# first; assign remote data location path
# Script Objective: To read the data file and count the number of time zones
filePath = 'C:/Users/Ashoo/PycharmProjects/pydata/data'
fileName = 'usagov_bitly_data2012-03-16-1331923249.txt'
# second: open the data file and ave to a temporary object
import json
import os
from collections import defaultdict as dd
fileToRead = os.chdir(filePath)
if os.path.exists(filePath):
    obj1 = open(fileName).readline()
    print obj1
    records = [json.loads(line) for line in open(fileName)]  # list comprehension
    # Counting time zones
    time_zones = [rec['tz'] for rec in records if
                  'tz' in rec]  # will check for attribute tz in recods, if found will save to object time_zones
    print time_zones[:10]


    def get_counts(sequence):
        counts = dd(int)  # values will initialize to zero
        for x in sequence:
            counts[x] += 1
        return counts


    counts = get_counts(time_zones)
    print "\nTotal number of Time Zones: ", counts


else:
    print "File path does not exists"
