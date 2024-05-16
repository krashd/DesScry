import hashlib
import xml.etree.cElementTree as hashTree
import xml.etree.cElementTree as readTree
from zipfile import ZipFile
from datetime import datetime

def hasher(input_folder, input_files):

    hashTab = hashTree.Element('HASH')                              # Hash file header
    print('Generating sha256 hash for files')

    with open(input_folder + input_files[0], 'rb') as file_obj:     # Grab the hash for the Designed XML
        file_contents = file_obj.read()

        sha256_hash = hashlib.sha256(file_contents).hexdigest()     # Generate hash to sha256

        asDesigned = hashTree.SubElement(hashTab, 'AsDesigned')
        asDesigned.text = sha256_hash
        print('Site_Config_As_Designed: ' + sha256_hash)

    with open(input_folder + input_files[1], 'rb') as file_obj:     # Grab the hash for the Installed XML
        file_contents = file_obj.read()

        sha256_hash = hashlib.sha256(file_contents).hexdigest()     # Generate hash to sha256

        asInstalled = hashTree.SubElement(hashTab, 'AsInstalled')
        asInstalled.text = sha256_hash
        print('Site_Config_As_Installed: ' + sha256_hash)

    hashTree.indent(hashTab)                                        # Indent the Hash XML Tree
    hashTree.ElementTree(hashTab).write(input_folder + input_files[2], encoding='utf-8', xml_declaration=True)      # Write the Hash XML file.



def zipper(input_folder, zip_file, input_files):

    print('archiving xml files for installation')

    with ZipFile(input_folder + zip_file, 'w') as zip:
        for file in input_files:
            zip.write(input_folder + file, file)

    print('Files archived to ' + input_folder + zip_file)



def main():
    input_folder = 'C:/opt/'
    input_files = ['Site_Config_As_Designed.xml', 'Site_Config_As_Installed.xml', 'Hash.xml']

    tree = readTree.parse(input_folder + input_files[0])
    root = tree.getroot()

    drawingNumber = root.find('./drawingInformation/drawingNumber').text
    revisionNumber = root.find('./drawingInformation/revisionNumber').text

    completeDrawingNumber = drawingNumber + '-' + revisionNumber

    zip_file = completeDrawingNumber + ' - (' + datetime.today().strftime('%Y-%m-%d') + ') - DCV Edit.zip'

    hasher(input_folder, input_files)
    zipper(input_folder, zip_file, input_files)


if __name__ == "__main__":
    main()