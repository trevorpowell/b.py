#!/usr/bin/env python3

import sys

def paramToInt(param):
    if '0b' in param:
        param = int(param, 2)
    else:
        param = int(param)
    return param

output = None

if len(sys.argv) >= 4:
    term1 = sys.argv[1]
    operator = sys.argv[2]
    term2 = sys.argv[3]
    term1 = paramToInt(term1)
    term2 = paramToInt(term2)
    if operator == 'left':
        output = term1 << term2
    elif operator == 'right':
        output = term1 >> term2
    elif operator == 'and':
        output = term1 & term2
    elif operator == 'or':
        output = term1 | term2
    elif operator == 'xor':
        output = term1 ^ term2
elif len(sys.argv) == 3:
    operator = sys.argv[1]
    term1 = sys.argv[2]
    term1 = paramToInt(term1)
    if operator == 'not':
        output = ~ term1
elif len(sys.argv) == 2:
    term1 = sys.argv[1]
    output = paramToInt(term1)

if output != None:
    print('Binary: ' + str(bin(output)))
    print('Decimal: ' + str(output))
