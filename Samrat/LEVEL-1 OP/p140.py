def print_subsets(n):
    total = 1 << n
    for mask in range(total):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(i+1)
        print(subset)
n=int(input())
print_subsets(n)
