import os
import xml.etree.ElementTree as ET

# Define folder to store XML files
# =============================================================================
# rfid_folder_path = ""
# =============================================================================
rfid_folder_path = os.path.join(os.path.expanduser("~"), "Documents", "amit", "RFID_Files")
os.makedirs(rfid_folder_path, exist_ok=True)

# Function to generate dummy XML file
def generate_xml(file_name, test_case):
    root = ET.Element("RFIDConfiguration")

    ET.SubElement(root, "TestCase").text = str(test_case)
    ET.SubElement(root, "TagID").text = "123456789"
    ET.SubElement(root, "Location").text = "Station_A"
    ET.SubElement(root, "Timestamp").text = "2025-03-09T12:00:00"

    tree = ET.ElementTree(root)
    file_path = os.path.join(rfid_folder_path, file_name)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {file_path}")

# Generate XML files Configuration1.xml to Configuration10.xml
for i in range(1, 11):
    generate_xml(f"Configuration{i}.xml", i)
