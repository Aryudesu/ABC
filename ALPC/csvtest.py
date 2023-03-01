import csv
with open("ALPC/test.csv", 'r') as f:
    reader = csv.DictReader(f)
    for line in reader:
        keys = line.keys()
        for key in keys:
            data = line.get(key)
            print(type(data), data)
            if data:
                print("True")
