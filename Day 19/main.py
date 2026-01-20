import random
from turtle import Turtle, Screen

jogando = False
tela = Screen()
tela.setup(width=500, height=400)

cores_pt = ["vermelho", "laranja", "amarelo", "verde", "azul", "roxo"]
cores_en = ["red", "orange", "yellow", "green", "blue", "purple"]

usuario_aposta = tela.textinput(
    title="Faça sua aposta",
    prompt="Escolha uma cor: (vermelho, laranja, amarelo, verde, azul, roxo)"
)

posicoes_y = [-70, -40, -10, 20, 50, 80]
todas_tartarugas = []

for i in range(0, 6):
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.color(cores_en[i])
    nova_tartaruga.penup()
    nova_tartaruga.goto(x=-230, y=posicoes_y[i])
    todas_tartarugas.append(nova_tartaruga)

if usuario_aposta:
    usuario_aposta = usuario_aposta.lower()
    if usuario_aposta in cores_pt:
        jogando = True

while jogando:
    for tartaruga in todas_tartarugas:
        distancia_aleatoria = random.randint(0, 10)
        tartaruga.forward(distancia_aleatoria)

        if tartaruga.xcor() > 230:
            jogando = False
            cor_vencedora_en = tartaruga.pencolor()

            indice_vitoria = cores_en.index(cor_vencedora_en)
            cor_vencedora_pt = cores_pt[indice_vitoria]

            if cor_vencedora_pt == usuario_aposta:
                print(f"Você ganhou! A tartaruga {cor_vencedora_pt} venceu!")
            else:
                print(f"Você perdeu! A vencedora foi a {cor_vencedora_pt}. Sua aposta foi {usuario_aposta}.")

            break

tela.exitonclick()