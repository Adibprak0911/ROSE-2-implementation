import numpy as np

def flood_fill(matrix, x, y, label, visited):
    rows, cols = matrix.shape
    target_color = matrix[x, y]
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if visited[cx, cy]:
            continue
        
        visited[cx, cy] = True
        matrix[cx, cy] = label
        
        # Check the four adjacent cells (up, down, left, right)
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny]:
                if matrix[nx, ny] == target_color:
                    stack.append((nx, ny))

def label_rooms(matrix):
    visited = np.zeros_like(matrix, dtype=bool)
    label_counter = 1
    
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if not visited[i, j]:
                flood_fill(matrix, i, j, label_counter, visited)
                label_counter += 1
    
    return matrix

# Example 2D array representing an occupancy grid with different colors (1, 2, 3, etc.)
matrix = np.array([
    [1, 1, 0, 0, 2, 2, 2],
    [1, 1, 0, 2, 2, 2, 2],
    [0, 0, 0, 2, 2, 0, 0],
    [3, 3, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 0, 4, 4],
    [3, 3, 3, 3, 0, 4, 4],
])

print("Original Matrix:")
print(matrix)

# Label the rooms (grouped areas of the same color)
labeled_matrix = label_rooms(matrix.copy())

print("\nLabeled Matrix (with rooms labeled as 1, 2, 3, etc.):")
print(labeled_matrix)
