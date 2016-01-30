
'''
xmlns='http://www.jeff.com/mynamespace'  - for namespace
xmlns='http://www.w3.org/2005/Atom'
xml.etree.ElementTree
https://www.youtube.com/watch?v=GxY0VJXACsk
http://www.diveintopython3.net/xml.html

'''
#from xml.etree import ElementTree
import xml.etree.ElementTree as etree  #if you want to have options to use different modules for your parser

#tree = ElementTree.parse('examples/reed_college_courses.xml') #the file is under folder 'exmamples'
#tree = ElementTree.parse('Classical_Rock.xml')
#tree = etree.parse('examples/reed_college_courses.xml')
tree = etree.parse('feed.xml')

root = tree.getroot()
print(root)   # gives the root object and it's memmory location
print(root.tag)  # gives the tag of the xml root in English
print(len(root)) #no.of child elements for the root. only 1 level deep. doesn't show the children of the children
print(root.attrib)  # show the attribute of the root. whatever you define as x=y inside it is attribute 

def traverse_the_tree(root):
	for child in root:
		for sub_child in child :
			print(sub_child.tag + "  : " + str(sub_child.text)) #note the diff b/w attrib and text


def traverse_the_tree_and_write_to_text(root):
	out_file = open("xml_to_text.txt","wt")
	for child in root:
		for sub_child in child :
			#print(sub_child.tag + "  : " + str(sub_child.text)) #note the diff b/w attrib and text
			out_file.write(sub_child.tag + "  : " + str(sub_child.text) +"\n")
	out_file.close()


def findall_example_feed(root):
	feed_list = root.findall('entry')  # only searches the immediate child
	title_list =[]
	author_list = []
	for feed_entry in feed_list:
		title = feed_entry.find('title').text # don't forget the text part
		title_list.append(title)
		#print(title)  # --> same is accomplished in below line using the list 
	
	print("\n".join(str(i) for i in title_list))  # The power of generators!

#traverse_the_tree(root)
#traverse_the_tree_and_write_to_text(root)
findall_example_feed(root)






