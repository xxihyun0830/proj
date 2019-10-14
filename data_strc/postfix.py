class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
    

def infix_to_postfix(str):
    stack = Stack()
    ret = [] 
    tokens = str.split()

    operator = {"*":3,"/":3,"+":2,"-":2,"(":1}

    for t in tokens :
        if t in "()*/+-":
            if t == '(':
                stack.push(t)   
            elif t == ')' : #연산자의 우선순위 비교는 끝난 상태
                op = stack.pop()
                while op != '(':
                    ret.append(op)
                    op = stack.pop()
            else:
                while(not stack.is_empty()) and operator[stack.peek()] >= operator[t]:
                    op = stack.pop()
                    ret.append(op)
                stack.push(t) # stack에 아무것도 없을 때
        else : 
            ret.append(t) # 피연산자일 때,숫자일때 

    while (not stack.is_empty()):
        ret.append(stack.pop())

    return " ".join(ret)


def prefix_to_postfix (str):

    stack = Stack()
    ret = []
    tokens = str.split()

    for t in reversed(tokens): #주어진 prefix순서 뒤집기 
        if t in "+-*/":
            op1 = stack.pop() #가장 끝부터 출력되므로  op1이 먼저 출력되어야 한다. 
            op2 = stack.pop()
            temp = op1 +" "+ op2 +" "+ t
            stack.push(temp)
        else:
            stack.push(t)
        
    while not stack.is_empty(): #어차피 처리가 끝난 가장 마지막 단계가 push되므로 ret에 append하지 않아도 괜츈할듯 
        ret.append(stack.pop())
    
    return " ".join(ret)
    
res = prefix_to_postfix("- * - 5 6 7 * 4 2")
print(res)
rest = prefix_to_postfix("/ + 123 6 + 6 3")
print(rest)
        

def evalution (num1, num2, op):
    if op == "*" :
        return num1 * num2
    elif op =="/":
        return num1 / num2
    elif op =="+":
        return num1 + num2
    elif op == "-":
        return num1 - num2

def eval_postfix(str):
    stack = Stack()
    postfixedStr =str.split()

    for s in postfixedStr : 
        if s in "*/+-" : #계산결과만 필요하기 때문에 괄호는 아무런 영향을 주지 않는다. 
            num2 = stack.pop()
            num1 = stack.pop()
            num3 = evalution(num1, num2, s)
            stack.push(num3)
        else :
           s1 = float(s) 
           stack.push(s1) 
    return stack.pop() #가장 마직막 숫자로 계산이 완료된 것 하나만 남는다. 

def expr_test(infix):
    postfix = infix_to_postfix(infix)
    result = eval_postfix(postfix)
    print("'%s' => '%s' = %f" % (infix, postfix, result))


# 숫자는 여러 자리 숫자가 올 수도 있어요. 대신 연산자와 피 연산자는 공백문자로 나누어집니다.
if __name__ == '__main__':
    expr_test("14 + 3 - 2")
    expr_test("4 + 23 - 4 / 2")
    expr_test("1 + 2 * 43 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 10 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")




    