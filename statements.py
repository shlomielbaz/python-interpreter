import re
from tracer import is_debug


def expr(left, op, right):
    # if is_debug():
    #     print('expretion: %s %s, %s, %s, %s' % (left, op, right, type(left), type(right)))
    if op == '+':
        return left + right
    elif op == '*':
        return left * right
    elif op == '-':
        return left - right
    elif op == '=':
        return left == right
    elif op == '>':
        return left > right
    elif op == '<':
        return left < right

    return None


class Statement:
    labels = {}
    return_line = -1
    registers = {}

    def __init__(self, line_no, label=None):
        self.line_no = line_no

        if label != None:
            self.labels[label] = line_no

    def __next__(self):
        return None

    def __by_label__(self, label):
        return self.labels[label]


class AssignStatement(Statement):
    def __init__(self, key, value, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s, %s' % ('AssignStatement', key, value, line_no))
        super().__init__(line_no)
        self.key = key
        self.value = value

    def __next__(self):
        self.registers[self.key] = int(self.value)
        return (self.line_no + 1)


class AssignCalcStatement(Statement):
    def __init__(self, key, value, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s, %s' % ('AssignCalcStatement', key, value, line_no))
        super().__init__(line_no)
        self.key = key
        self.value = value

    def __next__(self):
        matches = re.match(r'([^\W]+) ([\+\-\*]) (\d+)', self.value)

        left = matches.group(1)
        left = int(self.registers[left] if left.startswith('R') else left)

        op = matches.group(2)

        right = matches.group(3)
        right = int(self.registers[right] if right.startswith('R') else right)

        self.registers[self.key] = expr(left, op, right)
        return (self.line_no + 1)


class JumpStatement(Statement):
    def __init__(self, label, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s' % ('JumpStatement', label, line_no))
        super().__init__(line_no)
        self.label = label

    def __next__(self):
        return self.__by_label__(self.label)


class CallStatement(JumpStatement):
    def __init__(self, label, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s' % ('CallStatement', label, line_no))
        super().__init__(label, line_no)

    def __next__(self):
        self.return_line = (self.line_no + 1)
        return self.__by_label__(self.label)


class LabelStatement(Statement):
    table = {}

    def __init__(self, label, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s' % ('LabelStatement', label, line_no))
        super().__init__(line_no, label)
        self.label = label
        self.table[self.label] = line_no

    def __next__(self):
        return (self.line_no + 1)

    def get_line_by_label(self, label):
        print(self)
        return self.table[label]


class IfStatement(Statement):
    def __init__(self, k1, op, k2, label, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s, %s, %s, %s' % ('IfStatement', k1, op, k2, label, line_no))
        super().__init__(line_no)
        self.k1 = k1
        self.op = op
        self.k2 = k2
        self.label = label

    def __next__(self):
        if expr(self.registers[self.k1], self.op, self.registers[self.k2]):
            return self.__by_label__(self.label) + 1
        return (self.line_no + 1)


class ReturnStatement(Statement):
    def __init__(self, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s' % ('ReturnStatement', line_no))
        super().__init__(line_no)

    def __next__(self):
        next = self.return_line;
        self.return_line = -1
        return (next + 1)


class PrintStatement(Statement):
    def __init__(self, key, line_no):
        if is_debug():
            print('init class: %s, with parameters: %s, %s' % ('PrintStatement', key, line_no))
        super().__init__(line_no)
        self.key = key

    def __next__(self):
        print(self.registers[self.key])
        return (self.line_no + 1)


class Factory():
    """
    create_statement - gets statement type and parameters and create a statement object from it
    """

    def create_statement(self, type, parameters):
        return globals()[type](*parameters)
