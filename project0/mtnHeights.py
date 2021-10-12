list =  {"Mount Everest": 8848, "K2": 8611, "Lhoste": 8516, "Makalu": 8485, "Cho Oyu": 8188}

for mtn in list.keys():
    print(mtn)

for elevation in list.values():
    print(elevation)

for mtn, elevation in list.items():
    print(mtn + " is " + str(elevation) + " meters tall.")