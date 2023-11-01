def check_palindrome(text):
    l, r = 0, len(text)-1
    while l<r:
        if text[l] == text[r]:
            l += 1
            r -= 1
        else:
            return False
    return True