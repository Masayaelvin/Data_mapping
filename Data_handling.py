#!/usr/bin/python3
import csv
import json
import xml.etree.ElementTree as ET

# Function to extract data from CSV file
def extract_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Function to extract data from JSON file
def extract_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

# Function to extract data from XML file
def extract_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for element in root.findall('.//record'):  # Assuming 'record' is the XML element containing data
            record_data = {}  # Assuming each record is a dictionary
            for child in element:
                record_data[child.tag] = child.text
            data.append(record_data)

        return data
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return None

# Function to extract data from TXT file
def extract_txt(file_path):
    try:
        with open(file_path, 'r') as txt_file:
            data = [line.strip() for line in txt_file]
        return data
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return None

# Function to extract data from XML file
def extract_xml2(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for user_elem in root.findall('.//user'):  # Assuming 'user' is the XML element containing user data
            record_data = {}
            for attr_name, attr_value in user_elem.attrib.items():
                record_data[attr_name] = attr_value
            data.append(record_data)

        return data
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return None

