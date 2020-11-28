
my_dictionary = {
    "key1": "val1", 
    "key2": "val2"
    }
print(my_dictionary["key1"])        # val1
print(my_dictionary["key2"])        # val2


price_lookup = {
    "apple": 2.99,
    "orange": 3.99,
    "milk": 5.80
}
print(price_lookup["apple"])        # 2.99


# dictionary can contain str, kist, dict
d = {
    "k1": 123,
    "k2": [0, 1, 2],
    "k3": {
        "in_key1": "value1",
        "in_key2": "value2"
    },
    "k4": ["a", "b", "c"]
}
print(d["k2"][2])               # 2
print(d["k3"]["in_key1"])       # value1
print(d["k4"][1].upper())       # B

# add key value pair into dict
# d["key"] = "val"
d["k5"] = "val5"
print(d)        # {'k1': 123, 'k2': [0, 1, 2], 'k3': {'in_key1': 'value1', 'in_key2': 'value2'}, 'k4': ['a', 'b', 'c'], 'k5': 'val5'}


# only .keys() 
print(d.keys())         # dict_keys(['k1', 'k2', 'k3', 'k4', 'k5'])
# only .values()
print(d.values())       # dict_values([123, [0, 1, 2], {'in_key1': 'value1', 'in_key2': 'value2'}, ['a', 'b', 'c'], 'val5'])
# .items()
print(d.items())        # dict_items([('k1', 123), ('k2', [0, 1, 2]), ('k3', {'in_key1': 'value1', 'in_key2': 'value2'}), ('k4', ['a', 'b', 'c']), ('k5', 'val5')])

