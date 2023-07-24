import json
from datetime import datetime
import pytz

def convert_to_utc_minus_3(mod_time_str):
    # Check if the timezone offset format is '-03:0'
    if mod_time_str[-3] == ':':
        mod_time_str = mod_time_str[:-3] + mod_time_str[-2:]
    brtz = pytz.timezone('America/Sao_Paulo')
    mod_time = datetime.fromisoformat(mod_time_str)
    mod_time_utc_minus_3 = mod_time.replace(tzinfo=pytz.utc).astimezone(brtz)
    return mod_time_utc_minus_3.strftime('%Y-%m-%d %H:%M:%S')

def get_size_in_mb(size_bytes):
    return size_bytes / (1024 * 1024)

with open('FileList.json') as f:
    data = json.load(f)

output_data = {}
for item in data:
    path_parts = item["Path"].split("/")
    if len(path_parts) < 2:
        continue
    parent_folder = path_parts[-2]
    name = item["Name"]
    if ".bzEmpty" in name:
        continue
    size_mb = get_size_in_mb(item["Size"])
    mod_time_utc_minus_3 = convert_to_utc_minus_3(item["ModTime"])
    if parent_folder not in output_data:
        output_data[parent_folder] = []
    output_data[parent_folder].append(f"Name: {name}, Size: {size_mb:.2f} MB, ModTime Brazil: {mod_time_utc_minus_3}")

with open('output.txt', 'w') as f:
    for parent_folder, entries in output_data.items():
        f.write(f"Parent Folder: {parent_folder}\n")
        for entry in entries:
            f.write(f"{entry}\n")
        f.write("\n")

print("Output has been written to output.txt")
