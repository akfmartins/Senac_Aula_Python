def main():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    if salario <= 2424.00:
        novo_salario = salario * 1.06  # Aumento de 6%
        print(f"O funcionário {nome} terá um aumento salarial.")
        print(f"Novo salário: R${novo_salario:.2f}")
    else:
        print(f"O funcionário {nome} não terá aumento salarial este ano.")

if __name__ == "__main__":
    main()
