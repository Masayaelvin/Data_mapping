from Data_handling import extract_json, extract_csv, extract_xml
import json
import csv


emp_file_name = "user_data_23_4.json"
vehicle_file_name = "user_data_23_4.csv"
employee_info_file = "user_data_23_4.xml"



employee_data = extract_json(emp_file_name)
vehicle_data = extract_csv(vehicle_file_name)
employee_info = extract_xml(employee_info_file)

def combine(file_name):
    """
    checks for inconsistencies in the data user data and vehicle data if there are any inconsistencies it will remove the data from the list
    and return the combined data
    """
    with open(file_name + ".json", 'w', newline='') as combine:
        json_data = []
        for employee in range(len(employee_data)):
            First_Name = employee_data[employee]['firstName']
            Second_Name = employee_data[employee]['lastName']
            age = employee_data[employee]['age']

            for info in range(len(employee_info)):
                if (First_Name != employee_info[info]['firstName']
                    and Second_Name != employee_info[info]['lastName']
                    and age != employee_info[info]['age']):
                    continue
                else:
                    employee_data[employee]['retired'] = employee_info[info]['retired']
                    employee_data[employee]['dependants'] = employee_info[info]['dependants']
                    employee_data[employee]['marital_Status'] = employee_info[info]['marital_status']
                    employee_data[employee]['salary'] = employee_info[info]['salary']
                    employee_data[employee]['pension'] = employee_info[info]['pension']
                    employee_data[employee]['company'] = employee_info[info]['company']
                    employee_data[employee]['commute_distance'] = employee_info[info]['commute_distance']
                    break

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
                    json_data.append(employee_data[employee])
                    break
        json.dump(json_data, combine, indent=4)
    return True 

combine("combined_data")

# c_data = extract_json("combined_data.json")

for data in employee_data:
    for key, values in data.items():
        if key == 'debt':
            print(data)

def check():
    count = 0
    for data in range(len(employee_data)):
       for info in range(len(employee_info)):
            if employee_data[data]["address_postcode"] == employee_info[info]['address_postcode']:
                count += 1
    print(count)   
        
check()