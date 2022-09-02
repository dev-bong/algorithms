def solution(s):
    s_list = [a for a in s.split(" ")]
    jaden = []
    print(s_list)

    for string in s_list:
        if not string: # 공백문자가 연속해서 있을 경우 빈 스트링이 있을 수 있음
            jaden.append(string)
            continue
        fr = string[0]
        remain = string[1:]
        jaden.append(fr.upper() + remain.lower())

    return " ".join(jaden)

#? JadenCase : 첫글자는 대문자(알파벳일 경우), 나머지는 소문자
#? 알파벳이 아닌 문자에 upper(), lower()하면 변화 없는것 같다. 확인 필요