from data import MENU, resources

lucro = 0
MAQUINA_LIGADA = True


def verificar_recursos(ingredientes_bebida):
    """Retorna True se houver recursos suficientes, False se não"""
    for i in ingredientes_bebida:

        if ingredientes_bebida[i] > resources.get(i, 0):
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def processar_moedas():
    """Retorna o valor total das moedas inseridas[cite: 23]."""
    print("Please insert coins.")

    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transacao_bem_sucedida(dinheiro_recebido, custo_bebida):
    """Verifica se o dinheiro é suficiente e calcula troco."""
    if dinheiro_recebido >= custo_bebida:

        troco = round(dinheiro_recebido - custo_bebida, 2)
        if troco > 0:
            print(f"Here is ${troco} in change.")

        global lucro
        lucro += custo_bebida
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def fazer_cafe(nome_bebida, ingredientes_bebida):
    """Deduz os ingredientes e serve a bebida"""
    for i in ingredientes_bebida:
        resources[i] -= ingredientes_bebida[i]
    print(f"Here is your {nome_bebida} ☕. Enjoy!")


while MAQUINA_LIGADA:

    escolha = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if escolha == "off":
        MAQUINA_LIGADA = False
        print("Machine shutting down...")

    elif escolha == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${lucro}")

    elif escolha in MENU:
        bebida = MENU[escolha]

        if verificar_recursos(bebida["ingredients"]):
            pagamento = processar_moedas()
            if transacao_bem_sucedida(pagamento, bebida["cost"]):

                fazer_cafe(escolha, bebida["ingredients"])