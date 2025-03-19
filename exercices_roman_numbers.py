def create_roman_numb(num):
    list_roman_numb = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_to_string = ""
    for value, symbol in list_roman_numb:
        while num >= value:
            roman_to_string += symbol
            num -= value
    
    return roman_to_string


num = int(input("Introdu numar: "))
print(f"Numarul roman generat: {create_roman_numb(num)}")
