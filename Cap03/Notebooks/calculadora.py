# Cacluladora
def somar(x,y):
    return x+y
def subtrair(x,y):
    return x-y
def dividir(x,y):
    return x / y
def multiplicar(x,y):
    return x * y
def menu():
    print("         calculadora         \n")
    print("1. Soma\n")
    print("2. Subtrair\n")
    print("3. Multiplicar\n")
    print("4. Dividir\n")
    print("0. sair")

menu()
opcao=int(input("Selecione uma operacao: "))
while(opcao!=0):
    if(opcao > 0 and opcao <=4):
        x=float(input("Digite o primeiro elemento: "))
        y=float(input("Digite o segundo elemento: "))
        if(opcao==1):
            print(somar(x,y))
        elif(opcao==2):
            print(subtrair(x,y))
        elif(opcao==3):
            print(multiplicar(x,y))
        elif(opcao==4):
            print(dividir(x,y))
    else:
        menu()
        opcao=int(input("Selecione uma opcao valida: "))
    menu()
    opcao=int(input("Selecione uma operacao: "))
