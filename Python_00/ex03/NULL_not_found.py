# Write a function that prints the object type of all types of "Null".
#Return 0 if it goes well and 1 in case of error.
#Your function needs to print all types of NULL.


def NULL_not_found(object: any) -> int:
    if type(object).__name__ == 'NoneType':
        print("Nothing : None", type(object))
    elif type(object).__name__ == "float" and object != object:
        print("Cheese : ", type(object))
    elif type(object).__name__ == "int" and object == 0:
        print("Zero : 0", type(object))
    elif type(object).__name__ == "str" and object == "":
        print("Empty : ", type(object))
    elif type(object).__name__ == "bool" and object == False:
        print("Fake : False", type(object))
    else:
        print("Type not Found")
        return 1
    return 0

