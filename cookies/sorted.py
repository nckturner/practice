
d= [{ "a": 1, "b": 3, "c": "FIRST"},
{ "a": 2, "b": 2, "c": "SECOND"},
{ "a": 3, "b": 1, "c": "THIRD"}]

print(d)

print(sorted(d, key=lambda x: x["b"]))
