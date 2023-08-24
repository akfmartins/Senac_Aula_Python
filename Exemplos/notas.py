def verificar_aprovacao(nota):
    nota_de_corte = 6
    if nota >= nota_de_corte:
        return "Aprovado"
    else:
        return "Reprovado"
    
try:
    nota_aluno = float(input("Digite a nota do Aluno: "))
    resultado = verificar_aprovacao(nota_aluno)
    print(resultado)
except ValueError:
    print("Por favor digite um valor numérico válido.")

'''
Neste código, a função verificar_aprovacao compara a nota inserida com a nota de corte. 
Se a nota for maior ou igual à nota de corte, o aluno é considerado aprovado. 
Caso contrário, o aluno é considerado reprovado. 
O bloco try e except é usado para lidar com a possibilidade de entrada inválida, ou seja, caso o usuário insira algo que não seja um número.
'''