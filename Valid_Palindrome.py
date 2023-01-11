import collections


def isPalindrome(s: str) -> bool:
    str_set : Deque = collections.deque()

    for a in s:
        if a.isalnum():
            str_set.append(a.lower())

    while len(str_set) > 1:
        if str_set.popleft() != str_set.pop():
            return False

    return True


if __name__ == '__main__':
    isPalindrome("A man, a plan, a canal: Panama")
