# Given:
# a encoded to 1
# b encoded to 2
# ....
# z encoded to 26
#
# You can translate a number to a string:
# '123' can be translated to 'abc'
# but also can be translated to 'aw','lc' which gives 3 total translations
# '12' can be translated to 'ab' and 'l' -> 2 translations
#
# Write a function to get the number of valid combinations from a number like '123123123'

def char_encoding(instr):
    
    len_in = len(instr)
    
    T = {}
    def _encode(i):
        if i in T:
            return T[i]
            
        if i == 0:
            pick1 = int(instr[i])
            if pick1 >= 1 and pick1 <= 9:
                T[i] = 1
                return T[i]
            else:
                T[i] = 0
                return T[i]
        if i == 1:
            pick1 = int(instr[i])
            pick2 = int(instr[i-1:i+1])
            num_ways = 0
            if pick1 >= 1 and pick1 <=9:
                num_ways += _encode(0)
            if pick2 >=10 and pick2 <=26:
                num_ways += 1
            T[i] = num_ways
            return T[i]
            
        # i > 1
        pick1 = int(instr[i])
        pick2 = int(instr[i-1:i+1])
        num_ways = 0
        if pick1 >= 1 and pick1 <= 9:
            num_ways += _encode(i-1)
        if pick2 >= 10 and pick2 <=26:
            num_ways += _encode(i-2)
    
        T[i] = num_ways
        return T[i]
    
    return _encode(len_in-1)
            
    

if __name__ == '__main__':
	str1 = '123'  # 3
	str2 = '12'     # 2
	str3 = '1231'   # 3
	str4 = '1'      # 1
	str5 = '123123123'  # 27
	print(char_encoding(str1))
	print(char_encoding(str2))
	print(char_encoding(str3))
	print(char_encoding(str4))
	print(char_encoding(str5))
