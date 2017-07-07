# Given a string containing only digits,
# restore it by returning all possible valid IP address combinations.
# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255.
# The numbers cannot be 0 prefixed unless they are 0.

def ip_address_parsing(instr):
    if not instr: return
    
    len_in = len(instr)
    
    if len_in > 12: return 
    
    def _ipaddress(i, k):
        if i == len_in and k == 0:
            return [[]]
        if i == len_in or k == 0:
            return []
            
        pick1_results = []
        pick2_results = []
        pick3_results = []
        
        pick1 = instr[i]
        if int(pick1) >= 0 and int(pick1) <= 9:
            pick1_results = _ipaddress(i+1, k-1)
        
        if i < len_in-1:
            pick2 = instr[i:i+2]
            if int(pick2) >= 10 and int(pick2) <= 99:
                pick2_results = _ipaddress(i+2, k-1)
        
        if i < len_in-2:
            pick3 = instr[i:i+3]
            if int(pick3) >= 100 and int(pick3) <= 255:
                pick3_results = _ipaddress(i+3, k-1)
        
        for item in pick1_results:
            item.append(pick1)
        for item in pick2_results:
            item.append(pick2)
        for item in pick3_results:
            item.append(pick3)
        
        return pick1_results + pick2_results + pick3_results
        
    results = _ipaddress(0, 4)
    return [".".join(reversed(item)) for item in results]


if __name__ == '__main__':
    instr1 = '25525511135'
    instr2 = '0100100'
    print(ip_address_parsing(instr1))
    print(ip_address_parsing(instr2))    