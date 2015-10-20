# Filename: xml_element_tree.py

from xml.etree import ElementTree

def print_node(node):
    '''打印结点基本信息'''
    print("==============================")
    print("node.attrib:%s" % node.attrib)
    if node.attrib.has_key("age") > 0:
        print("node.attrib['age']:%s" % node.attrib['age'])
    print("node.tag:%s" % node.tag)
    print("node.text:%s" % node.text)

def read_xml(text):
    '''读xml文件'''
    # 加载xml文件 (2种方法，一是加载指定字符串，二是加载指定文件)
    # root = ElementTree.parse(r"e:/my_pro/python/study/test_xml.xml")
    root = ElementTree.fromstring(text)

    # 获取 element 的方法
    # 1.通过 getiterator
    lst_node = root.getiterator("person")
    for node in lst_node:
        print_node(node)
    # 2.通过 getchildren
    lst_node_child = lst_node[0].getchildren()[0]
    print_node(lst_node_child)
    # 3.find 方法
    node_find = root.find('person')
    print_node(node_find)
    # 4.findall 方法
    node_findall = root.findall("person/name")[1]
    print_node(node_findall)

if __name__ == '__main__':
    read_xml(open("./test/test_xml.xml").read())
