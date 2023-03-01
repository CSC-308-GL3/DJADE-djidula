
from datetime import date
from devoir import Grade, Employe, Client, Intervention, Contrat


gradeA = Grade("A", "Grade A", 40)



employe1 = Employe("E1", "Jean Dupont", gradeA, date(2018, 1, 1))

client1 = Client("C1", "Client 1", "1 rue de la Paix", "75001", "Paris", 50)

intervention1 = Intervention("I1", date(2023, 3, 1), 4, 0.5, employe1)
intervention2 = Intervention("I2", date(2023, 3, 2), 6, 0.5, employe1

contrat1 = Contrat("CNT1", date(2023, 3, 1), client1, 10000, [intervention1, intervention2])
