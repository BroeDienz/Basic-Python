iniroti = {
    "rtp": "roti panggang",
    "rtl": "roti lapis",
    "rtk": "roti kukus"
    
}

# update data
iniroti ["rtl"] = "roti mumet"
print (iniroti)
iniroti["rtb"] = "roti bakar"
print (iniroti)

iniroti.update({"rtl": "roti lapis"})
iniroti.update({"rtt": "roti tawar"})
print(iniroti)

# checking  
print(iniroti.get("rtk"))
print(iniroti.get("rtc"))

#deleting
del iniroti["rtt"]
print (iniroti)