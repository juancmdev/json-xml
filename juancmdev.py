import os
import xml.etree.ElementTree as xml
import json

data = {
    "name": "Juan",
    "age": 45,
    "birth_date": "05-02-1979",
    "programing_languages": ['Python', 'Kotlin', 'Javascripr'],
}

xml_file = "juancmdev.xml"
json_file = "juancmdev.json"

#XML

def create_xml():
    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
        
    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

#Leer el XML
with open(xml_file, "r") as xml_data:
    print(xml_data.read())

#Borrar XML
os.remove(xml_file)


#JSON
    
def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

#Borrar JSON
os.remove(json_file)
    
"""
EXTRA
"""
create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

#leer XML
with open(xml_file, "r") as xml_data:
    
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programing_languages = []
    for item in root.find("programing_languages"):
        programing_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programing_languages)
    print(xml_class.__dict__)

# leer JSON
with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    print(type(json_dict))
    json_class = Data(json_dict["name"], json_dict["age"], json_dict["birth_date"], json_dict["birth_date"])
    print(json_class.__dict__)