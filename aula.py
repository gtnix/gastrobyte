import os

velocidades_medias = []

def subtexto(texto):
    os.system("clear")
    print(texto)

def calcular_velocidade_media(distancia, tempo):
    velocidade_media = distancia / tempo
    subtexto(f"A velocidade média foi de {velocidade_media:.2f} km/h")
    velocidades_medias.append(velocidade_media)

def historico_velocidade():
    os.system("clear")
    print("Histórico das 3 últimas velocidades médias:\n")
    for velocidades in velocidades_medias:
        print(velocidades)
    
for dia in ["seg", "ter", "quar"]:
    distancia = float(input(f"{dia.upper()}. Digite aqui a distância percorrida: "))
    tempo = float(input(f"{dia.upper()}. Digite aqui o tempo do percurso: "))
    calcular_velocidade_media(distancia, tempo)

historico_velocidade()


