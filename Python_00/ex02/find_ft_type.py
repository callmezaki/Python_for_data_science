
# Write a function that prints the object types and returns 42

def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print(object, "is in the kitchen :",type(object))
    else:
        print(type(object).__name__, ":",type(object))
    return  42

