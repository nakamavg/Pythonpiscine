import math
def obtener_nombre_variable(obj):
    for nombre, valor in globals().items():
        if valor is obj:
            return str(nombre)
    return None

def NULL_not_found(object: any) -> int:
    datatype = str(type(object))
    nameobj = str(obtener_nombre_variable(object))
    
    if object is None:
        print("Nothing: None" + datatype)
        return 0
    elif object == "":
        print("Empty: Empty "+ datatype)
        return 0
    elif object is False:
        print(nameobj+": False " + datatype)
        return 0
    elif object == 0:
        print(nameobj+ ": 0 " + datatype)
        return 0
    elif datatype=="<class 'float'>" and math.isnan(object):
        print(nameobj+ ": NaN " + datatype)
        return 0
    else:
        print("Type not found")
        return 1