def all_thing_is_obj(obj: any) -> int:
	"""
	Imprime el tipo del objeto recibido y retorna 42.
	
	Args:
		obj: Cualquier objeto en Python.
		
	Returns:
		int: Retorna siempre el valor 42.
	"""
	type_messages = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: f"{obj} is in the kitchen"
	}
	
	message = type_messages.get(type(obj), "Type not found")
	print(f"{message} : {type(obj)}" if message != "Type not found" else message)
	
	return 42

if __name__ == "__main__":
	# Este bloque se asegura de que no haga nada si es llamado directamente.
	pass