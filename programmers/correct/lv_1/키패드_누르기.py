class ThumbPos():
    def __init__(self):
        self.l_pos = (3, 0)
        self.r_pos = (3, 2)
        self.keyboard = {
            1 : (0,0),
            2 : (0,1),
            3 : (0,2),
            4 : (1,0),
            5 : (1,1),
            6 : (1,2),
            7 : (2,0),
            8 : (2,1),
            9 : (2,2),
            "*" : (3,0),
            0 : (3,1),
            "#" : (3,2),
        }
        self.thumb_history = ""
    
    def click(self, button, thumb):
        if thumb == "L":
            self.thumb_history += "L"
            self.l_pos = self.keyboard[button]
        else:
            self.thumb_history += "R"
            self.r_pos = self.keyboard[button]

    def _distance(self, p1, p2): # 두 버튼 사이 거리
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def lr_dist(self, num):
        return (self._distance(self.l_pos, self.keyboard[num]), self._distance(self.r_pos, self.keyboard[num]))

def solution(numbers, hand):
    tp = ThumbPos()

    for num in numbers:
        if num in [1, 4, 7]: # 무조건 왼손
            tp.click(num, "L")
        elif num in [3, 6, 9]: # 무조건 오른손
            tp.click(num, "R")
        else:
            l_dis, r_dis = tp.lr_dist(num)
            if l_dis < r_dis: # 거리 가까운 쪽 엄지로 누르기
                tp.click(num, "L")
            elif l_dis > r_dis:
                tp.click(num, "R")
            else:
                if hand == "left": # 오른손잡이 or 왼손잡이
                    tp.click(num, "L")
                else:
                    tp.click(num, "R")

    return tp.thumb_history