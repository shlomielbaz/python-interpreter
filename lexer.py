from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    paramaters: tuple

def tokenize(code):
    keywords = {'LET', 'IF', 'JUMP', 'CALL', 'RETURN', 'PRINT', }

    patterns = {
        'LET': r'LET (R[0-9]) := (.+)',
        'IF': r'IF (R[0-9]) ([\=\<\>]) (R[0-9]) (.+)',
        'JUMP': r'JUMP (.+)',
        'CALL': r'CALL (.+)',
        'LABEL': r'([A-Za-z0-9]+):',
        'PRINT': r'PRINT (.+)',
        'RETURN': r'RETURN',
    }
    line_num = 1

    for line in code.split('\n'):
        if (re.match(r'^($|\n|\n\r|\r\n)', line)):
            continue

        for (kind, pattern) in patterns.items():
            match = re.match(pattern, line)
            if match:
                if kind == 'LET':
                    if (re.match(r'\d+', match.group(2))):
                        value = 'AssignStatement'
                        parameters = (match.group(1), match.group(2), line_num)
                    else:
                        value = 'AssignCalcStatement'
                        parameters = (match.group(1), match.group(2), line_num)

                elif kind == 'IF':
                    value = "IfStatement"
                    parameters = (match.group(1), match.group(2), match.group(3), match.group(4), line_num)

                elif kind == 'JUMP':
                    value = 'JumpStatement'
                    parameters = (match.group(1), line_num)

                elif kind == 'CALL':
                    value = 'CallStatement'
                    parameters = (match.group(1), line_num)

                elif kind == 'LABEL':
                    value = 'LabelStatement'
                    parameters = (match.group(1), line_num)

                elif kind == 'PRINT':
                    value = 'PrintStatement'
                    parameters = (match.group(1), line_num)

                elif kind == 'RETURN':
                    value = 'ReturnStatement'
                    parameters = (line_num,)

                yield Token(kind, value, line_num, parameters)
                line_num += 1
