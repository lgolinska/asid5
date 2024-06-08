import random

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
    print("Items in knapsack:", ", ".join(items_in_knapsack))

def print_items(max_weight, n, items):
    print("MAX WEIGHT OF THE KNAPSACK: ", max_weight)
    print("NUMBER OF ITEMS AVAILABLE: ", n)
    print(f"{'NAME':<48} {'WEIGHT':<8} {'VALUE':<5}")
    for item in items:
        name, weight, value = item
        print(f"{name:<48} {weight:<8} {value:<5}")

def feedback(choice):
    if choice == "knapsack brute force" or choice == "bf":
        feedback_options = ["Unfortunately, the algorithm was too slow and the thieves were captured.",
                            "The algorithm was slow, but fortunately the security guards were asleep, so the thieves managed to escape with the loot."]
    elif choice == "knapsack dynamic programming" or choice == "dp":
        feedback_options = ["Fortunately, the algorithm was fast enough and the thieves managed to escape with the loot.",
                            "The algorithm was quite fast, but unfortunately this time the security guards were alert and the thieves were captured."] 
    feedback = random.choice(feedback_options)
    return print("\n",feedback, sep='')