import csv

dataset_1=[]
dataset_2=[]

with open('bright_stars.csv','r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open('dwarf_starspro.csv','r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

headers_1=dataset_1[0]
star_data_1=dataset_1[1:]

headers_2=dataset_2[0]
star_data_2=dataset_2[1:]

headers=headers_1+headers_2

star_data=[]
for index,data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index]+star_data_2[index])

with open('finaldata.csv','a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)
    