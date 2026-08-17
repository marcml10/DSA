def frequency(liste: list[int], frequent: int) -> list[int]:
    census = {}

    for elements in liste:
        census[elements] = census.get(elements, 0) + 1
    sequence = sorted(census, key=census.get, reverse=True)[:frequent] # well the thing is i did not realise we had sorted or else long ago i
    return sequence                                                    # i would have solved it. Its so easy and close, i just did not know the [:frequent] would also work

result = frequency([1,1,1,2,2,3], 2)
print(result) 