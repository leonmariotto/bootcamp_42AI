#!/usr/local/bin/python3.7
import sys

if len(sys.argv) != 3:
  if len(sys.argv) > 3:
    print('InputError : too many arguments', file=sys.stderr)
  print("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
  sys.exit()

try:
  nb1 = int(sys.argv[1])
  nb2 = int(sys.argv[2])
except:
  print('InputError : only number', file=sys.stderr)
  print("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
  sys.exit()

try :
  res = nb1 + nb2
except:
  res = 'ERROR'
print('Sum:               ', res);

try :
  res = nb1 - nb2
except:
  res = 'ERROR'
print('Difference:        ', res);
 
try :
  res = nb1 * nb2
except:
  res = 'ERROR'
print('Product:           ', res);

try :
  res = nb1 / nb2
except:
  res = 'ERROR (div by 0)'
print('Quotient:        ', res);

try :
  res = nb1 % nb2
except:
  res = 'ERROR (modulo by 0)'
print('Remainder:        ', res);
