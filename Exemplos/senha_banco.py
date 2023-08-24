def validar_senha(senha_digitada, senha_correta):
    if senha_digitada == senha_correta:
        return True
    else:
        return False

senha_correta = "12345"  # Defina a senha correta aqui

senha_digitada = input("Digite sua senha: ")

if validar_senha(senha_digitada, senha_correta):
    print("Acesso permitido.")
else:
    print("Senha incorreta. Acesso negado.")
