#!/usr/bin/python3

data = {"a": {"b":"c"}, "d":{"f":"g", "h":{"i": "j"}}}
flattened_data = {}

def flatten(data, prev_keys):
     for key in list(data.keys()):
             if type(data[key]) == dict:
                     flatten(data[key], prev_keys + str(key) + "_")
             else:
                     flattened_data[prev_keys + str(key)] = data[key]

flatten(data, "")
print(f"original = {data}")
print(f"flattened = {flattened_data}")
            
