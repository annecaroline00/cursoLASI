while True:
    print(""" 
            Operações:

            Saldo Médio
            Porcentagem de clientes devedores
            Número de clientes com saldo credor
    
              """)

    debito1 = float(input("valor1: "))
    credito1 = float(input("valor1: "))
    saldo1 = debito1-credito1

    debito2= float(input("valor2: "))
    credito2 = float(input("valor2: "))
    saldo2 = debito2-credito2

    debito3 = float(input("valor3: "))
    credito3 = float(input("valor3: "))
    saldo3 = debito3-credito3

    debito4 = float(input("valor4: "))
    credito4 = float(input("valor4: "))
    saldo4 = debito4-credito4

    debito5 = float(input("valor5: "))
    credito5 = float(input("valor5: "))
    saldo5 = debito5-credito5

    debito6 = float(input("valor6: "))
    credito6 = float(input("valor6: "))
    saldo6 = debito6-credito6

    debito7 = float(input("valor7: "))
    credito7 = float(input("valor7: "))
    saldo7 = debito7-credito7

    debito8 = float(input("valor8: "))
    credito8 = float(input("valor8: "))
    saldo8 = debito8-credito8

    debito9 = float(input("valor9: "))
    credito9 = float(input("valor9: "))
    saldo9 = debito9-credito9

    debito10 = float(input("valor10: "))
    credito10 = float(input("valor10: "))
    saldo10 = debito10-credito10

    c1 = saldo1 
    c2 = saldo2 
    c3 = saldo3  
    c4 = saldo4 
    c5 = saldo5 
    c6 = saldo6  
    c7 = saldo7
    c8 = saldo8 
    c9 = saldo9 
    c10 = saldo10

    op = input("Operação a ser realizada:  ")

    if(op == "Saldo médio"):
        result = (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10)/10
    if(op == "Porcentagem de clientes devedores: "):
        result = 0 < (1- (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10))*100
    if(op == "Número de clientes com saldo credor"):
        result = (1(debito1+debito2+debito3+debito4+debito5+debito6+debito7+debito8+debito9+debito10)-(credito1+credito2+credito3+credito4+credito5+credito6+credito7+credito8+credito9+credito10))*100


    print(result)
