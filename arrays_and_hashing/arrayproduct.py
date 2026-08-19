def arrayproduct(nums: list[int]) -> list[int]:
    product = []
    prefix = 1

    for element in nums:
        product.append(prefix)
        prefix *= element 

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        product[i] *= suffix
        suffix *= nums[i]

    return product 


result = arrayproduct([1, 2, 3, 4])
print(result) 