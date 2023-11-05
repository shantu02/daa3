def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Create a list to store the selected items for the solution
    selected_items = []

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Trace back to find the selected items
    i, w = n, W
    while i > 0 and w > 0:
        if K[i][w] != K[i-1][w]:
            selected_items.append(i - 1)
            w -= wt[i - 1]
        i -= 1

    return K[n][W], selected_items

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

max_value, selected_items = knapSack(W, wt, val, n)

print("Maximum Value:", max_value)
print("Selected Items:")
for item in selected_items:
    print(f"Item {item}: Value {val[item]}, Weight {wt[item]}")
