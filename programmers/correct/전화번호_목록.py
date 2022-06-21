def solution(phone_book):
    book_size = len(phone_book)
    phone_book.sort() # 파이썬의 문자열 정렬은 사전식으로 정렬되어 이렇게 정렬하면 뒤에꺼 1개만 비교하면 된다!

    for i in range(book_size-1): # for문 1개로 단축
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

##### hash로 풀기 #####
class Hash():
    """
    hash 구조
    e.g. "347" 넣으면 아래처럼 됨
    hash_table = {
        "3" : {
            "is_end" : False,
            "4" : {
                "is_end" : False,
                "7" : {
                    "is_end" : True
                }
            }
        }
    }

    table 완성 시키고 숫자넣어서 tree search 처럼 찾아가서 도달한 곳에 "is_end"를 보고 접두사인지 판별
    "is_end"가 False면 접두사임
    ? 그냥 tree로 만들어 볼까??
    """
    def __init__(self):
        self.hash_table = {}

    def put_data(self, num): # 테이블에 데이터 넣기
        prefix = False
        tmp = self.hash_table
        size = len(num)
        for n in range(size):
            if num[n] in tmp:
                if n == (size - 1):
                    if not tmp[num[n]]["is_end"]: # 숫자 끝에 도달했을때 "is_end" = False 이면 접두사
                        prefix = True
                else:
                    tmp[num[n]]["is_end"] = False
            else:
                tmp[num[n]] = {}
                if n == (size - 1):
                    tmp[num[n]]["is_end"] = True
                else:
                    tmp[num[n]]["is_end"] = False
            tmp = tmp[num[n]]
            
        return prefix

def solution2(phone_book):
    pb_hash = Hash()
    phone_book.sort(reverse = True) # 사전식 역순으로 정렬해서 접두사 체크 용이하도록..
    for num in phone_book:
        if pb_hash.put_data(num): # 테이블 완성하지 않아도 중간에 접두사 발견하면 리턴
            return False

    return True

"""
원래는 테이블 다 완성시킨 후 하나씩 넣어보면서 접두사 체크하는 거였는데 (phone_book 정렬 X)
마지막 테스트 케이스에서 시간 초과가 나서 phone_book 정렬하고, 데이터 넣어보면서 접두사 체크 동시에 하는걸로 변경
? 정렬할거면 그냥 1번 풀이가 나은거 같은데..
? tree로 한번 해보기
"""