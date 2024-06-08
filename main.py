from knapsack import knapsack_brute_force, knapsack_dynamic_programming

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        max_weight = int(file.readline().strip())
        n = int(file.readline().strip())
        items = []
        
        for i in range(n):
            line = file.readline().strip()
            name, weight, value = line.split(',')
            items.append((name, int(weight), int(value)))
        
        items = tuple(items)
    return max_weight, n, items

def printing_result(function, items):
    fmax, best_option = function
    items_in_knapsack = []
    for i in range(len(items)):
        if best_option[i] == 1:
            items_in_knapsack.append(items[i][0])
    print(f"Max value: {fmax}")
    print("Items in knapsack:", *items_in_knapsack)

if __name__ == '__main__':
    filename = 'data.txt'
    max_weight, n, items = read_data_from_file(filename)

    while (True):
        choice=input("action> ").strip().lower()
        if choice == "help":
            print("help")
        elif choice == "knapsack brute force" or choice == "bf":
            printing_result(knapsack_brute_force(max_weight, n, items), items)
        elif choice == "knapsack dynamic programming" or choice == "dp":
            printing_result(knapsack_dynamic_programming(max_weight, n, items), items)
        elif choice == "exit":
            break
        else:
            print("To view possible actions type: Help")