### Escopo Local
Variáveis (ou funções) declaradas dentro de funções possuem escopo local (também chamado de escopo da função). Elas só são vistas por outros códigos dentro do mesmo bloco de código.

ex.
```
def minha_funcao():
    minha_var_local = 2
    
# Isso causará um NameError
print(minha_var_local) 
```

### Escopo Global
Variáveis ou funções declaradas no nível superior (não identado) de um arquivo de código possuem escopo global. É acessível em qualquer lugar no arquivo de código.

ex.

```
minha_var_global = 3

def minha_funcao():
    # Isso funciona sem problemas
    print(minha_var_global)
```