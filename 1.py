#задание 1
A = input("Введите имя: ")
B = input("Введите фамилию: ")
C = int(input("Введите год рождения: "))
print(A, B, C, sep="_")
A, B = B, A                              
C = C + 60     
print(A, B, C, sep="_")
