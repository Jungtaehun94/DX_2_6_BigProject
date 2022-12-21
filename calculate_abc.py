import numpy as np
def calculate_abc(df, target_sum):
    # Calculate the sum of the values in the '소방공무원_22' column
    sum_df = df['dpt'].sum()
    
    # Calculate the proportions of each element in the '소방공무원_22' column
    proportions = df['dpt'] / sum_df
    
    # Calculate the value of each element in the list [a, b, c]
    abc = proportions * target_sum
    
    # Round each element in the list [a, b, c] to the nearest integer
    a, b, c = np.round(abc).astype(int)
    
    # Adjust the values of a, b, and c so that they sum up to the target sum
    diff = target_sum - (a + b + c)
    if diff != 0:
        # Find the element with the largest fractional part
        largest = np.argmax(abc - np.floor(abc))
        if diff > 0:
            # Increase the value of the element with the largest fractional part
            abc[largest] += diff
        else:
            # Decrease the value of the element with the largest fractional part
            abc[largest] -= diff
    
    # Round the final values of a, b, and c to the nearest integer
    a, b, c = np.round(abc).astype(int)
    
    return a, b, c