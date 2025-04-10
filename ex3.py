usuario_tela = input("Usuário: ")
senha_tela = input("Senha: ")

usuario = "Giuliana"
senha = "Takara"

if usuario_tela.upper() != usuario and senha_tela != senha:
    print("Acesso negado!")
else:
    print("Acesso liberado!")

