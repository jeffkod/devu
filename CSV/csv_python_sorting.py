'''
sorts from sprint.csv file to sprint_sorted.csv file on descending order of time

'''

import csv

#this is the tricky function in python to sort by keys. item[n] where n is the column number of list which require it to be sorted.
#  credits -  http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/ 

def getKey(item):
	return item[3]

csvFile = open("sprint.csv")  # opens the reader ofbject
csvReader = csv.reader(csvFile) # data object 
csvData = list(csvReader) #import the data into a list for further manipulation by python.

csvData_copy=csvData

csvData_copy.sort(key=getKey) #you need a callable fn as value of key and hence can't simply put key=3; try out and see the error
for row in csvData_copy:
	print(row)

csvOutFile2=open("sprint_sorted.csv",'w')
outputWriter = csv.writer(csvOutFile2)
outputWriter.writerows(csvData_copy)
csvOutFile2.close()


'''
more on sorting
You can also use the list.sort() method. It modifies the list in-place (and returns None to avoid confusion). 
Usually it’s less convenient than sorted() - but if you don’t need the original list, it’s slightly more efficient.

Another difference is that the list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.