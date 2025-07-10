from collections import deque

def is_palindrome(s: str):
    if not(1 <= len(s) <= 50):
        print("The length of the word must be between 1 and 50.")
    stack = []
    queue = deque()

    for char in s:
        stack.append(char)
        queue.append(char)

    while stack:
        if stack.pop() != queue.popleft():
            return print(f"The word, {s}, is not a palindrome")
    return print(f"The word, {s}, is a palindrome")

s = input("Enter a word:")
print(is_palindrome(s))