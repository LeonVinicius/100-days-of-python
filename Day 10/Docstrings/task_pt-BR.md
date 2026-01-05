Você pode usar docstrings para escrever comentários de várias linhas que documentam seu código.

### Sintaxe
Basta colocar seu texto dentro de um par de três aspas duplas.

por exemplo.
```
"""
Meu
Comentário
De Várias Linhas
"""

```

### Documentando Funções
Uma característica interessante das docstrings é que você pode usá-la logo abaixo da definição de uma função e esse texto será exibido quando você passar o mouse sobre uma chamada de função. É uma boa maneira de lembrar o que uma função criada por você faz.

por exemplo.
```
def minha_funcao(num):
    """Multiplica um número por ele mesmo."""
    return num * num
```