def solution(new_id):
    available_ascii = [i for i in range(ord("a"), ord("z") + 1)]
    available_ascii += [i for i in range(ord("0"), ord("9") + 1)]
    available_ascii.append(ord("-"))
    available_ascii.append(ord("_"))
    available_ascii.append(ord("."))
    
    # step 1 : 대문자 -> 소문자
    st1 = new_id.lower()
    print("step 1:", st1)

    # step 2 : 지정된 문자말고 제외
    st2 = ""
    for ch in st1:
        if ord(ch) in available_ascii:
            st2 += ch
    print("step 2:", st2)

    # step 3 : 연속된 마침표 제거
    st3 = ""
    ex_dot = False
    for ch in st2:
        if ch == ".":
            if ex_dot:
                continue
            else:
                ex_dot = True
        else:
            if ex_dot:
                ex_dot = False
        st3 += ch
    print("step 3:", st3)

    # step 4 : 양 끝의 마침표 제거
    st4 = st3.strip(".")
    print("step 4:", st4)

    # step 5
    st5 = st4 if st4 else "a"
    print("step 5:", st5)

    # step 6
    st6 = st5[:15].strip(".") if len(st5) >= 16 else st5
    print("step 6:", st6)

    # step 7
    st7 = st6
    if len(st7) <= 2:
        for i in range(3 - len(st6)):
            st7 += st6[-1]
    print("step 7:", st7)

    return st7