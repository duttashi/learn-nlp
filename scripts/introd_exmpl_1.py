# In this example the data is loaded from a remote loaction.
# Then using list comprehension data is converted to dictionary format
# first; assign remote data location path
path='/data/usagov_bitly_data2012-03-16-1331923249.txt'
# second: open the data file and ave to a temporary object

obj1= open(path).readline()
print obj1
