import re

def verify_card_number(card_number:str):
    number = re.sub(r'[\s\-]', '', card_number)
    print(number)
    if not number:
        return 'INVALID!'
    doubled = 0
    ordinary = 0
    last_digit = 0
    for i, num in enumerate(number[::-1]):
        if i==0:
            last_digit = int(num)
            print(f'last_digit: {last_digit}')
            
        elif i%2!=0:
            if int(num) == 9:
                temp = 9
            else:
                temp = (int(num)*2)%9
            doubled += temp
            print(f'doubled: {doubled}, num: {num}, temp: {temp}') 
        
        else:
            ordinary += int(num)
            print(f'ordinary: {ordinary}, num: {num}')

    if (doubled+ordinary+last_digit)%10 == 0 :
        print(doubled+ordinary+last_digit)
        return 'VALID!'
    else:
        print(doubled+ordinary+last_digit)
        return 'INVALID!'


print(verify_card_number('1234 5678 9012 3456'))