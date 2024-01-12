from Data_handling import extract_json, extract_csv, extract_xml
import json
import csv


emp_file_name = "user_data_23_4.json"
vehicle_file_name = "user_data_23_4.csv"
xml_data = "user_data_23_4.xml"



employee_data = extract_json(emp_file_name)
vehicle_data = extract_csv(vehicle_file_name)
employee_info = extract_xml(xml_data)
print( employee_data[0])
print(vehicle_data[0])
print(employee_info[0])

"""for data in range(min(10, len(employee_info))):
    print(employee_info[data])"""

def combine(file_name):
    """
    checks for inconsistencies in the data user (json file) and vehicle data (csv) if there are any inconsistencies it will remove the data from the list
    and return the combined data
    """
    with open(file_name + ".json", 'w', newline='') as combine:
        json_data = []
        for employee in range(len(employee_data)):
            First_Name = employee_data[employee]['firstName']
            Second_Name = employee_data[employee]['lastName']
            age = employee_data[employee]['age']

            for vehicle in range(len(vehicle_data)):
                '''check whether the first name, second name and age are the same in both the files'''
                if (First_Name != vehicle_data[vehicle]['First Name']
                    and Second_Name != vehicle_data[vehicle]['Second Name']
                    and age != vehicle_data[vehicle]['Age (Years)']):
                    continue
                else:
                    employee_data[employee]['Sex'] = vehicle_data[vehicle]['Sex']
                    employee_data[employee]['Vehicle Make']= vehicle_data[vehicle]['Vehicle Make']
                    employee_data[employee]['Vehicle Model'] = vehicle_data[vehicle]['Vehicle Model']
                    employee_data[employee]['Vehicle Year'] = vehicle_data[vehicle]['Vehicle Year']
                    employee_data[employee]['Vehicle Type'] = vehicle_data[vehicle]['Vehicle Type']
                    """json_data.append(employee_data[employee])"""
            for x in range(len(xml_data)):
                if (First_Name != xml_data[x]['firstName'] and Second_Name != xml_data[x]['lastName'] and age != xml_data[x]['age'] and 
                    employee_data[employee]['Sex'] != xml_data[x]['sex']):
                    continue
                else:
                    employee_data[employee]['Retired'] = xml_data[x]['retired']
                    employee_data[employee]['Dependants'] = xml_data[x]['dependants']
                    employee_data[employee]['Marital_Status'] = xml_data[x]['marital_status']
                    employee_data[employee]['Salary'] = xml_data[x]['salary']
                    employee_data[employee]['Pension'] = xml_data[x]['pension']
                    employee_data[employee]['Company'] = xml_data[x]['company']
                    employee_data[employee]['Commute_Distance'] = xml_data[x]['commute_distance']
                    employee_data[employee]['Address_Code'] = xml_data[x]['address_code']
                    json_data.append(employee_data[employee])
        json.dump(json_data, combine)
    return True 

combine("combined_data")

def check_gender():
    ok = 0
    for data in vehicle_data:
        if data['Sex'] not in ['Male','Female']:
             print(data)
        else:
             ok += 1
    print(ok)
