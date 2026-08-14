def anagram(t:str , s:str) -> bool:
    census = {}
    if len(s) != len(t):
        return False

    for element in s:
        census[element] = census.get(element, 0) + 1

    for element in t:
        if element not in census or census[element] == 0:
            return False
        census[element] -= 1
    return True

result = anagram("hitmo", "mohit")
print(result)