# Template provided by Andreas Nilsson
# https://github.com/andreas-hkr/DA557B_exam2_template/blob/main/exam2.py

def read_file(filename):
    with open(filename) as f:
        data = [int(x) for x in [line.strip() for line in f.readlines()] if x != "---"]
    return data

def write_file(filename, data):
    with open(filename, "w") as f:
        f.write("\n".join([str(x) for x in data]))

def filter_numbers(data, keep_even):
    return [x for x in data if x % 2 != int(keep_even)]

def print_results(percentages):
    # Percentage of numbers remembered:  91.00%
    # --> odd numbers remembered    :  88.89%
    # --> even numbers remembered   :  93.48%
    p1, p2, p3 = percentages
    print(f"Percentage of numbers remembered: {p1:>6.2f}%")
    print(f"  --> odd numbers remembered    : {p2:>6.2f}%")
    print(f"  --> even numbers remembered   : {p3:>6.2f}%")

def main():
    print()
    print("Enter the path to the following files:")
    correct_file_path = input("CORRECT DATA : ")
    test_file_path = input("TEST DATA    : ")
    print()

    try:
        correct_file_data = read_file(correct_file_path)
    except FileNotFoundError:
        print(f"ERROR: The specified file '{correct_file_path}' does not exist.")
        print()
        exit(0)
    try:
        test_file_data = read_file(test_file_path)
    except FileNotFoundError:
        print(f"ERROR: The specified file '{test_file_path}' does not exist.")
        print()
        exit(0)
    
    correct_odd_data, correct_even_data = filter_numbers(correct_file_data, False), filter_numbers(correct_file_data, True)
    test_odd_data, test_even_data = filter_numbers(test_file_data, False), filter_numbers(test_file_data, True)
    
    write_file("odd_numbers.txt", test_odd_data)
    write_file("even_numbers.txt", test_even_data)

    p = (len(test_file_data) / len(correct_file_data) * 100, len(test_odd_data) / len(correct_odd_data) * 100, len(test_even_data) / len(correct_even_data) * 100)

    print_results(p)

if __name__ == '__main__':
    main()