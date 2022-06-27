import re
def iscorrect(string):
    m = re.match(r"[(){}\[\]]*(.*)",string)
    assert m is not None and len(m.group(1))<1
    stack = []
    match = {']':'[',')':'(','}':'{'}
    for literal in string:
        if literal in ['(','[','{']:
            stack.append(literal)
        elif literal in [')',']','}']:
            if len(stack) > 0 and stack[-1] == match[literal]:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True
def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        string = input()
        print(iscorrect(string))
if __name__ == "__main__":
    main()
