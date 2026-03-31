"""n = 5 
for i in range(1, n + 1):
  print("*" * i)"""


"""rows = 5
for num in range(1, rows + 1):
    for i in range(num):
        print(num, end=" ")
    print()"""


"""rows = 5
for i in range(rows):                
    for j in range(i + 1):           
        print(chr(65 + j), end="")   
    print() """                         

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

