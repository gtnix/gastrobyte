while True:
    try:
        idade = int(input("Insira a sua idade: "))
        if 0 <= idade <= 12:
            print("Criança")
            break
        elif 13 <= idade <= 18:
            print("Adolescente")
            break
        elif idade > 18:
            print("Adulto")
            break
        else:
            print("entrada inválida")
    except ValueError:
        print("Entrada inválida")
        

