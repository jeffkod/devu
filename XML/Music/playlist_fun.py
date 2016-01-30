
'''
xmlns='http://www.jeff.com/mynamespace'  - for namespace
xml.etree.ElementTree
https://www.youtube.com/watch?v=GxY0VJXACsk
http://www.diveintopython3.net/xml.html

'''
#from xml.etree import ElementTree
import xml.etree.ElementTree as etree  #if you want to have options to use different modules for your parser

def traverse_the_tree(root):
	for child in root:
		for sub_child in child :
			print(sub_child.tag + "  : " + str(sub_child.text)) #note the diff b/w attrib and text

	for child in root:
		for sub_child in child :
			for sub_sub_child in sub_child:
				for sub_sub_sub_child in sub_sub_child:
					print(sub_sub_sub_child.tag)
					print(sub_sub_sub_child.text)

def traverse_the_tree_and_write_to_text(root):
	out_file = open("xml_to_text.txt","wt")
	for child in root:
		for sub_child in child :
			#print(sub_child.tag + "  : " + str(sub_child.text)) #note the diff b/w attrib and text
			out_file.write(sub_child.tag + "  : " + str(sub_child.text) +"\n")
	# for child in root:
	# 	for sub_child in child :
	# 		for sub_sub_child in sub_child:
	# 			for sub_sub_sub_child in sub_sub_child:
	# 				print(sub_sub_sub_child.tag)
	# 				print(sub_sub_sub_child.text)
	out_file.close()

#tree = ElementTree.parse('examples/reed_college_courses.xml') #the file is under folder 'exmamples'
#tree = ElementTree.parse('Classical_Rock.xml')
tree = etree.parse('examples/reed_college_courses.xml')
#tree = etree.parse('Classical_Rock.xml'')

root = tree.getroot()
print(root)   # gives the root object and it's memmory location
print(root.tag)  # gives the tag of the xml root in English
print(len(root)) #no.of child elements for the root. only 1 level deep. doesn't show the children of the children
print(root.attrib)  # show the attribute of the root. whatever you define as x=y inside it is attribute 


traverse_the_tree(root)
traverse_the_tree_and_write_to_text(root)



