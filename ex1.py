while True:
    try:
        numero = int(input("Insira um número de 0 a 100: "))
        
        if 0 <= numero <= 100:
            if numero % 2 == 0:
                print("PAR")
            else:
                print("ÍMPAR")
            break  # Sai do loop após entrada válida
        else:
            print("Número inválido! Tente novamente com um número entre 0 e 100.")
    except ValueError:
        print("Entrada inválida! Por favor, insira apenas números inteiros.")


    