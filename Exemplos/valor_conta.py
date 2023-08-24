valor_conta = float (input("Qual o valor da conta?"))
valor_conta = (valor_conta + (valor_conta * 10/100))
quantidade_pessoas = int(input("Por quantas pessoas será dividida a conta? "))
valor_por_pessoa = valor_conta/quantidade_pessoas
print("cada um deve pagar", valor_por_pessoa)