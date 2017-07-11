# Write code to decode strings.
# For example, String str = "3[a2[bd]g4[ef]h]", the output should be
# "abdbdgefefefefhabdbdgefefefefhabdbdgefefefefh".

def decode(instr):
    
    len_s = len(instr)
    
    count_stack = []
    text_stack = []
    
    current_count = ''
    for char in instr:
        if char.isdigit():
            current_count += char
            continue
        elif char == '[': # count ends.
            count_stack.append(int(current_count))
            current_count = ''
            text_stack.append('[')
            continue
        elif char == ']':
            # pop until '['
            target_text = ''
            pop_text = text_stack.pop()
            while pop_text != '[':
                target_text = pop_text + target_text
                pop_text = text_stack.pop()
            count = count_stack.pop()
            target_text = target_text * count
            text_stack.append(target_text)
            continue
        else: # normal character
            text_stack.append(char)

    return text_stack[0]
        
# # 3[a2[bd]g]
# cs[3
# ts['[','a','bdbd',g
# cc = '
# tt = ''

# abdbdgefefefefhabdbdgefefefefhabdbdgefefefefh
# abdbdgefefefefhabdbdgefefefefhabdbdgefefefefh

if __name__ == '__main__':
    instr = "3[a2[bd]g4[ef]h]"
    
    print(decode(instr))