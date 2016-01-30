# reed_college_courses
# https://www.youtube.com/watch?v=GxY0VJXACsk
# http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree




import os
from xml.etree import ElementTree

file_name = 'reed_college_courses.xml'
full_file = os.path.abspath(os.path.join('data',file_name))
#print(full_file)

dom = ElementTree.parse(file_name)
#print(dom)

courses = dom.findall('course')

for c in courses:
	#print(c.text)
	title = c.find('title').text
	num = c.find('crse').text
	days = c.find('days').text

	print("*{} [{}] {} ".format(
		num, days, title
		))


