def dfs(image, i, j, visited):
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or visited[i][j] or image[i][j] == 0:
        return 0
    
    visited[i][j] = True
    size = 1

    size += dfs(image, i - 1, j, visited)  # Check up
    size += dfs(image, i + 1, j, visited)  # Check down
    size += dfs(image, i, j - 1, visited)  # Check left
    size += dfs(image, i, j + 1, visited)  # Check right

    return size

def largest_cloud_size(image):
    if not image:
        return 0

    rows, cols = len(image), len(image[0])
    visited = [[False] * cols for _ in range(rows)]
    max_cloud_size = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and image[i][j] == 1:
                cloud_size = dfs(image, i, j, visited)
                max_cloud_size = max(max_cloud_size, cloud_size)

    return max_cloud_size

# Input
M, N = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the size of the largest cloud
result = largest_cloud_size(image)
print(result)
