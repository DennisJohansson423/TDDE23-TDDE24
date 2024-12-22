def split_rec(message):
    """Splits a string in to two parts recursively. """
    if not message:
        return ("", "")
    char = message[0]
    first_message, second_message = split_rec(message[1:])
    if char.islower() or char in ("_" , "."): 
        first_message = char+first_message
    if char.isupper() or char in ("|" , " "):
        second_message = char+second_message
    return first_message, second_message

def split_it(message):
    """Splits a string in to two parts iterativily. """
    first_message, second_message = "",""
    for char in message:
        if char.islower() or char in ("_" , "."):
            first_message += char
        elif char.isupper() or char in ("|" , " "):
            second_message += char
    return first_message, second_message