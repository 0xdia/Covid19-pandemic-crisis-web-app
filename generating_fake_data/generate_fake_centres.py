import csv

# centre/daira => 548 centres de vaccination en total

with open('data/centres_vaccination.csv', mode='w') as centres:
    centres_writer = csv.writer(centres, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['id', 'zone_id']
    centres_writer.writerow(_ for _ in header)

    for i in range(1, 549):
        centres_writer.writerow([i, i])
