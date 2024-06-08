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