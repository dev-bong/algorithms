class Hash:
    # TODO : collision 해결하는 로직 추가하기 (seperate chaining, open addressing .. etc)
    def __init__(self, size):
        self.hash_size = size
        self._hash_table = [0] * self.hash_size

    def _hash_func(self, data): # data는 문자열
        # 나머지를 이용하는 간단한 hash function
        data_ascii_sum = sum([ord(d) for d in data]) # ord : 문자의 아스키코드 값 리턴
        hash_addr = data_ascii_sum % self.hash_size
        return hash_addr

    def put_data(self, data, value):
        hash_addr = self._hash_func(data)
        self._hash_table[hash_addr] = value

    def get_data(self, data):
        hash_addr = self._hash_func(data)
        return self._hash_table[hash_addr]

# 예시 - 이름 : 전화번호 데이터 저장하기
if __name__ == "__main__":
    h = Hash(10)
    h.put_data("Sam", "010-1111-1111")
    h.put_data("Johnson", "010-2222-2222")
    h.put_data("Andy", "010-3333-3333")
    print(h._hash_table)
    print(h.get_data("Johnson"))