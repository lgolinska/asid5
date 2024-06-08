def knapsack_brute_force(c, n, items):
    fmax = 0
    for i in range(1, pow(2,n)):
        option = [int(bit) for bit in bin(i)[2:].zfill(n)]
        w_sum = 0
        for j in range(len(items)):
            if option[j] == 1:
                w_sum += items[j][1]
        if w_sum <= c:
            value_sum = 0
            for k in range(len(items)):
                if option[k] == 1:
                    value_sum += items[k][2]
            if value_sum > fmax:
                fmax = value_sum
                best_option = option
    return fmax, best_option

def knapsack_dynamic_programming(c, n, items):
    V = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        _, item_weight, item_value = items[i - 1]
        for j in range(c + 1):
            if item_weight > j:
                V[i][j] = V[i - 1][j]
            else:
                V[i][j] = max(V[i - 1][j], V[i - 1][j - item_weight] + item_value)
    fmax = V[n][c]
    best_option = [0] * n
    j = c
    for i in range(n, 0, -1):
        if V[i][j] != V[i - 1][j]:
            best_option[i - 1] = 1
            j -= items[i - 1][1]
    return fmax, best_option