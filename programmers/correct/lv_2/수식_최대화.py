from itertools import permutations

def cal(n1, n2, op): # op에 따라 계산
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2

def calcul_op_order(expr, op_order):
    expr = list(expr)
    nums = None
    ops = []
    
    # expr 문자열을 편하게 사용하기 위해 nums, ops로 나누기
    for i in range(len(expr)):
        if expr[i] in op_order:
            ops.append(expr[i])
            expr[i] = ","
    expr = "".join(expr)
    nums = [int(n) for n in expr.split(",")]

    for op in op_order: # 연산자 우선순위에 따라 계산
        cnt = 0
        for i in range(len(ops)):
            if ops[i] == op:
                nums[i + 1] = cal(nums[i], nums[i + 1], op)
                nums[i] = None
                cnt += 1

        for i in range(cnt): # 해당 연산자에 대해 계산한 횟수 만큼 nums, ops에서 필요없어진 값 삭제
            nums.remove(None)
            ops.remove(op)

    return abs(nums[0])
    

def solution(expression):
    answer = []
    operator = set(["+", "*", "-"])
    cases = permutations(operator, 3)

    for case in cases:
        res = calcul_op_order(expression, case)
        answer.append(res)
    return max(answer)