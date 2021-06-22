open = ["[","{","("]
close = ["]","}",")"]

def multi_bracket_validation(input):
    brackets = []
    for i in input:
        if i in open:
            brackets.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(brackets) > 0) and
                (open[pos] == brackets[len(brackets)-1])):
                brackets.pop()
            else:
                return False
    if len(brackets) == 0:
        return True
    else:
        return False