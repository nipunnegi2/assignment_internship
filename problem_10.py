def get_keys_from_dicts(lst):
    keys = set()
   
    for d in lst:
        
        keys.update(d.keys()) #add each key of dict to set 
    
    return keys


data = [{"name": "ABC", "AGE": "20"}, {"name": "XYZ", "company": "QWE"}]


unique_keys = get_keys_from_dicts(data)


print("Keys present in the dictionaries:", unique_keys)
