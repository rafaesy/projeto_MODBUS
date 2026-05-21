# projeto_MODBUS

projeto da aula de informatica industrial, comunicação modbus TCP em python

## o que precisa instalar

ter o python instalado e rodar o pip pra instalar as bibliotecas

```
pip install -r requirements.txt
```

## como rodar

primeiro sobe o servidor:

```
cd servidor
python main.py
```

depois em outro terminal roda o cliente:

```
cd cliente
python main.py
```

digite as opções desejadas

## exemplos

tem dois exemplos na pasta exemplos, um de float e um de bits

```
python exemplos/exemplo_float.py
python exemplos/exemplo_bits.py
```

o servidor tem que estar rodando antes de executar os exemplos