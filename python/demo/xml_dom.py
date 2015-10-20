# Filename: xml_dom.py

from xml.dom import minidom 
import traceback 

try: 
    f = open("./test/xmlstuff.xml", "w") 
    try: 
        doc = minidom.Document() 
        rootNode = doc.createElement("root") 
        doc.appendChild(rootNode) 
        bookNode = doc.createElement("book") 
        bookNode.setAttribute("isbn", "34909023") 
        rootNode.appendChild(bookNode) 
        authorNode = doc.createElement("author") 
        bookNode.appendChild(authorNode) 
        authorTextNode = doc.createTextNode("dikatour") 
        authorNode.appendChild(authorTextNode) 
        doc.writexml(f, "\t", "\t", "\n", "utf-8") 
    except: 
        trackback.print_exc() 
    finally: 
        f.close() 
except IOException: 
    print("open file failed")
