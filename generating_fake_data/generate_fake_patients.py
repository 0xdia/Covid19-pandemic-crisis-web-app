import csv
from random import randint

male_names = [
        'Mohammed', 'Amine', 'Mouslim', 'Ahmed', 'Dhiaa Eddine', 
        'Hatem', 'Juba', 'Allaa Eddine', 'Zine Eddine', 'Malek',
        'Abde Al Aziz', 'Younes', 'Youcef', 'Ramzi',
        'Imad', 'Omar', 'Mokhtar', 'Lakhdar', 'Kaddour',
        'Sohaib', 'Dirar', 'Haitham', 'Abde Al Bassit', 'Saleh',
        'Oussama', 'Akram', 'Abdel Allah', 'Hakim'
        ]

female_names =  [
                'Roumaissa', 'Khaoula', 'Manel', 'Feriel', 
                'Maria', 'Lilya', 'Yousra', 'Aicha', 
                'Naoual', 'Loubna', 'Melissa', 'Maissa', 'Sara',
                'Khadija', 'Zineb', 'Saliha', 'Yamina', 'Amina',
                'Chaima', 'Mahdiya', 'Sahar', 'Nesrine', 
                'Yasmine', 'Farah', 'Karima', 'Zolikha', 'Foulla'
                ]

prefix = ['ben', 'bou', 'ould', 'bel']

with open('covidapp/data/patients.csv', mode='w') as patients:
    patients_writer = csv.writer(patients, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['code', 'age', 'sex', 'nom_complet', 'deg_vuln', 'util_id', 'var_id', 'deg_sev', 'zone_id']
    patients_writer.writerow(_ for _ in header)

    for i in range(1, 2000):
        row = [i, randint(10, 100)] # code and age

        full_name = ""
        gen = ['M', 'F'][randint(0,1)]
        if gen == 'M':
            full_name += male_names[randint(0, len(male_names)-1)] + " "
        else:
            full_name += female_names[randint(0, len(female_names)-1)] + " "
        full_name += prefix[randint(0, len(prefix)-1)] + " "
        full_name += (male_names+female_names)[randint(0, len(male_names)+len(female_names)-1)]

        row.append(gen)
        row.append(full_name)
        row.append(randint(1, 10))  # degre de vulnrabilite
        row.append(randint(200000, 205000))  # utilisateur id
        row.append(randint(1, 2)) # variant id
        row.append(randint(1, 10)) # degre de severite
        row.append(randint(1,548))

        patients_writer.writerow(row)
