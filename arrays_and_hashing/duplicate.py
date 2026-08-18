def duplicate(a) -> bool:
    number=set()

    for num in a:
        if num in number:
            return True
        number.add(num)
    return False

checking = duplicate([1, 2, 3, 1])
print(checking)