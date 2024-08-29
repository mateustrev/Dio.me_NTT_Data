# Datetime
[doc](https://docs.python.org/3/library/datetime.html)\
Uma data *aware* carrega fuso horário, enquanto uma data *naive* não carrega.\
Os objetos **date**, **time** **timedelta** e **datetime**  são os objetos mais populares do módulo **datetime**.\
O objeto **timedelta** permite realizar diversas operações matemáticas com datas. Esse objeto não funciona com o objeto **time**, apenas com **date** e **datetime**.\
Os métodos **strftime** e **strptime** são métodos para formatar as datas em python. O primeiro serve para formatar uma data, o segundo é utilizado para realizar o parsing de valores armazenados em uma string em uma variavel do tipo datetime.\
A biblioteca **pytz** serve para lidar com fuso-horários. Necessário instalar a biblioteca - *pip install pytz*\
É uma boa prática armazenar e tratar as datas *utc* no sistema, modificando para o fuso horário do usuário apenas na hora de exibir.

## Métodos
 - date.today = retorna a data de hoje.
 - datetime.today = retorna data e hora do momento.
 - datetime.now = retorna data e horario com timezone.
 - datetime.utcnow = retorna data e horario em utc time.


