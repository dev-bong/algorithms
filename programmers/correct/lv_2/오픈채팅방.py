def solution(record):
    answer = []
    nicknames = {} # key : id, value : nickname

    for rc in record: # 각 id의 최종 nickname인지 무엇인지 저장
        rc_sp = rc.split(" ")
        nicknames[rc_sp[-2]] = rc_sp[-1] # record에서 가장 뒤는 nickname, 뒤에서 2번째는 id
    
    for rc in record:
        rc_sp = rc.split(" ")
        if rc_sp[0] == "Enter": # record에서 가장 앞은 action, 앞에서 2번째는 id
            answer.append(f"{nicknames[rc_sp[1]]}님이 들어왔습니다.")
        elif rc_sp[0] == "Leave":
            answer.append(f"{nicknames[rc_sp[1]]}님이 나갔습니다.")

    return answer

# 테스트 케이스
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))