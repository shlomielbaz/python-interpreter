import sys
from statements import Factory as StatementFactory
from lexer import tokenize
from executer import Executer
from tracer import is_debug

"""

"""
if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        file = open(filename)
        code = file.read()
        file.close()
    except (IndexError, FileNotFoundError):
        raise

    factory = StatementFactory()
    idx = 1
    plan = {}
    for token in tokenize(code):
        if is_debug():
            print(token)
        plan[idx] = factory.create_statement(token.value, token.paramaters)
        idx += 1

    executer = Executer(plan)
    executer.__run__()