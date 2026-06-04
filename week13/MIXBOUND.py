# Global variable to count recursive calls
recursive_calls = 0

def dfs_knapsack(i, current_weight, current_value, items, max_capacity):
    global recursive_calls
    recursive_calls += 1  # Increment the recursive call count
    
    if i == len(items):
        return current_value if current_weight <= max_capacity else 0

    # Option 1: Don't take the item
    value_without_item = dfs_knapsack(i + 1, current_weight, current_value, items, max_capacity)

    # Option 2: Take the item (if it fits)
    value_with_item = 0
    if current_weight + items[i][0] <= max_capacity:
        value_with_item = dfs_knapsack(i + 1, current_weight + items[i][0], current_value + items[i][1], items, max_capacity)

    # Return the better of the two options
    return max(value_with_item, value_without_item)

# Input reading and testing
items = [(weight1, value1), (weight2, value2), ...]  # List of (weight, value)
max_capacity = 50  # Example capacity
max_value = dfs_knapsack(0, 0, 0, items, max_capacity)

print("Max Value:", max_value)
print("Total Recursive Calls:", recursive_calls)

#####  Prune States Exceeding Capacity

def dfs_knapsack_pruned(i, current_weight, current_value, items, max_capacity):
    global recursive_calls
    recursive_calls += 1
    
    if current_weight > max_capacity:  # Prune if the capacity is exceeded
        return 0

    if i == len(items):
        return current_value

    value_without_item = dfs_knapsack_pruned(i + 1, current_weight, current_value, items, max_capacity)

    value_with_item = 0
    if current_weight + items[i][0] <= max_capacity:
        value_with_item = dfs_knapsack_pruned(i + 1, current_weight + items[i][0], current_value + items[i][1], items, max_capacity)

    return max(value_with_item, value_without_item)



#  Bounding Function

def knapsack_bound(i, current_weight, current_value, items, max_capacity):
    remaining_capacity = max_capacity - current_weight
    bound = current_value
    
    # Sort items by value/weight ratio
    sorted_items = sorted(items[i:], key=lambda x: x[1] / x[0], reverse=True)
    
    for weight, value in sorted_items:
        if weight <= remaining_capacity:
            remaining_capacity -= weight
            bound += value
        else:
            bound += (value / weight) * remaining_capacity
            break
    
    return bound

# Part 9: DFS with Bounding Function



maxV = 0  # Global variable to store the maximum value found so far

def dfs_knapsack_with_bound(i, current_weight, current_value, items, max_capacity):
    global maxV, recursive_calls
    recursive_calls += 1

    if current_weight > max_capacity:
        return

    if i == len(items):
        if current_value > maxV:
            maxV = current_value
        return

    # Bounding function to estimate the optimistic maximum value from this state
    bound = knapsack_bound(i, current_weight, current_value, items, max_capacity)
    
    # Prune if the optimistic bound is less than the best solution found so far
    if bound <= maxV:
        return

    # Recur by either including or excluding the current item
    dfs_knapsack_with_bound(i + 1, current_weight, current_value, items, max_capacity)

    if current_weight + items[i][0] <= max_capacity:
        dfs_knapsack_with_bound(i + 1, current_weight + items[i][0], current_value + items[i][1], items, max_capacity)

# Running the function
items = [(weight1, value1), (weight2, value2), ...]
max_capacity = 50
dfs_knapsack_with_bound(0, 0, 0, items, max_capacity)
print("Max Value:", maxV)
print("Total Recursive Calls:", recursive_calls)
