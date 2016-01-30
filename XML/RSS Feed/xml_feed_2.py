
'''
xmlns='http://www.jeff.com/mynamespace'  - for namespace
xmlns='http://www.w3.org/2005/Atom'
xml.etree.ElementTree
https://www.youtube.com/watch?v=GxY0VJXACsk
http://www.diveintopython3.net/xml.html
http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree

markup - machine and human readable, exporting and importing data b/w different softwares!
tree,root,elements
tags,attribute,text

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


def  dfs_iter_feed(tree):     # note that this takes the entire tree and not the root. no need for nested for loops
	for elem in tree.iter():
		print(elem.tag,elem.attrib,elem.text)

def dfs_iter_specific_feed(tree):
	for elem in tree.iter(tag='name'):
		print(elem.tag,elem.attrib, elem.text)

def xpath_iter_feed(tree):
	for elem in tree.iterfind("entry/author/name"):
		print(elem.tag,elem.attrib, elem.text)

def xpath_child_iter_feed(tree):
	for elem in tree.iterfind("entry/author"):
		for child_elem in elem.iter():    # the element tree could also be used to iterate. Very useful indeed !
			print(child_elem.tag,child_elem.attrib,child_elem.text)

def xpath_child_iter_specific_feed(tree):
	for elem in tree.iterfind('author[@name="Mark"]'):
		print(elem.tag,elem.attrib, elem.text)
		# for child_elem in elem.iter():    # the element tree could also be used to iterate. Very useful indeed !
		# 	print(child_elem.tag,child_elem.attrib,child_elem.text)
	
def xml_copying_del(tree2):
	root=tree2.getroot()
	print(len(root))
	del root[7]
	#traverse_the_tree(root)
	dfs_iter_feed(tree2)  # note that even though we did the action on root, it's reflecting in the tree
	tree2.write("updated_feed.xml")

def xml_new_file():
	top = etree.Element('class')
	child1 = etree.SubElement(top,'student')
	child1.attrib ={'id':'1001'}
	sub_child1= etree.SubElement(child1,'name')
	sub_child1.text ="Jeffin"

	child2 = etree.SubElement(top,'student')
	child2.attrib ={'id':'1002'}
	sub_child2= etree.SubElement(child2,'name')
	sub_child2.text ="Pradeep"

	tree = etree.ElementTree(top)
	tree.write("DevU.xml")



#traverse_the_tree(root)
#traverse_the_tree_and_write_to_text(root)
#findall_example_feed(root)

#dfs_iter_feed(tree)
#dfs_iter_specific_feed(tree)
# xpath_iter_feed(tree)
# xpath_child_iter_feed(tree)
#xpath_child_iter_specific_feed(tree)
#xml_copying_del(tree)

#xml_new_file()

