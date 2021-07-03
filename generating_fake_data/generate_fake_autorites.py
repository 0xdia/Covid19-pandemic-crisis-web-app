import csv
from random import randint
from covidapp import bcrypt

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

with open('covidapp/data/autorites.csv', mode='w') as autorites:
    autorites_writer = csv.writer(autorites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    header = ['id', 'nom_complet', 'email', 'password']
    autorites_writer.writerow(_ for _ in header)

    for i in range(1, 50):
        row = [i]

        full_name = ""
        gen = ['M', 'F'][randint(0,1)]
        if gen == 'M':
            full_name += male_names[randint(0, len(male_names)-1)] + " "
        else:
            full_name += female_names[randint(0, len(female_names)-1)] + " "
        full_name += prefix[randint(0, len(prefix)-1)] + " "
        full_name += (male_names+female_names)[randint(0, len(male_names)+len(female_names)-1)]

        row.append(full_name)
        
        email = full_name.replace(' ', '.')+"@sante.dz"
        password = bcrypt.generate_password_hash(email).decode("utf-8")

        row.extend([email, password])

        autorites_writer.writerow(row)
