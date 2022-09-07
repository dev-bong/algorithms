def solution(files):
    answer = []
    numbers = [str(i) for i in range(10)]
    format_files = []

    for file in files:
        # head 분리
        for i in range(len(file)):
            if file[i] in numbers:
                break
        head = file[:i].lower()
        remain = file[i:]

        # remain에서 number, tail 분리
        is_break = False
        for i in range(len(remain)):
            if remain[i] not in numbers or i > 4:
                is_break = True
                break
        
        if is_break: # 뒤에 tail이 있는 경우
            number = int(remain[:i])
        else: # tail 없이 모두 number인 경우
            number = int(remain)

        format_files.append((head, number, file))

    format_files.sort(key = lambda r : (r[0], r[1])) # 정렬.. #! python의 sort()는 in-place sort인 것으로 보임
    for f_file in format_files:
        answer.append(f_file[2])

    return answer

"""
#? print(int("010"))?? -> 10
#? in-place 정렬?

만약 sort()가 in-place가 아니었다면??
    - in-place 정렬 새로 짜서 적용해야함
"""