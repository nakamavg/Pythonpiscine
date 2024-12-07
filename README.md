# Pythonpiscine
## Index
- [Ex00](#ex00)
## Ex00

### In this exercise, we learn about Arrays, Tuples, Sets, and Dicts.

### Arrays

- Arrays in Python can have their values changed by accessing them with indexes.
```python
hola[1]
```

### Tuples
-  Tuples are inmutables  and cant change values for this module i change the tuple wit this code
```python
def change_tuple(tupletochange,index, value):
	'''Change the value of a tuple at a given index (tupletochange) -> tuple'''
	tupletochange = (tupletochange[index], value)
	return tupletochange
```
### Sets
- Sets in Python are unordered collections of unique elements. This means that a set cannot have duplicate elements.
- To remove a duplicate element from a set, you can use the `remove()` method.
- Sets in Python are unordered collections of unique elements. This means that the order of elements in a set is not guaranteed and can vary each time you access the set. The reason for this is that sets use a hash-based implementation, which allows for efficient membership testing and element uniqueness, but does not preserve the order of elements.
### Dict 

- A dictionary in Python is a data structure that stores key-value pairs. Each element in a dictionary has a unique key associated with a value. Dictionaries are very useful when you need to store and access data efficiently using a custom key instead of a numeric index.

- ```python
	# Crear un diccionario
		person = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
				}

	# Cambiar el valor de un elemento
	person["edad"] = 26

	print(person)
	```
- ```output
	{
		"nombre": "Juan",
		"edad": 26,
		"ciudad": "Madrid"
	}
	```

[subir](#pythonpiscine)
## Ex02

- Aprender que es __main__
	- en este caso nos sirve para que si es llamado al .py no haga nada
	```python 
	if __name__ == "__main__":
   
    pass
	```
- La funcion type te devuelve el tipo del objeto , aunque la funcion type
es demasiado poderosa y puede usarse para crear clases y metaprogramacion, en la propia documentacion nos hablan de la funcion
- isInstance(obj,string):
	- Recibe un objeto y devuelve un booleano comparandolo con lo quue le pasamos por el segundo argumento.
### ex 03 NULL not found

- Este ejercicio nos enseña las diferencias entre:
- ```python
	1 None
	bool false
	emptystring=""
	float(NaN)
	int 0
	```
- None
	```python
	if variable is None:
    print("La variable no tiene valor asignado")
	else:
    print("La variable tiene un valor")
	```
- float(NaN)
```python
import math

if math.isnan(variable):
    print("La variable es NaN")
else:
    print("La variable no es NaN")
```
- el 0 int y el false
- ambos se pueden consegir con 
```python
Capturar ambos	if not variable:
Distinguir False	if variable is False:
Distinguir 0	if variable == 0:
Capturar solo ambos	if variable in (False, 0):
```
### ex04 parserarguments

```python
	# Ejemplo de parseo de argumentos en Python
	import argparse
	# 1
	parser = argparse.ArgumentParser()
	# 2
	parser.add_argument("patata" ,type=int ,help="el tipo de dato")
	#3
	args = parser.parse_args()
	print(args.patata+args.patata)
```
- 1 Creamos el objeto parser
- 2 Añadimos con el metodo `add__argument` el nombre , el tipo , y una pequeña descripicion cuando hacemos -h o -help
```output
➜  ex04 git:(main) ✗ python3 Ejemplosparseo.py -h
usage: Ejemplosparseo.py [-h] patata

positional arguments:
  patata      el tipo de dato

options:
  -h, --help  show this help message and exit
```
- Con esto tambien conseguimos parsear el dato y que nos retorno el error si el tipo no es el deseado
```output
➜  ex04 git:(main) ✗ python3 Ejemplosparseo.py patata
usage: Ejemplosparseo.py [-h] patata
Ejemplosparseo.py: error: argument patata: invalid int value: 'patata'
```