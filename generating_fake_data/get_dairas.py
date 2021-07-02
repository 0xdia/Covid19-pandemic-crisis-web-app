import csv

dairas = set()

with open('data/zones.csv') as zones:
    zones_reader = csv.reader(zones, delimiter=',')

    i = 0
    for row in zones_reader:
        if i != 0:
            dairas.add((row[2], row[4]))
        i += 1

with open('data/dairas.csv', mode='w') as dayras:
    dayras_writer = csv.writer(dayras, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['id', 'daira', 'wilaya']
    dayras_writer.writerow(_ for _ in header)

    i = 1
    for daira in dairas:
        dayras_writer.writerow([i, daira[0], daira[1]])
        i += 1
