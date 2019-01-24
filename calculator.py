def tokenize(input_string):
    l = []
    li = []
    for i in range(len(input_string)):
        if input_string[i]== " ":
            l.append(''.join(li))
            li = []
        else:
            li.append(input_string[i])
        if i == len(input_string)-1:
            l.append(''.join(li))
    return l
def number_check(string):
    for i in string:
        if ("0123456789".find(i) == -1 and i != "."):
            return False
        elif(string.count(".") != 1 and string.count(".") != 0):
            return False
    return True
def evaluate(expression, stack, binary_operations, unary_operations):
    tokens = tokenize(expression)
    for token in tokens:
        if number_check(token):
            stack.append(float(token))
        elif token in unary_operations.keys():
            stack.append(unary_operations[token](stack.pop()))
        elif token in binary_operations.keys():
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(binary_operations[token](temp2,temp1))
