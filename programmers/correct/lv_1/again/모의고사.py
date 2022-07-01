class Hash: # N번 문제를 뭘로 찍을까에 대한 패턴을 hash로 구현
    def __init__(self, table):
        self.hash_size = len(table)
        self.hash_table = table

    def _hash_func(self, data):
        hash_addr = data % self.hash_size # 같은 패턴으로 돌아가면서 찍기
        return hash_addr

    def get_data(self, data):
        hash_addr = self._hash_func(data)
        return self.hash_table[hash_addr]

def solution(answers):
    answer = []
    pattern = [ # 찍기 패턴 입력
        Hash([1, 2, 3, 4, 5]),
        Hash([2, 1, 2, 3, 2, 4, 2, 5]),
        Hash([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    score = [[1, 0], [2, 0], [3, 0]] # 점수 [학생번호?, 맞춘 문제 수]
    num_of_problem = len(answers)

    for i in range(num_of_problem): # 점수 계산
        if pattern[0].get_data(i) == answers[i]:
            score[0][1] += 1
        if pattern[1].get_data(i) == answers[i]:
            score[1][1] += 1
        if pattern[2].get_data(i) == answers[i]:
            score[2][1] += 1
    
    score.sort(key=lambda r:r[1], reverse=True)
    answer.append(score[0][0])
    for sc in score[1:]:
        if score[0][1] == sc[1]: # 동점자 있으면 추가로 넣기
            answer.append(sc[0])
    answer.sort()

    return answer