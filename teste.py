usuario_correto = 'admin'
senha_correta = 'admin'
 
usuario = input("Digite o usuario: ")
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login realizado com sucesso!')
else:
    print('Credenciais inválidas!')
    
    #crie uma aplicação Para verificar onde o ponto está localizado no plano cartesiano
x = float(input("digite o valor de x: "))
y = float(input("digite o valor de y: "))

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
else:
    print('O ponto esta na origem')
    
