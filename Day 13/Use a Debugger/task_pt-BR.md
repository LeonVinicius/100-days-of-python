A maioria dos IDEs (Ambientes de Desenvolvimento Inteligentes), como o PyCharm, terá ferramentas integradas para depuração. Isso é geralmente conhecido como depurador. De muitas maneiras, eles são como instruções de impressão em esteróides.

Os depuradores nos permitem espiar nosso código durante a execução e pausar em linhas escolhidas para descobrir qual é o mecanismo interno e onde está dando errado.

Existem algumas coisas que são as mesmas na maioria dos IDEs com as quais você deve estar familiarizado:

1. **Ponto de interrupção** - Você pode definir um ponto de interrupção clicando em uma linha na margem do código (onde estão os números das linhas). Esta linha será onde o programa pausa durante a execução de depuração.

2. **Passar por cima** - Este botão passará pela execução do seu código linha por linha e permitirá que você veja os valores intermediários de suas variáveis.
3. **Entrar** - Isso entrará em quaisquer outros módulos que o seu código referencia. Por exemplo, se você usar uma função do módulo random, ele mostrará o código original dessa função para que você possa entender melhor sua funcionalidade e como ela se relaciona com seus problemas.
4. **Entrar no meu código** - Isso faz a mesma coisa que Entrar, mas limita o escopo ao código do seu próprio projeto e ignora o código da biblioteca, como o random.

### PAUSA 1
Use o depurador PyCharm para descobrir qual é o problema no código inicial e corrija-o.