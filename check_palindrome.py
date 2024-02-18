from collections import deque


def check_palindrome(word):
    word = word.lower().replace(" ", "")
    d = deque(word)
    for i in range(len(word) // 2):
        left = d.popleft()
        right = d.pop()
        if left != right:
            return False
    return True


if __name__ == "__main__":
    assert check_palindrome("abcdcba") == True
    assert check_palindrome("abcddcba") == True
    assert check_palindrome("aba") == True
    assert check_palindrome("abab") == False

    assert check_palindrome("ABCdcba") == True
    assert check_palindrome("ab  cdcb a") == True
