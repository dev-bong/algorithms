def solution(phone_book):
    book_size = len(phone_book)
    len_num = [[len(num), num] for num in phone_book]
    len_num = sorted(len_num, key=lambda r:r[0], reverse=False)

    for i in range(book_size):
        num = len_num[i][1]
        for j in range(i+1, book_size):
            if len_num[j][1].startswith(num):
                return False

    return True