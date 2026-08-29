def capacity(height : list[int]) -> int:
    max_capacity = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_capacity = max(area, max_capacity)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_capacity

result = capacity([1, 1])
print(result)