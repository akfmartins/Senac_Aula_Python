saldo = 10
credito = 20
total = saldo + credito
tenho_dinheiro = total >= 50
tenho_compahia = True

print('Você tem R$', total, 'disponivel')
print('Devo ir?', tenho_dinheiro and tenho_compahia)