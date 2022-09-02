class Music():
    def __init__(self, start, end, name, melody):
        self.start = int("".join(start.split(":"))) # 시작 시간 문자열에서 : 빼고 정수로 만들어서 크기 비교 가능하도록
        self.minute = self._calcul_minute(start, end)
        self.melody = self._get_full_melody(self._extract_notes(melody))
        self.name = name

    def _calcul_minute(self, start, end):
        # 음악 재생 시간 계산 (분 단위)
        sh, sm = [int(s) for s in start.split(":")]
        eh, em = [int(e) for e in end.split(":")]

        if em >= sm:
            h = eh - sh
            m = em - sm
        else:
            h = eh - sh - 1
            m = 60 + em - sm
        
        return (h * 60) + m

    def _get_full_melody(self, notes):
        # 추출한 음들을 이용해서 멜로디 재구성 (알파벳 뒤에 0 또는 # 붙은 형태로)
        full_melody = ""
        notes_size = len(notes)

        for i in range(self.minute):
            full_melody += notes[i % notes_size]
        
        return full_melody

    def _extract_notes(self, melody):
        # 음 추출해서 분리하기
        notes = []
        idx = 0

        while idx < len(melody):
            note = melody[idx]

            if idx + 1 < len(melody): # 뒤에 "#" 있는건 붙이고, 없는건 "0" 붙여서 구분
                if melody[idx + 1] == "#":
                    note += "#"
                    idx += 1
                else:
                    note += "0"
            else:
                note += "0" # 맨뒤에도 붙여줘야함
            notes.append(note)
            idx += 1
        
        return notes

    def in_melody(self, melody):
        # 비교대상 멜로디도 똑같은 포맷으로 만들어서 비교
        tr_melody = "".join([m for m in self._extract_notes(melody)])
        
        return True if tr_melody in self.melody else False


def solution(m, musicinfos):
    answer = {
        "name" : "",
        "minute" : 0,
        "start" : 0
    }
    mi_list = []

    for mi in musicinfos:
        st, end, name, melody = mi.split(",")
        mi_list.append(Music(st, end, name, melody))

    for music in mi_list:
        if music.in_melody(m):
            if music.minute > answer["minute"]: # 재생된 시간이 더 크면 저장
                answer["name"] = music.name
                answer["minute"] = music.minute
                answer["start"] = music.start
            elif music.minute == answer["minute"]:
                if music.start < answer["start"]: # 재생된 시간이 같을 경우 먼저 재생된 음악일 경우에만 저장
                    answer["name"] = music.name
                    answer["minute"] = music.minute
                    answer["start"] = music.start

    if not answer["name"]: # 일치하는 음악 없을 경우 (문제 조건)
        return "(None)"

    return answer["name"]