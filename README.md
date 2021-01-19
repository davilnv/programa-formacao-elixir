# Programa de Formação em Elixr | Teste Técnico
Utilizei nesse teste a linguagem Python, usei dos meus conhecimentos na linguagem para solucionar o problema.

## Como executar o código?
A pasta possui dois arquivos (.py), utilizei classe na maior parte do teste, pois entendi que seria mais prático, essas classes estão no arquivo classes.py. Já o outro arquivo, o main.py, está toda a parte de instância das classes, lista e chamada de funções, ao contrário de chamar um método para realizar o que foi pedido, separei em 3 funções. 
- Para executar o código, utilizando um terminal é necessário passar o comando:

> python3 main.py

Estando na pasta onde está os dois arquivos.

- Outra forma de realizar essa execução é atravéz da IDE Pycharm, abrindo a pasta e executando o arquivo main.py

## Como eu solucionei o problema?
Para cada retorno pedido no teste existe uma função para realiza-lo, basta instânciar um ou mais items, adicionar a lista e da mesma forma, instânciar um ou mais pessoas e adicionar a lista de pessoas, com essas duas listas alimentadas, basta instanciar a classe Cart (classe criada para facilitar a entrada das duas listas e a manipulação) e chamar as funções, após essa chamada é exibido um retorn em tela.

## O problema das dízimas periodicas
Para solucionar o problema com as dízimas, procurei uma forma onde os primeiros valores foram arredondados para duas casas decimais e o último valor, fosse adicionado um número para dar o valor exato, retornando um dicionário

## Valores na instância da classe
Como é detalhado no teste, os valores utilizados foram inteiros, então para o preço do item utilizei do valor considerando que 1 real equivale a 100 centavos, sendo assim, ao instânciar um objeto do tipo Item, preciso passar o preço em centavos, exemplo:

```python
item = Item("Coca", 12, 1000, 500, 12000)
```
- Onde 12 é a quantidade de itens comprados, 1000 é o preço do item, 500 o preço por peso e 12000 o preço por pacote

## Considerações finais
Algumas coisas na intepretação da explicação do teste me confudiram, mas depois de analisar direito o que estava sendo pedido consegui desenvolver, não tenho certeza se meu código está 100% correto, mas fiz o que foi mais prático.

