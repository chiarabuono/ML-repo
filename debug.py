lines = ["#Outlook   Temperature  Humidity  Windy  Play",
"sunny      hot          high      TRUE	 no",
"sunny      mild         high      FALSE  ",
"sunny      cool         normal    FALSE  yes",
"sunny      mild         normal    TRUE   "]

database = {}
for line in lines:
    if "#" in line:
        header = [e.strip() for e in line.split("#")[1].split(" ") if e.strip() != ""]
        for e in header:
            if e != "":
                database[e] = []
        continue

    values = [e.strip() for e in line.split(" ") if e.strip() != ""]
    if len(values) < len(header):
        values.append("N/A")

    for i, value in enumerate(values):
        if value == "TRUE": value = True
        elif value == "FALSE": value = False
        key = header[i] 
        database[key].append(value)

print(database)
