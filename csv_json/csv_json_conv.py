import json
import csv
import os


def json_to_csv(file_json, file_creating = True):

    with open (file_json, "r") as f:

        def flatten_json(data):
            out = {}

            def flatten(value, name =''):
                if type(value) is dict:
                    for item in value:
                        flatten(value[item], name + item + '_')
                elif type(value) is list:
                    i = 0
                    for item in value:                
                        flatten(item, name + str(i) + '_')
                        i += 1
                else: out[name[:-1]] = value
            
            flatten(data)
            return out
    
        data = json.load(f)
        data = flatten_json(data)
        headers = data.keys()
        
    with open (os.path.splitext(file_json)[0]+".csv", "w+", newline = '') as f:

        writer = csv.DictWriter (f, fieldnames= headers)
        writer.writeheader()
        writer.writerow(data)
        if (file_creating):
            return f
        else:
            f.close()
            file_name = os.path.splitext(file_json)[0]+".csv"
            path = os.path.abspath(file_name)
            os.remove(path)
            return f


def csv_to_json(file_csv, file_creating = True):

    with open (file_csv, "r", newline='') as f:

        data = []
        reader = csv.reader(f)
        for row in reader:
            arr_of_keys = row
            break
        reader = csv.reader(f)
        for row in reader:
            Dict_of_data = {}
            i = 0
            if (row == []):
                continue
            for key in arr_of_keys:
                while (i <= len(row)):
                    Dict_of_data[key] = row[i]
                    i += 1
                    break  
            data.append(Dict_of_data)

    with open (os.path.splitext(file_csv)[0]+".json", "w") as f:

        json.dump(data, f, indent = 4)
        if (file_creating):
            return f
        else:
            f.close()
            file_name = os.path.splitext(file_csv)[0]+".json"
            path = os.path.abspath(file_name)
            os.remove(path)
            return f