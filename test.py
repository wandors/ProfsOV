import xml.etree.ElementTree as ET

path = "./document.xml"

def par(path_xml):
    erot = ET.parse(path_xml)
    impo_ses = erot.getroot()
    print(impo_ses)


par(path_xml=path)
