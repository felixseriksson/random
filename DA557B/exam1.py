print("----------------------")
print("  What food to order")
print("----------------------")
print()
num_persons = int(input("How many persons are there? "))

def print_summary(num_persons, num_pizzas, num_salads, num_drinks):
    if num_persons == 0 or (num_pizzas == 0 and num_salads == 0 and num_drinks == 0):
        print("No order")
    else:
        total_pizzas_price, total_salads_price, total_drinks_price = num_pizzas * 85, num_salads * 65, num_drinks * 20
        total_price = total_pizzas_price + total_salads_price + total_drinks_price
        vat_price = 0.12*total_price
        delivery_price = 50
        print()
        print("------------------------------")
        print("         Your order:")
        print("------------------------------")
        if num_pizzas >= 1:
            first_part = f"{num_pizzas} pizza(s) x 85 kr:"
            second_part = f"{total_pizzas_price:0.2f} kr"
            space_padding = " "*(30 - len(first_part) - len(second_part))
            print(f"{first_part}{space_padding}{second_part}")
        if num_salads >= 1:
            first_part = f"{num_salads} salad(s) x 65 kr:"
            second_part = f"{total_salads_price:0.2f} kr"
            space_padding = " "*(30 - len(first_part) - len(second_part))
            print(f"{first_part}{space_padding}{second_part}")
        if num_drinks >= 1:
            first_part = f"{num_drinks} drink(s) x 20 kr:"
            second_part = f"{total_drinks_price:0.2f} kr"
            space_padding = " "*(30 - len(first_part) - len(second_part))
            print(f"{first_part}{space_padding}{second_part}")
        print()
        first_part = "VAT (12%)         :"
        second_part = f"{vat_price:0.2f} kr"
        space_padding = " "*(30 - len(first_part) - len(second_part))
        print(f"{first_part}{space_padding}{second_part}")
        first_part = "Delivery          :"
        second_part = f"{delivery_price:0.2f} kr"
        space_padding = " "*(30 - len(first_part) - len(second_part))
        print(f"{first_part}{space_padding}{second_part}")
        print()
        first_part = "Total price       :"
        total_total_price = total_price + vat_price + delivery_price
        second_part = f"{total_total_price:0.2f} kr"
        space_padding = " "*(30 - len(first_part) - len(second_part))
        print(f"{first_part}{space_padding}{second_part}")

def get_person_order(person_idx):
    print()
    print("--------")
    print(f"Person {person_idx}")
    print("--------")

    num_pizza, num_salad, num_drink = 0, 0, 0
    last_person_input = None
    while not last_person_input == 4:
        print(f"1. Add/remove pizza ({num_pizza} selected)")
        print(f"2. Add/remove salad ({num_salad} selected)")
        print(f"3. Add/remove drink ({num_drink} selected)")
        print(f"4. Finish")
        last_person_input = int(input("Choose: "))
        if last_person_input == 1:
            num_pizza = int(not num_pizza)
        elif last_person_input == 2:
            num_salad = int(not num_salad)
        elif last_person_input == 3:
            num_drink = int(not num_drink)
    return num_pizza, num_salad, num_drink

d = dict() # d[person_idx] = (pizzas, salads, drinks)

for person_idx in range(1, num_persons + 1):
    d[person_idx] = get_person_order(person_idx)

total_pizzas = sum([x[0] for x in d.values()])
total_salads = sum([x[1] for x in d.values()])
total_drinks = sum([x[2] for x in d.values()])

print_summary(num_persons, total_pizzas, total_salads, total_drinks)