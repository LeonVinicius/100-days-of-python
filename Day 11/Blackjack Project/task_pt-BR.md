### Escolha sua dificuldade
- **Normal** 😎: Use todas as dicas abaixo para concluir o projeto.
- **Difícil** 🤔: Use apenas as Dicas 1, 2, 3 para concluir o projeto.
- **Extra difícil** 😭: Use apenas Dicas 1 e 2 para concluir o projeto.
- **Especialista** 🤯: Use only Dica 1 para concluir o projeto.

### Nossas Regras do Jogo de Blackjack

- O baralho é ilimitado em tamanho.
- Não há curingas.
- O Valete/Dama/Rei todos contam como 10.
- O Ás pode contar como 11 ou 1.
- Use a seguinte lista como o baralho de cartas:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- As cartas na lista têm igual probabilidade de serem sorteadas.
- As cartas não são removidas do baralho conforme são sorteadas.
- O computador é o dealer.

<div class="hint" title="Dica 1">
Visite este site e experimente o jogo Blackjack:

https://games.washingtonpost.com/games/blackjack/

Depois, experimente o projeto completo do Blackjack aqui:

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Dica 2">
Leia esta descrição dos requisitos do programa: 

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Depois, tente criar seu próprio fluxograma para o programa.
</div>

<div class="hint" title="Dica 3">
Baixe e leia este fluxograma que eu criei:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
</div>

<div class="hint" title="Dica 4">
Crie uma função <code>deal_card()</code> que usa a Lista abaixo para retornar uma carta aleatória.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Lembre-se de que o 11 é o Ás.
</div>

<div class="hint" title="Dica 5">
Distribua ao usuário e ao computador 2 cartas cada usando <code>deal_card()</code> e <code>append()</code>.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Dica 6">
Crie uma função chamada <code>calculate_score()</code> que leva uma Lista de cartas como entrada e retorna a soma de todas as cartas na Lista como a pontuação. Pesquise a função <code>sum()</code> para ajudá-lo a fazer isso.
</div>

<div class="hint" title="Dica 7">
Dentro de <code>calculate_score()</code>, verifique um blackjack (uma mão com apenas 2 cartas: ás + 10) e retorne <code>0</code> em vez da pontuação real. <code>0</code> representará um blackjack no nosso jogo.
</div>

<div class="hint" title="Dica 8">
   Dentro de <code>calculate_score()</code> verifique um 11 (ás). Se a pontuação já está acima de 21, remova o 11 e substitua-o por um 1. Você pode precisar pesquisar para encontrar a documentação das funções internas do Python <code>append()</code> e <code>remove()</code>.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Dica 9">
Chame a função <code>calculate_score()</code>. Se o computador ou o usuário tem um blackjack (0) ou se a pontuação do usuário é mais de 21, então o jogo termina.
</div>

<div class="hint" title="Dica 10">
Se o jogo não terminou, pergunte ao usuário se ele quer puxar outra carta. Se sim, então use a função <code>deal_card()</code> para adicionar outra carta à Lista <code>user_cards</code>. Se não, então o jogo terminou.
</div>

<div class="hint" title="Dica 11">
A pontuação precisará ser rechecada com cada nova carta sorteada e as verificações da Dica 9 precisam ser repetidas até que o jogo termine.
</div>

<div class="hint" title="Dica 12">
  Uma vez que o usuário terminou, é hora de deixar o computador jogar. O computador deve continuar puxando cartas enquanto sua pontuação for menor que 17.
</div>

<div class="hint" title="Dica 13">
  Crie uma função chamada <code>compare()</code> e passe o<code>user_score</code> e o <code>computer_score</code>. 

- Se o computador e o usuário tiverem a mesma pontuação, então é um empate.
- Se o computador tem um blackjack (0), então o usuário perde.
- Se o usuário tem um blackjack (0), então o usuário ganha.
- Se o <code>user_score</code> for mais de 21, então o usuário perde.
- Se o <code>computer_score</code> for mais de 21, então o computador perde.
- Se não for nada do acima, então o jogador com a maior pontuação ganha.
</div>

<div class="hint" title="Dica 14">
  Pergunte ao usuário se eles querem reiniciar o jogo. Se eles responderem sim, limpe o console e comece um novo jogo de blackjack e mostre o logo de art.py.
</div>
