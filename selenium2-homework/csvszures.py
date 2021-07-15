import csv

with open('new.csv', 'w', encoding = 'utf-8') as new_csv:
    with open('table_in.csv', encoding = 'utf-8') as csvfile:
        nevek = csv.reader(csvfile, delimiter = ',')

        for i in nevek:
            new_csv.write(i[1].strip() + "," + i[0] + "\n")

# with open('new.csv', 'w', encoding = 'utf-8') as new_csv
#
#     new_csv = csv.writer(n('table_in.csv', encoding = 'utf-8') as csvfile:
#     nevek = csv.reader(csvfile, delimiter = ',')
#     email_list = []
#
#     for i in nevek:
#         print(i[0] + i[1])
#
# with open('new.csv', 'w', encoding = 'utf-8') as new_csv:
#     new_csv = csv.writer(email_list)