import csv

data=[]


with open('dwarf_stars.csv','r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)

data=data[data['Star_name'].notna()]
data=data[data['Distance'].notna()]
data=data[data['Mass'].notna()]
data=data[data['Radius'].notna()]

headers=data[0]
star_data=data[1:]

for data_point in star_data:
    data_point[2]=data_point[2]*0.000954588
    data_point[3]=data_point[3]*0.102763


with open('dwarf_stars_converted','a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)