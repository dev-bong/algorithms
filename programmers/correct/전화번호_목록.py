def solution(phone_book):
    book_size = len(phone_book)
    phone_book.sort() # 파이썬의 문자열 정렬은 사전식으로 정렬되어 이렇게 정렬하면 뒤에꺼 1개만 비교하면 된다!

    for i in range(book_size-1): # for문 1개로 단축
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True