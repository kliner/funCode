op = ['+', '-', '*', '/', '^']
debug = 0

def solve(s):
    s = '('+s+')'
    ans = ''
    opStack = []
    for ch in s:
        if ch == ')':
            while opStack[-1] != '(':
                ans += opStack.pop() 
            opStack.pop()
        elif ch == '(':
            opStack += [ch]
        elif ch in op:
            idx = op.index(ch)
            while opStack and opStack[-1] != '(' and op.index(opStack[-1]) > idx:
                ans += opStack.pop() 
            opStack += [ch]
        else:
            ans += ch
        
    print ans

if debug:
    solve('(a+(b*c))')
    solve('a+b*c')
    solve('((a+b)*(z+x))')
    solve('((a+t)*((b+(a+c))^(c+d)))')
T = input()
for _ in xrange(T):
    solve(raw_input())

