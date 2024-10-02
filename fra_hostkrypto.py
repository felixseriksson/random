import itertools

words_a = ["Sorla","Stall","Eldar","Gnagt","Knall","Gamla","Stark","Slira","Enigt","Åtala","Koral","Samla","Stiga","Ålder","Klaga","Åtaga","Snart","Sadla"]
words_b = ["Saiat", "Elalk", "Godga", "Ktrel", "Ånmrr"]
f = (lambda x, i: set([y[i] for y in x]))
actual_sets = [f(words_b, i) for i in range(5)]

for comb in itertools.combinations(words_a, 5):
    comb_sets = [f(comb, i) for i in range(5)]
    if comb_sets == actual_sets:
        print(comb)