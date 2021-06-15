import unittest
from csv_json.csv_json_conv import *

def abs_path (file):
    path = os.path.abspath('tests')
    file_path = os.path.join(path, file)
    return file_path

class test_Csv_Json_Conv (unittest.TestCase):
       
    def test_json_2_csv (self):
        f1_list = list()
        f2_list = list()
        f1 = open (abs_path("file1_example.csv"), "r")
        json_to_csv(abs_path("file1.json"))
        f2 = open (abs_path("file1.csv"), "r")
        for rows1 in f1:
            f1_list.append(rows1)
        for rows2 in f2:
            f2_list.append(rows2)
        self.assertListEqual(f1_list, f2_list)

    def test_csv_2_json (self):
        f1_list = list()
        f2_list = list()
        f1 = open (abs_path("file2_example.json"), "r")
        csv_to_json(abs_path("file2.csv"))
        f2 = open (abs_path("file2.json"), "r")
        for rows1 in f1:
            f1_list.append(rows1)
        for rows2 in f2:
            f2_list.append(rows2)
        self.assertListEqual(f1_list, f2_list)


if __name__ == "__name__":
    unittest.main()