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
gender = ['M', 'F']
variants = ['Epsilon', 'Eta', 'Iota', 'Kappa', 'Zeta', 'Alpha', 'Beta', 'Delta', 'Gamma']

with open('data/patients.csv', mode='w') as patients:
    patients_writer = csv.writer(patients, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['code', 'age', 'sex', 'degreVulnrablite', 'utilisateur', 'variant_label', 'degreSeverite', 'demande', 'zone_id']
    patients_writer.writerow(_ for _ in header)

    for i in range(100000, 110001):
        row = [i, randint(10, 100)]
        gen = gender[randint(0, 1)]
        row.append(gen)

        full_name = ""
        if gen == 'M':
            full_name += male_names[randint(0, len(male_names)-1)] + " "
        else:
            full_name += female_names[randint(0, len(female_names)-1)] + " "
        full_name += prefix[randint(0, len(prefix)-1)] + " "
        full_name += (male_names+female_names)[randint(0, len(male_names)+len(female_names)-1)]

        row.append(full_name)
        
        row.append(randint(1, 10))
        row.append(randint(1, 1500))
        row.append(variants[randint(0, len(variants)-1)])
        row.append(randint(1, 10))
        row.append(randint(1,100000))
        row.append(randint(1, 548))

        patients_writer.writerow(row)
