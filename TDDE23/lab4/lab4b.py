def or_func(arg1,arg2):
    """ Bollean operation OR """
    if arg1 == "true":
        return "true"
    elif arg2 == "true":
        return "true"
    return "false"

def and_func(arg1,arg2):
    """ Bollean operation AND """
    if arg1 == arg2 == "true":
        return "true"
    return "false"

def not_func(arg):
    """ Bollean operation NOT """
    if arg == "true":
        return "false"
    return "true"

def interpret(exp,inter):
    """ Returns true or false if the entire expression is true oe false in this particular interpret"""
    if isinstance(exp,str):
        if exp in inter:
            return inter[exp]
        return exp
    if len(exp) == 3:
        if exp[1] == "AND":
            return and_func(interpret(exp[0],inter),interpret(exp[2],inter))
        elif exp[1] == "OR":
            return or_func(interpret(exp[0],inter),interpret(exp[2],inter))
    elif len(exp) == 2:
        return not_func(interpret(exp[1],inter))
