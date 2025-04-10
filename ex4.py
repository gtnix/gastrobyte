coordenada_x = float(input("Insira a coordenada x: "))
coordenada_y = float(input("Insira a coordenada y: "))

if coordenada_x > 0 and coordenada_y > 0:
    print("As coordenadas encontram-se no PRIMEIRO QUADRANTE.")
elif coordenada_x < 0 and coordenada_y > 0:
    print("As coordenadas encontram-se no SEGUNDO QUADRANTE.")
elif coordenada_x < 0 and coordenada_y < 0:
    print("As coordenadas encontram-se no TERCEIRO QUADRANTE.")
elif coordenada_x > 0 and coordenada_y < 0:
    print("As coordenadas encontram-se no QUARTO QUADRANTE.")
else: 
    print("As coordenadas encontram-se no eixo ou origem.")