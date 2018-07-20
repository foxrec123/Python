
matrix = [
    [12, 15, 20, 96],
    [52, 45, 52, 37],
    [14, 25, 86, 56],
];

print('Strings: ');

for string in matrix:
    print(string);

print('Rows: ');

list_1 = list();
list_2 = list();
list_3 = list();
list_4 = list();


for row in matrix:
    list_1.append(row[0])
    list_2.append(row[1])
    list_3.append(row[2])
    list_4.append(row[3])

print(list_1);
print(list_2);
print(list_3);
print(list_4);



