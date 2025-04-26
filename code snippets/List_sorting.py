lst = [2, 4, 5, 7, 1, 6, 8, 333, 23]
print(f"before sorting = {lst}")

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]  # Swap elements

print(f"after sorting = {lst}")

