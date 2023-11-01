from b_hashtable import Hashable
from c_stack import Stack
def is_pair(text):
    # 1. stack 만들기
    stack = Stack()

    for ch in text:
        stack.push(ch)

    # 2. 각 쌍 stack 만들기
    s1 = Stack()  # ]
    s2 = Stack()  # }
    s3 = Stack()  # )

    # 3. 하나씩 뽑으면서 체크
    while not(stack.is_empty()):
        top = stack.peek()
        stack.pop()
        # 닫는 괄호 일때는 각 괄호 스택에 푸쉬 
        if top not in '()[]{}':
            continue
        elif top in ']})':
            if top == ']':
                s1.push(top)
            elif top == '}':
                s2.push(top)
            elif top == ')':
                s3.push(top)
        else:
            # 여는 괄호 일때는 각 괄호 스택에 짝있나 확인
            # 없으면 바로 return false
            # 있으면 괄호 스택 pop
            if top == '[':
                if not s1.is_empty():
                    s1.pop()
                else:
                    return False
            elif top == '{':
                if not s2.is_empty():
                    s2.pop()
                else:
                    return False
            elif top == '(':
                if not s3.is_empty():
                    s3.pop()
                else:
                    return False
 
    # 세 스택 다 비어있어야
    if s1.is_empty() and s2.is_empty() and s3.is_empty():
        return True
    else:
        return False

# 직접 구현한 hashtable 사용해서 구현하기
# switch로직 사용 할것(switch문 없이)


def is_pair2(text):
    hashtable = Hashable()
    hashtable.add("(",")") # key - value쌍으로 해쉬에 넣기
    hashtable.add("[","]")
    hashtable.add("{","}")

    stack = Stack()

    for ch in text:
        # 열리는 괄호 일때(key)
        if ch in hashtable:
            stack.push(ch)
            continue
        # 닫히는 괄호 검사 전에 이미 스택이 비어있으면 (열리는 괄호 없다는 뜻)
        if stack.is_empty(): return False

        # 닫히는 괄호 일때(value)
        k = stack.pop() # 맨마지막에 들어간 열린 괄호
        if ch != hashtable.get(k): # 첫 닫히는 괄호와 쌍이 안맞으면 안됨
            return False
    
    return True if stack.is_empty() else False 
    


