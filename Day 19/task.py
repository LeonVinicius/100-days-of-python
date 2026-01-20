from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def para_frente():
    tim.forward(10)

def para_tras():
    tim.backward(10)

def girar_direita():
    tim.right(10)

def girar_esquerda():
    tim.left(10)

def limpar_tela():
    tim.clear()
    tim.setposition(0,0)


def aplicar_comando(registrador_turtle, tecla, funcao_movimento):
    registrador_turtle(key=tecla, fun=funcao_movimento)

move = {
    "w": para_frente,
    "s": para_tras,
    "a": girar_esquerda,
    "d": girar_direita,
    "c": limpar_tela,
}

screen.listen()


for tecla, acao in move.items():
    aplicar_comando(screen.onkey, tecla, acao)

screen.exitonclick()