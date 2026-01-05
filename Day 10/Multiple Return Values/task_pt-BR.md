As funções terminam na palavra-chave `return`. Se você escrever código abaixo da declaração return, esse código não será executado.

No entanto, você pode ter várias declarações de retorno em uma única função. Então, como isso funciona?

### Retornos Condicionais

Quando temos controle de fluxo, como no código que se comportará de maneira diferente (irá por diferentes caminhos de execução) dependendo de certas verificações condicionais, podemos acabar com várias terminações (retornos).

por exemplo:
```
def podeComprarAlcool(idade):
    if idade >= 18:
        return True
    else:
        return False
```

### Retornos Vazios
Você também pode escrever return sem nada depois, e isso apenas diz à função para sair.

por exemplo:
```
def podeComprarAlcool(idade):
    # Se o tipo de dado da entrada idade não for um int, então saia.
    if type(idade) != int:
        return

    if idade >= 18:
        return True
    else:
        return False
```