#programa  = list()
# #while True:
#    cadastro = str(input("Nome:  "))
#   cadastrarnota = float(input("Nota:  ")) 
#    todososalunos = str(input("Nome:  "))
#    excluiraluno = str(input("Deseja excluir esse aluno? [S/N]"))
#    if excluiraluno in "Ss": 
#        break
#    sair = str(input("Deseja terminar? [S/N]")) 
#    if sair in "Nn": 
#        break 

#print('-='*80)
#print(programa)

#programa = list()
#while True:
#        if opção == 1:
#                ação = cadastrar_aluno = str(input("Nome: "))
#        else:
#            if opção == 2:
#                    ação = cadastrarnota = int(input("Nota:  "))
#            else:
#                if opção == 3:
#                        ação = consultaraluno = str(input("Nome:  "))
#                else:
#                    if opção == 4:
#                            ação = todososalunos = str(input("Listar:  "))
#                    else: 
#                        if opção == 5:
#                                ação = remover_aluno = str(input("Deseja remover o aluno? [S/N]"))
#                        else: 
#                            if opção == 0:
#                                ação = sair = str(input("Deseja terminar? [S/N]"))
#                                if sair in "Nn": 
#                                    break
                            

#print(programa)

ls =[]
obj = ('', 0, 0)
turma = []
escolha = ''

while escolha != 0 :

        escolha = (input (("""
Escolha a opção abaixo:

1.Cadastrar aluno 
2.Cadastrar nota do aluno 
3.Consultar aluno 
4.Lista de aluno 
5.Excluir aluno 
0.Sair
         
Sua Opção: 
         
                 """)))
        if escolha == 1:
                obj[0].append(str(input('Nome do aluno' + "" )))
                obj[1].append(int(input("Número de cadastro:   ")))        
        elif escolha == 2:
                obj[2].append(float(input("Nota do aluno: ")))
        elif escolha== 3:
                print(f""" 
                Nome:{obj[0]}
                Cadastro: {obj[1]}
                Nota: {obj[2]}
                """) 
        elif escolha == 4:
                print("\n")
                print("\nLista de aluno\n")
                for i in range(ls.__len__()):    
                        obj.display(ls[i])      
        elif escolha == 5:
                i = obj.delete()
                del ls[i]     
        elif escolha == 0:
                print("Volte sempre!")





                                    
                      










