Um dicionário em Python funciona de maneira semelhante a um dicionário na vida real. É uma estrutura de dados que nos permite associar uma chave a um valor e emparelhar essas duas peças de dados.

Aqui está como você cria um dicionário em Python:
```
# Um dicionário exemplo
cores = {
    "maçã": "vermelho", 
    "pêra": "verde", 
    "banana": "amarelo"
}

```

Aqui está como você recupera itens de um dicionário:
```
print(cores["pêra"])
#Vai imprimir "verde"
```

Aqui está como criar um dicionário vazio:
```
meu_dicionario_vazio = {}
```

Aqui está como você pode adicionar novos itens a um dicionário existente:

```
cores["pêssego"] = "rosa"
```

Esta também é a maneira de editar um valor existente em um dicionário:
```
cores["maçã"] = "verde"
```

Aqui está como percorrer um dicionário e imprimir todas as chaves:
```
for chave in cores:
    print(chave)
```

Aqui está como percorrer um dicionário e imprimir todos os valores:
```
for chave in cores:
    print(cores[chave])
```