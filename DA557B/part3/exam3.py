import pickle

# Template provided by Andreas Nilsson
# https://github.com/andreas-hkr/DA557B_exam3_template/blob/main/exam3.py

def read_drone_file(filename):
    with open(filename, "rb") as f:
        data_set = pickle.load(f)
    return data_set

def read_plant_register(filename):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    data_dict = {}
    for line in data:
        x, y, name = line.split(",")
        data_dict[(int(x), int(y))] = name
    return data_dict

def filter_one_of_each(data_sets):
    return set().union(*data_sets)

def filter_detected_by_several(data_sets):
    ret = set()
    unique_vals = filter_one_of_each(data_sets)
    for val in unique_vals:
        num_contained_in = sum([1 for data_set in data_sets if val in data_set])
        if num_contained_in >= 2:
            ret.add(val)
    return ret

def print_set(data):
    data_list = sorted(list(data))
    for i, thing in enumerate(data_list, start = 1):
        print(f"{str(thing):<15}", end = "")
        if not i % 5:
            print()
    print()
    if i % 5:
        print()

def print_with_translation(data, translation_dict):
    data_list = sorted(list([translation_dict[x] for x in data]))
    for i, thing in enumerate(data_list, start = 1):
        print(f"{str(thing):<15}", end = "")
        if not i % 5:
            print()
    if i % 5:
        print()

def print_results(data_sets, translation_dict):
    for i, data_set in enumerate(data_sets):
        print(f"Plants detected by drone {i}:")
        print_set(data_set)
    
    one_of_each_data = filter_one_of_each(data_sets)
    detected_by_several_data = filter_detected_by_several(data_sets)

    print("List of all detected plants:")
    print_set(one_of_each_data)
    
    if len(detected_by_several_data):
        print("Plants detected by several drones:")
        print_set(detected_by_several_data)
    
    print("Plants listed by name/ID:")
    print_with_translation(one_of_each_data, translation_dict)


def main():
    num_drones = int(input("Enter the number of drones: "))

    drone_file_data = [read_drone_file(f"drone_data_{i}.dat") for i in range(num_drones)]
    translation_dict = read_plant_register("plant_register.txt")

    print_results(drone_file_data, translation_dict)

if __name__ == '__main__':
    main()