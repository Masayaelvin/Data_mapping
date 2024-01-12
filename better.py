from Data_handling import extract_json, extract_csv, extract_xml
import csv
import json


emp_file_name = "user_data_23_4.json"
vehicle_file_name = "user_data_23_4.csv"
employee_info_file = "user_data_23_4.xml"



employee_data = extract_json(emp_file_name)
vehicle_data = extract_csv(vehicle_file_name)
employee_info = extract_xml(employee_info_file)

def combine(file_name):
    with open(file_name + ".json", 'w', newline='') as combine:
        json_data = []

        # Create dictionaries for faster lookups
        info_dict = {tuple((info['firstName'], info['lastName'], info['age'])): info for info in employee_info}
        vehicle_dict = {tuple((vehicle['First Name'], vehicle['Second Name'], vehicle['Age (Years)'])): vehicle for vehicle in vehicle_data}

        for employee in employee_data:
            key = tuple((employee['firstName'], employee['lastName'], employee['age']))

            # Check if there is corresponding info data
            if key in info_dict:
                info = info_dict[key]
                employee.update({
                    'retired': info['retired'],
                    'dependants': info['dependants'],
                    'marital_Status': info['marital_status'],
                    'salary': info['salary'],
                    'pension': info['pension'],
                    'company': info['company'],
                    'commute_distance': info['commute_distance']
                })

            # Check if there is corresponding vehicle data
            if key in vehicle_dict:
                vehicle = vehicle_dict[key]
                employee.update({
                    'Sex': vehicle['Sex'],
                    'Vehicle Make': vehicle['Vehicle Make'],
                    'Vehicle Model': vehicle['Vehicle Model'],
                    'Vehicle Year': vehicle['Vehicle Year'],
                    'Vehicle Type': vehicle['Vehicle Type']
                })
                json_data.append(employee)

        json.dump(json_data, combine, indent=4)

    return True

combine('efficient')

 for cust in data:
                if 'debt' in cust:
                    debt_info = cust['debt']
                    if isinstance(debt_info, dict):
                        data['debt_amount'] = debt_info.get('amount', None)
                        data['debt_period_in_years'] = debt_info.get('period_in_years', None)
                    else:
                        data['debt_amount'] = debt_info
            del cust['debt']