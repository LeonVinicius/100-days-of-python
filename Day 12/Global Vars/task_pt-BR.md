Você pode forçar o código a permitir que você modifique algo com global se usar a palavra-chave global antes de usá-la.

por exemplo. Isso lhe dará um erro

```
a = 1
def minha_função():
    a += 1
    print(a)
```

Mas isso funcionará
```
a = 1
def minha_função():
    global a
    a += 1
    print(a)
```