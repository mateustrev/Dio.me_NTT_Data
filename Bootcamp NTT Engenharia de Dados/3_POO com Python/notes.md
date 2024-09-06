# POO com Python

## Classes
A sintaxe para a criação de uma classe é *class CLASSE:*.\
A sintaxe para criação de um método de uma classe é *def METODO(self):*.\
Ao definir um método, sempre definir *self* como primeiro parametro, e utilizar a sintaxe *self.var* ao definir uma variável dentro de uma classe.\
Métodos especiais começam com duplo underline e servem para adaptar métodos e operadores de objetos nativos do python para as classes de objetos criadas.\
É possível criar métodos dentro de métodos (nested), e o método interno não precisa definir o *self* como primeiro parâmetro.

## Objetos
Um objeto pode ser instanciado com a sintaxe *OBJETO = CLASSE(PARAM,...)*.\
Os atributos podem ser acessadas com a sintaxe *OBJETO.VAR*.\
Os métodos podem ser acessados com a sintaxe *OBJETO.MÉTODO()*.

## Construtores e destrutores
O método especial *\_\_init__* é utilizado para instanciar um objeto de uma classe criada.\
Assim como todos os métodos, o primeiro parametro dos construtores e destrutores deve ser o *self*.\
O método especial *\_\_del__* é utilizado para destruir um obejto e desalocar a memória. O "coletor de lixo"do python gerencia automaticamente a memória, portanto só utilizar o método destrutor quando for realmente necessário.\
Para chamar o método destrutor, utilizamos a seguinte sintaxe: *del OBJETO*.

## Herança
Para que uma classe filha herde de uma classe já criada, utilizamos a sintaxe : *class CLASSE_FILHA(CLASSE_PAI):*.\
Para que uma classe filha herde de mais de uma classe (herança múltipla), utilizamos a sintaxe: *class CLASSE_FILHA(CLASSE_MÃE, CLASSE_PAI)*.\
Se a classe C extende da classe B, e esta extende da classe A, então a classe C também extende de A.

## Utilidades
def \_\_str__(self): return f"{self.\_\_class__.\_\_name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.\_\_dict__.items()])}"
* O código acima retorna uma string contendo o nome da classe, seguida pelos nomes e valores dos atributos, separados por vírgula. Útil para fazer a representação de uma classe.  
* O método *\_\_str__*, se criado na classe, definirá a saída de *print(self)* em um outro método por exemplo, assim como a saída de *print(OBJETO)* para instâncias dessa classe.
* ver também método *\_\_repr__*

