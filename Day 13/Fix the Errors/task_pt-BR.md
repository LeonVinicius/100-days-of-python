Corrija quaisquer erros (sublinhados em vermelho) que apareçam no editor antes de executar o seu código. Os avisos (amarelos) são correções opcionais, às vezes causarão um problema mais tarde, outras vezes está tudo bem e o editor simplesmente não entende o que você está tentando fazer.

### Capturando Exceções
Você pode usar um bloco try/except no Python para capturar quaisquer exceções que possam ocorrer. Por exemplo, se você imaginar que pode haver uma chance de erro do usuário. Você pode impedir que ele quebre seu código antecipando isso. Você armadilha o código perigoso dentro de um bloco try e usa um bloco except para capturar quaisquer erros potenciais. Então você define o que deve acontecer quando esse erro ocorrer, em vez de simplesmente travar e parar o código.

ex.

```
try:
    print(6 > "cinco")
except TypeError:
    print("Você não pode misturar inteiros e strings em uma comparação")
```

### PAUSA 1 
Corrija o bug para que a instrução de impressão exiba o valor correto da idade na área de saída.