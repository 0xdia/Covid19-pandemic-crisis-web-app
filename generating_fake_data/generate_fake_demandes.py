import csv

codes = set()

with open('data/patients.csv') as patients:
    patients_reader = csv.reader(patients, delimiter=',')

    i = 0
    for row in patients_reader:
        if i != 0:
            codes.add(row[0])
        i += 1


with open('data/demandes_vaccination.csv', mode='w') as demandes:
    demandes_writer = csv.writer(demandes, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['id', 'code_patient']
    demandes_writer.writerow(_ for _ in header)

    i = 1
    for code in codes:
        row = [i, code]
        demandes_writer.writerow(row)

        i += 1
