#Вывести количество выживших женщин и мужчин из файлика train.csv
import csv
male: int = 0
female: int = 0
with open("train.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Survived'] == '1':
            match row['Sex']:
                case "male":
                    male += 1
                case "female":
                    female += 1
    print("Количество выживших мужчин: {0}\nКоличество выживших женщин: {1}".format(male, female))



