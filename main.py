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