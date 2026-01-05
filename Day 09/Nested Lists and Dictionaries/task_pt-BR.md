Você pode misturar e combinar vários tipos de dados para obter a estrutura desejada.

### Aninhando uma Lista dentro de um Dicionário
Em vez de um valor String atribuído a uma chave, podemos substituí-lo por uma Lista. Você pode aninhar uma Lista em um Dicionário assim:

```
my_dictionary = {
    key1: [Lista],
    key2: Valor,
}
```

### PAUSA 1
Veja se você consegue descobrir como imprimir "Lille" da Lista aninhada chamada `travel_log`.
```
travel_log = {
    "França": ["Paris", "Lille", "Dijon"],
    "Alemanha": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  Para obter essa parte: <code>["Paris", "Lille", "Dijon"]</code>
Você precisaria de: <code>travel_log["França"]</code>

Portanto para conseguir Lille, você precisa de:
<code>travel_log["França"][1]</code>
</div>

### Aninhando Listas dentro de outras Listas

Já vimos Listas Aninhadas antes:

```
lista_aninhada = ["A", "B", ["C", "D"]]
```

### PAUSA 2
Você se lembra de como obter itens que estão profundamente aninhados em uma lista? Tente imprimir "D" da lista `lista_aninhada`.

<div class="hint">
  Para obter essa lista: ["C", "D"] vamos precisar do código:

<code>lista_aninhada[2]</code>

Portanto, para conseguir "D" precisamos de:

<code>lista_aninhada[2][1]</code>
</div>


### Aninhando um Dicionário dentro de um Dicionário
Você também pode aninhar um dicionário em outro dicionário:

```
my_dictionary = {
    key1: Valor,
    key2: {Chave: Valor, Chave: Valor},
}
```

### PAUSA 3
Descubra como imprimir "Stuttgart" a partir da seguinte lista:
```
travel_log = {
  "França": {
    "cidades_visitadas": ["Paris", "Lille", "Dijon"], 
    "total_visitas": 12
   },
  "Alemanha": {
    "cidades_visitadas": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visitas": 5
   },
}
```