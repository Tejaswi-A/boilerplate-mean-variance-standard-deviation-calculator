import numpy as np

def calculate(list_input):
    # Validate input length
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to a 3x3 numpy array
    matrix = np.array(list_input).reshape(3, 3)

    # Debugging output
    print("Matrix:\n", matrix)
    
    # Perform calculations
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]
    }

    # Debugging output
    print("Calculations Dictionary Created Successfully")

    return calculations  # Ensure proper indentation

# Testing the function directly from this script
if __name__ == "__main__":
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("Final Result:\n", result)
