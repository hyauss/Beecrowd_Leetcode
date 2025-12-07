#Problemas do Beecrowd do 5a10 sorteado em python

def Media1():
    A = float(input())
    B = float(input())
    Media = (A * 3.5 + B * 7.5) / (3.5 + 7.5)
    print(f"MEDIA = {Media:.5f}")
    
def Media2():
    A = float(input())
    B = float(input())
    C = float(input())
    Media = (A * 2 + B * 3 + C*5) / (10)
    print(f"MEDIA = {Media:.1f}")

def Diferenca():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    diferenca = (A*B - C*D)
    print(f"DIFERENCA = {diferenca}")

def Salario():
    A = int(input())
    B = int(input())
    C = float(input())
    salario = B*C
    print(f"NUMBER = {A}")
    print(f"SALARY = U$ {salario:.2f}")

def SalarioComBonus():
    A = str(input())
    B = float(input())
    C = float(input())
    salarioExtra = B+C*0.15
    print(f"TOTAL = R$ {salarioExtra:.2f}")





#Media1()
#Media2()
#Diferenca()
#Salario()
#SalarioComBonus()