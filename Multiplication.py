tables = [1,2,3,]
lines = [1,2,3,4,5]
for table in tables:
    print("\n")
    for line in lines:
        print(table,line,table * line)

for table in range(2,5):
    for line in range(1,5):
        print(table*line)
    print("\n")