iniroti = {
    "rtp": "roti panggang",
    "rtl": "roti lapis",
    "rtk": "roti kukus"
    
}

#looping first try
for roti in iniroti:
    print (roti)

#interables
keys = iniroti.keys()
print (keys)

for key in iniroti.keys():
    print(iniroti.get(key))

values = iniroti.values()
print (values)

for value in iniroti.values():
    print(value)

items = iniroti.items()
print (items)

for item in iniroti.items():
    print(item)
    
for key,value in iniroti.items():
     print(f"key={keys}, value={values}")