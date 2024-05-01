SYMBOL_VALUE_MAP = {
    'I': (1, 1, 3),
    'V': (5, 1, 1),
    'X': (10, 10, 3),
    'L': (50, 10, 1),
    'C': (100, 100, 3),
    'D': (500, 100, 1),
    'M': (1000, 1000, 3),
}
ALLOWED_DUALCHAR_NUMERALS = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def roman_to_int(roman: str):
    if not roman or len(roman) == 0:
        return -1
    
    value = 0

    curr_level = 10000
    curr_level_val = 0
    prev_char_val = 0
    active_repeats = 0
    expect_lower_level = True
    index = 0
    while index < len(roman):
        curr_char = roman[index]
        curr_char_val, new_char_level, curr_allowed_repeats = SYMBOL_VALUE_MAP.get(curr_char)
        if curr_char_val == None:
            return -1
        if curr_char_val == prev_char_val:
            if active_repeats < allowed_repeats:
                active_repeats += 1
            else:
                return -1
        else:
            active_repeats = 1
            allowed_repeats = curr_allowed_repeats

        if new_char_level == curr_level and curr_char_val <= prev_char_val: # example: III, XX, VI etc...
            if expect_lower_level:
                return -1
            curr_level_val += curr_char_val
            expect_lower_level = False
        elif new_char_level < curr_level: 
            ## check if this is dual char numeral:
            if index < len(roman) and roman[index: index + 2] in ALLOWED_DUALCHAR_NUMERALS:                
                big_val, _, _= SYMBOL_VALUE_MAP.get(roman[index + 1])
                curr_level_val += big_val - curr_char_val
                allowed_repeats = 0
                expect_lower_level = True # after dual numeral we expect a lower level
                index += 1
            else: # example XI, VI etc...
                value += curr_level_val
                curr_level_val = curr_char_val
                curr_level = new_char_level
                expect_lower_level = False
        else:
            return -1
        prev_char_val = curr_char_val
        index += 1
    if curr_level_val > 0:
        value += curr_level_val
    return value        

def test_roman_to_int(roman, expected):
    actual = roman_to_int(roman)
    if expected == actual:
        print(f'CORRECT {roman} is {actual}')
    else:
        err = "invalid number" if expected == -1 else expected
        print(f'ERROR {roman} expected {err}, got {actual}')

if __name__ == '__main__':    
    test_roman_to_int('XCVI', 96)
    test_roman_to_int('XC', 90)
    test_roman_to_int('XIV', 14)
    test_roman_to_int('CXIV', 114)
    test_roman_to_int('MCMXCIV', 1994)
    test_roman_to_int('IV', 4)
    test_roman_to_int('XIXI', -1)
    test_roman_to_int('XXI', 21)
    test_roman_to_int('III', 3)
    test_roman_to_int('IIII', -1)
    test_roman_to_int('C', 100)
    test_roman_to_int('MMMDCCCXCIX', 3899)
    test_roman_to_int('IX', 9)
    test_roman_to_int('XL', 40)
    test_roman_to_int('CD', 400)
    test_roman_to_int('CM', 900)
    test_roman_to_int('LVIII', 58)
    test_roman_to_int('MCMIII', 1903)
    test_roman_to_int('MMXXIV', 2024)
    test_roman_to_int('MMMCMXCIX', 3999)
    test_roman_to_int('IIIIII', -1)
    test_roman_to_int('VV', -1)
    test_roman_to_int('XXXX', -1)
    test_roman_to_int('LL', -1)
    test_roman_to_int('DD', -1)
    test_roman_to_int('MMMM', -1)
    test_roman_to_int('IC', -1)
    test_roman_to_int('IM', -1)
    test_roman_to_int('XM', -1)
    test_roman_to_int('LC', -1)
    test_roman_to_int('LD', -1)
    test_roman_to_int('LM', -1)
    test_roman_to_int('DM', -1)

    
