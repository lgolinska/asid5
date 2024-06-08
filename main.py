from knapsack import knapsack_brute_force, knapsack_dynamic_programming
from functions import read_data_from_file, printing_result, print_items

if __name__ == '__main__':
    filename = 'data.txt'
    max_weight, n, items = read_data_from_file(filename)

    while (True):
        choice=input("action> ").strip().lower()
        if choice == "help":
           print("""Help                            Show this message
Print items                     Print the maximum weight of the knapsack, the number of items available and list of items
Knapsack brute force            Run knapsack brute force algorithm
Knapsack dynamic programming    Run knapsack dynamic programming algorithm
Exit                            Exits the program (same as ctrl+D)""")
        elif choice == "knapsack brute force" or choice == "bf":
            printing_result(knapsack_brute_force(max_weight, n, items), items)
        elif choice == "knapsack dynamic programming" or choice == "dp":
            printing_result(knapsack_dynamic_programming(max_weight, n, items), items)
        elif choice == "print items" or choice == "print":
            print_items(max_weight, n, items)
        elif choice == "exit":
            break
        else:
            print("To view possible actions type: Help")