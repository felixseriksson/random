from itertools import permutations, combinations_with_replacement, product, combinations
from more_itertools import distinct_permutations, distinct_combinations

ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}

def eval(expression):
    stack = []

    for token in expression:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(token)

    return stack.pop()

def is_valid(sequence):
    count_nums = 0
    for token in sequence:
        if not token:
            count_nums -= 1
            if count_nums < 1:
                return False
        else:
            count_nums += 1
    return True

def valid_sequences(num_count):
    base = (True,) * num_count + (False,) * (num_count - 1)
    perms = distinct_permutations(base)
    for sequence in perms:
        if is_valid(sequence):
            yield sequence

def distinct_ordered_combinations(iterable, r):
    seen = set()
    for combination in combinations_with_replacement(iterable, r):
        for permutation in permutations(combination):
            if permutation not in seen:
                yield permutation
                seen.add(permutation)

def generate_sequences(numbers, operators):
    l = len(numbers)
    for sequence in valid_sequences(l):
        for nums, ops in product(distinct_permutations(numbers), distinct_ordered_combinations(operators, l - 1,)):
            nums = iter(nums)
            ops = iter(ops)
            yield tuple(next(nums) if token else next(ops) for token in sequence)

numbers = [int(x) for x in input("Enter numbers: ").split()]
target = int(input("Enter target: "))
operators = ["+", "-", "*", "/"]

res = set()

for s in range(1, 7):
    for choice in distinct_combinations(numbers, r = s):
        for sequence in generate_sequences(choice, operators):
            try:
                evalres = eval(sequence)
            except:
                pass
            if evalres == target:
                res.add(sequence)

for sequence in res:
    print(sequence)