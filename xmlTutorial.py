import xml.etree.cElementTree as ET

# Create an XML tree

siteDataString = """<?xml version="1.0"?>
<siteData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="SiteLayout.xsd">
</siteData>"""

siteData = ET.fromstring(siteDataString)

configType = ET.SubElement(siteData, 'configType')
configType.text = "as_installed"

drawingInformation = ET.SubElement(siteData, "drawingInformation")

authorName = ET.SubElement(drawingInformation, "authorName")
authorName.text = "Dan Brown"

authorEmail = ET.SubElement(drawingInformation, "authorEmail")
authorEmail.text = "dan.brown@yunextraffic.com"

drawingNumber = ET.SubElement(drawingInformation, "drawingNumber")
drawingNumber.text = "871252221-YU-00-XX-DR-Y-0001 C5"

nodeList = ET.SubElement(siteData, 'nodeList')

node = ET.SubElement(nodeList, 'node')

nodeID = ET.SubElement(node, "id")
nodeID.text = "1_E_1"

signalType = ET.SubElement(node, "signalType")
signalType.text = "HD80F"

nodeType = ET.SubElement(node, "nodeType")
nodeType.text = "pdu"

serialNumber = ET.SubElement(node, "serialNumber")

poleNumber = ET.SubElement(node, "poleNumber")
poleNumber.text = "1"

nodeText = ET.SubElement(node, "text")
nodeText.text = "PB"


nodeSpecificData = ET.SubElement(node, "nodeSpecificData")

waitPduData = ET.SubElement(nodeSpecificData, "waitPduData")

orientation = ET.SubElement(waitPduData, "orientation")
orientation.text = "0"

phase = ET.SubElement(waitPduData, "phase")
phase.text = "E"

audible = ET.SubElement(waitPduData, "audible")
audible.text = "not_fitted"

tactile = ET.SubElement(waitPduData, "tactile")
tactile.text = "not_fitted"

pushButtonInputName = ET.SubElement(waitPduData, "pushButtonInputName")
pushButtonInputName.text = "EPBU1"

#rank = ET.SubElement(country, 'rank')

#rank.text = '1'



# Indent the XML element

ET.indent(siteData)



# Write the tree to file

tree = ET.ElementTree(siteData)

tree.write('Site_Config_As_Installed.xml', encoding='utf-8', xml_declaration=True)