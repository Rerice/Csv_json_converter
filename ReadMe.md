# Csv-json file converter 

#### Csv-json converter converts csv files to json files. The converter can convert standard csv files with headers and standart json files.
#### Functions of this package can return the converted file as a variable and create the converted file in the project directory if needed.
***
## How to use it? 

##### * First of all you must import this package like:
```python
from csv_json.csv_json_conv import *
```
##### * If you want to convert csv to json you must use:
```python
csv_to_json(file_csv, file_creating=)
```
Instead file_csv you need to write here relative or absolute path to your csv file.
On second position you need to write value (True or False). If argument is false json file creation will not be done, the function will just return this file as a variable. By default the argument is true.
##### * If you want to convert json to csv you must use:
```python
json_to_csv(file_json, file_creating=)
```
Instead file_json you need to write here relative or absolute path to your json file.
On second position you need to write value (True or False). If argument is false csv file creation will not be done, the function will just return this file as a variable. By default the argument is true.

## License

MIT

### Autor

Kovalev Maxim