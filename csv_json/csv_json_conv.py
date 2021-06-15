import json
import csv
import os

def flatten_json (value, name = '', out = {}):
    if isinstance(value, dict):
        for item in value:
            flatten_json(value[item], name + item + '_')
    elif isinstance(value, list):
        i = 0
        for item in value:                
            flatten_json(item, name + str(i) + '_')
            i += 1
    else: out[name[:-1]] = value
    return out

def json_to_csv(file_json):

    with open (file_json, "r") as f:

        data = json.load(f)
        data = flatten_json(data)
        headers = data.keys()
        
    with open (os.path.splitext(file_json)[0]+".csv", "w+", newline = '') as f:

        writer = csv.DictWriter (f, fieldnames= headers)
        writer.writeheader()
        writer.writerow(data)
        return os.path.abspath(os.path.splitext(file_json)[0]+".csv")

def csv_to_json(file_csv):

    with open (file_csv, "r") as f:

        data = []
        reader = csv.reader(f)
        arr_of_keys = reader.__next__()
        for row in reader:
            dict_of_data = {}
            if not row:
                continue
            for i, key in enumerate(arr_of_keys):
                dict_of_data[key] = row[i]
            data.append(dict_of_data)

    with open (os.path.splitext(file_csv)[0]+".json", "w") as f:

        json.dump(data, f, indent = 4)
        return os.path.abspath(os.path.splitext(file_csv)[0]+".json")