Python é um pouco diferente de outras linguagens de programação, pois não possui escopo de bloco.

Isso significa que as variáveis criadas aninhadas em outros blocos de código, por exemplo, loops for, instruções if, loops while etc., não possuem escopo local. Elas recebem escopo de função se estiverem dentro de uma função ou escopo global se não estiverem.

por exemplo

```
# Acessível em qualquer lugar
my_global_var = 1

def my_function():
    # Acessível apenas dentro de my_function()
    my_local_var = 2
    
for _ in range(10):
    # Acessível em qualquer lugar
    my_block_var = 3

```