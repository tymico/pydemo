# Filename: test_element_tree.xml

from xml.etree import ElementTree as ET

#要找出所有人的年龄
per = ET.parse('./test/test_xml.xml')
p = per.findall('person')
for x in p:
    print(x.attrib)
print()

for oneper in p:  #找出person节点
    for child in oneper.getchildren(): #找出person节点的子节点
        print(child.tag,':',child.text)
    print('age:',oneper.get('age'))
    print('############')
