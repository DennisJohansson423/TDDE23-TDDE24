from calc import *

def exec_output(statement, table):
  """Prints out the statement that is given and checks if its a varibal"""
  variable = output_expression(statement)
  if is_variable(variable):
    variable = output_expression(statement)
    value = table[variable]
    print(f"{variable} = {value}")
  else:
    print(eval_expression(output_expression(statement), table))


def eval_condition(statement, table):
  """
  Evaluate a if statement. If true returns the true branch else returns the 
  false branch if  exists else false.
  """
  left = eval_expression(condition_left(statement), table)
  right = eval_expression(condition_right(statement), table)
  operator = condition_operator(statement)

  if operator == ">":
    return left > right
  elif operator == "<":
    return left < right
  elif operator == "=":
    return left == right
  else:
    raise Exception("Not a valid condoper")
  
  
def exec_selection(statement, table):
  """Returns the true branch if true else the false branch"""
  if eval_condition(selection_condition(statement), table):
      return exec_statement(selection_true_branch(statement), table)
  elif selection_has_false_branch(statement):
      return exec_statement(selection_false_branch(statement), table)
  return table
    

def eval_binaryexpr(statement, table):
  """
     Findes the values used for binary functions and the returns the value 
     of the functions by calling binary_calculater
  """
  left = eval_expression(binaryexpr_left(statement), table)
  right = eval_expression(binaryexpr_right(statement), table)
  operator = binaryexpr_operator(statement)

  if operator == "+":
    return left + right
  elif operator == "-":
    return left - right
  elif operator == "*":
    return left * right
  elif operator == "/":
    return left / right
  raise Exception("Not a vaild binary")


def exec_assignemnt(seq, table):
  """Takes a varibal and adds it to the varibal dictory and returns it"""
  var = assignment_variable(seq)
  exp = eval_expression(assignment_expression(seq), table)
  copy_table = table.copy()
  copy_table[var] = exp
  return copy_table


def exec_input(seq, table):
  """
  Takes a varibel as an input, then an other input for the value,
  then returns a copy of the varibale table with the new value 
  """
  copy_table = table.copy()
  var = input_variable(seq)
  value = int(input(f"Enter value for {var}: "))
  copy_table[var] = value
  return copy_table


def exec_repetition(seq, table):
  """
  Checks if the break statement throung if_funk then evaluates the args 
  that are given, then checks break_statement
  """
  while eval_condition(repetition_condition(seq), table):
    table = exec_statements(repetition_statements(seq), table)
  return table


def eval_constant(program):
  """Returns the constant"""
  return program


def eval_variable(program,table):
  """Returns the variable"""
  return table[program]


def eval_expression(program, table):
  """Returns the value of an evaluation function"""
  if is_binaryexpr(program):
    return eval_binaryexpr(program, table)
  elif is_variable(program):
    return eval_variable(program,table)
  elif is_constant(program):
    return eval_constant(program)


def exec_statement(program, table):
  """
  Finds which type of operation the program is and calls the correct
  funktions. All the functions returns a table that are used for uppdateing 
  the varibale table 
  """
  if is_repetition(program):
    return exec_repetition(program, table)
  elif is_input(program):
    return exec_input(program, table)
  elif is_output(program):
    exec_output(program, table)
    return table
  elif is_assignment(program):
    return exec_assignemnt(program, table)
  elif is_selection(program):
     return exec_selection(program, table)
  else:
    raise Exception("Not a valid statement")


def exec_statements(program, table):
  """
  Takes a list of statments and a table and returns a new table with,
  based on the statments
  """
  if empty_statements(program):
    return table
  table = exec_statement(first_statement(program), table)
  return exec_statements(rest_statements(program), table)


def exec_program(program, table=None):
  """
  Checks if the given args are vaild and starts executs statements, 
  returns an update varibal table
  """
  if is_program(program):
    if not table: table = {} 
    return exec_statements(program_statements(program), table)
  else:
    raise Exception("Not a vaild program")



calc1 = ['calc', ['set', 'a', 5], ['print', 'a']]


calc2 = ['calc', ['set', 'x', 7],
            ['set', 'y', 12],
            ['set', 'z', ['x', '+', 'y']],
            ['print', 'z']]


calc3 = ['calc', ['read', 'p1'],
            ['set', 'p2', 47],
            ['set', 'p3', 179],
            ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],
            ['print', 'result']]
calc4 = ['calc', ['read', 'n'],
            ['set', 'sum', 0],
            ['while', ['n', '>', 0],
            ['set', 'sum', ['sum', '+', 'n']],
            ['set', 'n', ['n', '-', 1]]],
            ['print', 'sum']]


calcfib = ['calc', ['read', 'n'],
          ['set', 'n1', 0],
          ['set', 'n2', 1],
          ['set','sum',1],
          ['if',['n','=',1],['set','nth',1]],
          
          ['while', ['sum', '<', 'n'],
          ['set', 'nth', ['n1', '+', 'n2']],
          ['set', 'n1', 'n2'],
          ['set','n2','nth'],
          ['set','sum',['sum','+',1]]],
          ['print', 'nth']]


calc5  = ['calc', ['read', 'n'],
            ['set', 'sum', 0],
            ['while', ['n', '>', 0],
            ['set', 'sum', ['sum', '+', 'n']],
            ['set', 'n', ['n', '-', 1]]],
            ['print', 'sum']]


calcfib = ['calc', ['read', 'n'],
          ['set', 'n1', 0],
          ['set', 'n2', 1],
          ['set','sum',1],
          ['if',['n','=',1],['set','nth',1]],
          
          ['while', ['sum', '<', 'n'],
          ['set', 'nth', ['n1', '+', 'n2']],
          ['set', 'n1', 'n2'],
          ['set','n2','nth'],
          ['set','sum',['sum','+',1]]],
          ['print', 'nth']]


calc2 = ["calc",
        ["read", "n"],
        ["set", "sum", 0],
        ["while",
            ["n", ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"],]


#cal = ["calc",["read","n"],["set", "sum", 0],["set", "sum", ["sum", "+", "n"]],["set", "n", ["n", "-", 1]],["print", "sum"],]
#print(exec_program(calc2))