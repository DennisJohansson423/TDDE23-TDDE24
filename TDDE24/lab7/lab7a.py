def match(seq, pattern):
  """
  Returns whether given sequence matches the given pattern.
  """
  
  if not pattern:
    return not seq
  elif not isinstance(seq, list) and not isinstance(pattern, list):
    return False
    #Vi kan råka indexera åren vilket är siffror vilket inte går
  elif pattern[0] == '--':
    if match(seq, pattern[1:]):
      return True
    elif not seq:
      return False
    else:
      return match(seq[1:], pattern)
  elif not seq:
    return False
  elif seq[0] == pattern[0]:
    return match(seq[1:], pattern[1:])
  elif pattern[0] == '&':
    return match(seq[1:], pattern[1:])
  elif isinstance(seq, list) and isinstance(pattern, list):
    if match(seq[0], pattern[0]):
      return match(seq[1:], pattern[1:])
  else:

    return False

#The given database
db = [[['författare', ['john', 'zelle']],
       [
         'titel',
         [
           'python', 'programming', 'an', 'introduction', 'to', 'computer',
           'science'
         ]
       ], ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']], ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']], ['år', 2011]],
      [['författare', ['john', 'zelle']],
       [
         'titel',
         [
           'data', 'structures', 'and', 'algorithms', 'using', 'python', 'and',
           'c++'
         ]
       ], ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']], ['år', 1993]]]


def search(pattern, db):
  """ 
  Gose through the db Recursively and calls the function match.
  If the functions returns true the db sequence is insert to the list.
  """
  if not db:
    return []
  seq = db[0]
  search_result = search(pattern, db[1:])
  if match(seq, pattern):
    #Uses insert becuse add the sequence to the front of list
    search_result.insert(0,seq)
  return search_result




patterns = [
  ["--"], #gets the complete database
  
  ["&"], 
  
  ['--', ['titel', ['&', '&']], '--'],
  
  ['--', ['år', 2042], '--'],
  
  [['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']],
  
  [['författare', ['john', 'zelle']],['titel',['python', 'programming', 'an','introduction', 'to', 'computer','science']], ['år', 2010]],
  
  [['författare', ['&', '&']],"--"],
  
  ['--', ['år', 2010]],
  
  [['&', ['&', '&']],['&', ['&', '&', '&']], ['&', '&']] #checks that & works corekt
]


expecteds = [
  (db),
  
  ([]),
  
  ([[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]),
  
  ([]),
  
  ([[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
  'to', 'computer', 'science']], ['år', 2010]],[['författare', ['john', 'zelle']], ['titel',
   ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]]]),
  
  ([[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
  'to', 'computer', 'science']], ['år', 2010]]]),
  
  
  ([[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], ['år', 2010]], [['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]], [['författare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]], [['författare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['år', 1993]]]),
  
  ([[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
  'to', 'computer', 'science']], ['år', 2010]]]),
  
  ( [[['författare', ['anders', 'haraldsson']],['titel', ['programmering', 'i', 'lisp']], ['år', 1993]]])
  
]


def test_search():
  """ 
  Tests the search function.
  """
  for pattern, expected in zip(patterns, expecteds):
    assert (search(pattern,db) == expected), "Expected {} got {} by using pattern {}".format(expected,str(search(pattern,db)),pattern)

  print("The code passed all the test")
    
  


test_search()
