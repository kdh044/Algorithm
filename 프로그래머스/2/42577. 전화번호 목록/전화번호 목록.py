def solution(phone_book):
    phone_set = set(phone_book)
    
    for number in phone_set:
        for i in range(1,len(number)):
            number_split = number[:i]
            
            if number_split in phone_set:
                return False
    return True