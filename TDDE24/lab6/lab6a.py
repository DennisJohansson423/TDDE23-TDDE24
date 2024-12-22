
from calc import *



def eval_find_constant(left, right):
  """Returns the complete value of the seqens"""
  left = eval_find_statement_type(left)
  right = eval_find_statement_type(right)
  return left, right


def eval_print_funk(statement):
  """
  Prints out the given expresion 
  """
  print(output_expression(statement))


def condoper_funcs(operator, left, right):
  """Evaluate a condoper function based on the args"""
  funcs = {">": exec_greater_then_func, "<": exec_smaller_then_func, "=": exec_equal_func}
  return funcs[operator](left, right)


def exec_greater_then_func(left, right):
  """Returns true if left lager then right"""
  return left > right


def exec_smaller_then_func(left, right):
  """Returns true if left smaller then right"""
  return left < right


def exec_equal_func(left, right):
  """Returns true if left equals right"""
  return left == right


def exec_addition(left, right):
  """Returns left + right """
  return left + right


def exec_subtraktion(left, right):
  """Returns left - right """
  return left - right


def exec_multiplation(left, right):
  """Returns left * right """
  return left * right


def exec_divison(left, right):
  """Returns left / right """
  return left / right


def eval_binary_calculater(operator, left, right):
  """Returns the value of the binary function that matchs the input values"""
  funcs = {"+": exec_addition, "-": exec_subtraktion, "*": exec_multiplation, "/": exec_divison}
  return funcs[operator](left, right)


def eval_binary_func(statment):
  """
     Findes the values used for binary functions and the returns the value 
     of the functions by calling binary_calculater
  """
  operator = binaryexpr_operator(statment)
  left = binaryexpr_left(statment)
  right = binaryexpr_right(statment)
  left, right = eval_find_constant(left, right)
  return eval_binary_calculater(operator, left, right)


def eval_if_funk(statement, has_false_statment):
  """
  Evaluate a if statement. If true returns the true branch else returns the 
  false branch if  exists else false.
  """
  condition = selection_condition(statement)
  operator = condition_operator(condition)
  if is_condoper(operator):
    left = condition_left(condition)
    right = condition_right(condition)
    left, right = eval_find_constant(left, right)
    if condoper_funcs(operator, left, right):
      return eval_find_statement_type(selection_true_branch(statement))
    elif has_false_statment:
      return eval_find_statement_type(selection_false_branch(statement))
    return False




def eval_find_statement_type(program):
  """
  Checks which type of statement the input and calls the corockt function
  """
  if is_selection(program):
    return eval_if_funk(program, selection_has_false_branch(program))
  elif is_output(program):
    eval_print_funk(program)
  elif is_binaryexpr(program):
    return eval_binary_func(program)
  elif is_constant(program):
    return program
  else:
    raise ValueError

def exec_statements(program):
  print(program)
  if is_statements(program):
    eval_find_statement_type(first_statement(program))
    exec_statements(rest_statements(program))
  elif program != []:
    raise ValueError



def exec_program(program):
  if is_program(program):
    return exec_statements(program_statements(program))
  else:
    return False


#calc2 = ['calc', {},[['print',5] ]]
#calc2 = ['calc', ['if', [1, '=', 0], ['print', 2], ['print', 4]]]
#calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
#calc2 = ['calc',[2,'?',2]]
#calc2 = ['calc',[a,'+',2]]
#exec_program(calc2)
