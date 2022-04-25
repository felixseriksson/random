from itertools import permutations, combinations_with_replacement, product

ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}

def eval(expression):
  tokens = expression.split()
  stack = []

  for token in tokens:
    if token in ops:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(int(token))

  return stack.pop()

numbers = input("Enter numbers: ").split()
target = int(input("Enter target: "))
operators = ["+", "-", "*", "/"]

res = set()
for num in numbers:
    if int(num) == target:
        res.add(num)

for s in range(2, 7):
    for permutation in permutations(numbers, r = s):
        a, b, *rest = permutation
        operations = product(operators, repeat = s-1)
        for permutation in operations:
            expression = zip([a+ " " + b, *rest], permutation)
            rpn = "".join(variable + " " + operator + " " for variable, operator in expression)
            rpn = rpn[:-1]
            if eval(rpn) == target:
                res.add(rpn)
    if res:
        for r in res:
            print(r)
        break
else:
    print("None found")

# Input
# 100 25 5 1 3 8
# 913
# Erroneously returns "None found"
# despite the possible solution
# 100 25 + 5 + 8 1 - * 3 +