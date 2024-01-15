from Data_handling import extract_json, extract_csv, extract_xml
import json
import csv


customer_details_file = "user_data_23_4.json"
customer_vehicle_file = "user_data_23_4.csv"
customer_info_file = "user_data_23_4.xml"


customer_details = extract_json(customer_details_file)
customer_vehicle = extract_csv(customer_vehicle_file)
customer_info = extract_xml(customer_info_file)

def combine(file_name):
    """
    checks for inconsistencies in the data user (json file) and vehicle data (csv) if there are any inconsistencies it will remove the data from the list
    and return the combined data
    """
    with open(file_name + ".json", 'w', newline='') as combine:
        json_data = []
        for i in range(len(customer_details)):
            First_Name = customer_details[i]['firstName']
            Second_Name = customer_details[i]['lastName']
            age = customer_details[i]['age']

            for x in range(len(customer_vehicle)):
                '''check whether the first name, second name and age are the same in both the files'''
                if (First_Name != customer_vehicle[x]['First Name']
                    and Second_Name != customer_vehicle[x]['Second Name']
                    and age != customer_vehicle[x]['Age (Years)']):
                    continue
                else:
                    customer_details[i]['Sex'] = customer_vehicle[x]['Sex']
                    customer_details[i]['Vehicle_Make']= customer_vehicle[x]['Vehicle Make']
                    customer_details[i]['Vehicle_Model'] = customer_vehicle[x]['Vehicle Model']
                    customer_details[i]['Vehicle_Year'] = customer_vehicle[x]['Vehicle Year']
                    customer_details[i]['Vehicle_Type'] = customer_vehicle[x]['Vehicle Type']
                    
                    """json_data.append(employee_data[employee])"""
            for y in range(len(customer_info)):
                if (First_Name != customer_info[y]['firstName'] and Second_Name != customer_info[y]['lastName'] and age != customer_info[y]['age'] and 
                    customer_details[i]['Sex'] != customer_info[y]['sex']):
                    continue
                else:
                    customer_details[i]['Retired'] = customer_info[y]['retired']
                    customer_details[i]['Dependants'] = customer_info[y]['dependants']
                    customer_details[i]['Marital_Status'] = customer_info[y]['marital_status']
                    customer_details[i]['Salary'] = customer_info[y]['salary']
                    customer_details[i]['Pension'] = customer_info[y]['pension']
                    customer_details[i]['Company'] = customer_info[y]['company']
                    customer_details[i]['Commute_Distance'] = customer_info[y]['commute_distance']
                    customer_details[i]['Address_Code'] = customer_info[y]['address_postcode']
            json_data.append(customer_details[i])
        json.dump(json_data, combine, indent=4)
    return True 

combine("combined_data")

