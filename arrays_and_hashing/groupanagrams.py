def group_anagram(str:list[str])-> list[list[str]]:
    census = {}
    for elements in str:
        messed = "".join(sorted(elements))
        if messed in census:
            census[messed].append(elements)
        else:
            census[messed] = [elements]


    return list(census.values())

result = group_anagram(["eat","tea","tan","ate","nat","bat"])
print(result)

