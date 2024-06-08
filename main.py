from knapsack import knapsack_brute_force

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

def knapsack_dynamic_programming():
    pass

if __name__ == '__main__':
    filename = 'data.txt'
    max_weight, n, items = read_data_from_file(filename)

    while (True):
        choice=input("action> ").strip().lower()
        if choice == "help":
            print("help")
        elif choice == "knapsack brute force" or choice == "bf":
            print(knapsack_brute_force(max_weight, n, items))
        elif choice == "knapsack dynamic programming" or choice == "dp":
            knapsack_dynamic_programming()
        elif choice == "exit":
            break
        else:
            print("To view possible actions type: Help")