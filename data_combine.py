from Data_handling import extract_json, extract_csv, extract_xml
import json
import csv


emp_file_name = "user_data_23_4.json"
vehicle_file_name = "user_data_23_4.csv"
employee_info = "user_data_23_4.xml"



employee_data = extract_json(emp_file_name)
vehicle_data = extract_csv(vehicle_file_name)
employee_info = extract_xml(employee_info)
"""print( employee_data[0])
print(vehicle_data[0])
print(employee_info[0])"""

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
            for x in range(len(employee_info)):
                if (First_Name != employee_info[x]['firstName'] and Second_Name != employee_info[x]['lastName'] and age != employee_info[x]['age'] and 
                    employee_data[employee]['Sex'] != employee_info[x]['sex']):
                    continue
                else:
                    employee_data[employee]['Retired'] = employee_info[x]['retired']
                    employee_data[employee]['Dependants'] = employee_info[x]['dependants']
                    employee_data[employee]['Marital_Status'] = employee_info[x]['marital_status']
                    employee_data[employee]['Salary'] = employee_info[x]['salary']
                    employee_data[employee]['Pension'] = employee_info[x]['pension']
                    employee_data[employee]['Company'] = employee_info[x]['company']
                    employee_data[employee]['Commute_Distance'] = employee_info[x]['commute_distance']
                    employee_data[employee]['Address_Code'] = employee_info[x]['address_postcode']
            json_data.append(employee_data[employee])
        json.dump(json_data, combine, indent=4)
    return True 

combine("combined_data")

# c_data = extract_json("combined_data.json")

# for data in employee_data:
#     for key, values in data.items():
#         if key == 'debt':
#             print(data)

# def check():
#     count = 0
#     for data in range(len(employee_data)):
#        for info in range(len(employee_info)):
#             if employee_data[data]["address_postcode"] == employee_info[info]['address_postcode']:
#                 count += 1
#     print(count)   
        
# check()
