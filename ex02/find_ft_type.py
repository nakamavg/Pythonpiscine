def all_thing_is_obj(obj: any) -> int:
    """
    Imprime el tipo del objeto recibido y retorna 42.
    
    Args:
        obj: Cualquier objeto en Python.
        
    Returns:
        int: Retorna siempre el valor 42.
    """
    if isinstance(obj, list):
        print(f"List : {type(obj)}")
    elif isinstance(obj, tuple):
        print(f"Tuple : {type(obj)}")
    elif isinstance(obj, set):
        print(f"Set : {type(obj)}")
    elif isinstance(obj, dict):
        print(f"Dict : {type(obj)}")
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42


if __name__ == "__main__":
    # Este bloque se asegura de que no haga nada si es llamado directamente.
    pass
