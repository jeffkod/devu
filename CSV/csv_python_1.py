import csv


#writing to new file
csvOutFile2=open("test2.csv",'w')   #handles file i/o; can be opened in w or a mode
outputWriter = csv.writer(csvOutFile2)  #
outputWriter.writerow(['name','skills','interests'])  #--First row is the 'headers' or definition of columns/arrtributes
outputWriter.writerow(['jeff','nwtworking','python']) # 2nd row onwards the data
outputWriter.writerow(['jeff2','football','basketball'])
csvOutFile2.close()


#Reading and displaying
csvInFile = open("sprint.csv")  # opens the reader ofbject
csvReader = csv.reader(csvInFile) # data object 
csvData = list(csvReader) #import the data into a list for further manipulation by python.

print(csvReader.line_num) # number of rows  directly from the reader object




#print all contents of file using list 
for row in csvData:
	print(row)

l=len(csvData)
print(csvData[1]) #print random row 
print(csvData[1][3])  #print a value
csvFile.close()
