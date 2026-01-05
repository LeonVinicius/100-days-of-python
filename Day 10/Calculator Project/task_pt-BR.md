O objetivo é construir um programa de calculadora.

### Demonstração
https://appbrewery.github.io/python-day10-demo/


### Armazenando Funções como Valor de uma Variável
Você pode armazenar uma referência a uma função como valor para uma variável.
por exemplo:
```
def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Vai retornar 8
```
No arquivo inicial, você verá um dicionário que referencia cada um dos cálculos matemáticos que podem ser executados pela nossa calculadora. Teste e veja se você consegue fazer adição, subtração, multiplicação e divisão.

### PAUSA 1
TAREFA: Escreva as outras 3 funções - subtrair, multiplicar e dividir.

### PAUSA 2
TAREFA: Adicione essas 4 funções em um dicionário como os valores. Chaves = "`+`", "`-`", "`*`", "`/`"

### PAUSA 3
TAREFA: Use as operações do dicionário para executar os cálculos. Multiplique 4 * 8 usando o dicionário.


### Funcionalidades
- Programa pede ao usuário para digitar o primeiro número.
- Programa pede ao usuário para digitar um operador matemático(uma escolha entre "`+`", "`-`", "`*`" ou "`/`")
- Programa pede ao usuário para digitar o segundo número.
- Programa calcula o resultado com base no operador matemático escolhido.
- Programa pergunta se o usuário deseja continuar trabalhando com o resultado anterior.
- Se sim, o programa repete o processo usando o resultado anterior como o primeiro número.
- Se não, o programa pede ao usuário para digitar o primeiro número novamente e esquece todos os cálculos anteriores.
- Adicione o logo do arquivo art.py

<div class="hint">
  Tente elaborar um fluxograma para planejar seu programa.
</div>

<div class="hint">
    Para chamar a multiplicação do dicionário de operações, você escreveria seu código dessa maneira:

<code>result = operations["*"](n1= 5, n2= 3)</code>

O resultado seria igual a 15.
</div>