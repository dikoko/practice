# You given a sentence of english words and spaces between them.
#
# no double spaces
# no empty words
# no spaces at the ends of a sentence Reverse the string as the example.
# Example:
# input "I wish you a merry Christmas"
# output "Christmas merry a you wish I"
#
# Constrains: O(1) additional memory


def reverse_str(instr):
    if not instr: return
    
    len_s = len(instr)
    inlist = list(instr)
    
    def _reverse(low, high):
        while low < high:
            inlist[low], inlist[high] = inlist[high], inlist[low]
            low += 1
            high -= 1
            
    # reverse all first
    _reverse(0, len_s-1)
    # then reverse word by word
    low = 0
    for i in range(1, len_s):
        if inlist[i] == ' ':
            _reverse(low, i-1)
            low = i+1
    _reverse(low, len_s-1)
    
    return "".join(inlist)


if __name__ == '__main__':
    instr = "I wish you a merry Christmas"
    print(reverse_str(instr))