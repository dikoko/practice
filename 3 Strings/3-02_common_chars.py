# Write a function that takes two strings as arguments
# and returns a string containing only the characters found in both strings.
# Have them write 2 versions – one that is O(n) and one that is O(n^2).

def common_chars_n2(str1, str2):
    out_list = []
    for ch1 in str1.lower():
        for ch2 in str2.lower():
            if ch1 == ' ' or ch2 == ' ':
                continue
            if ch1 == ch2 and ch1 not in out_list:
                out_list.append(ch1)
    return "".join(out_list)
    
    
def common_chars_n(str1, str2):
    _ctable = set()
    out_list = []
    for ch1 in str1.lower():
        if ch1 != ' ' and ch1 not in _ctable:
            _ctable.add(ch1)
            
    for ch2 in str2.lower():
        if ch2 in _ctable and ch2 not in out_list:
            out_list.append(ch2)
    
    return "".join(out_list)

if __name__ == '__main__':
    str1 = "I am a boy!"
    str2 = "You! don’t mind it"
    
    print(common_chars_n2(str1, str2))
    print(common_chars_n(str1, str2))    