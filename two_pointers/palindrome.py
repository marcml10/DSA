def palindrome(str) -> bool:
    left = 0 
    right = len(str) - 1

    while left :
        if (not str[left].isalnum()): 
            left +=1
        elif (not str[left].isalnum()):
            right-=1

        else:
            if str[left].lower() != str[right].lower:
                return False
            left += 1
            right -=1
    return True

print(palindrome("A man, a plan, a canal: Panama"))
