def change_tuple(tupletochange,index, value):
	'''Change the value of a tuple at a given index (tupletochange) -> tuple'''
	tupletochange = (tupletochange[index], value)
	return tupletochange
def pop_and_add_set(settochange, value):
	'''Remove a value from a set and add a new value to it (settochange) -> set'''
	settochange.discard("tutu!")
	settochange.add(value)
	
	return settochange
def change_value_dict(dicttochange, key, value):
	'''Change the value of a dictionary at a given key (dicttochange) -> dict'''
	dicttochange[key] = value