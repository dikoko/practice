# Giving a method intToEnglish that receives an int as a parameter, 
# how do you return its representation in english words. 
# The number can be of any size but no more than around 2 billion since the parameter is an int 2ˆ32

# 1,000,000,000
# billion
# million
# thousand
# hundread
# ninety
# eighty
# seventy
# sixty
# fifty
# forty
# thirty
# twenty
# nineteen
# eighteen
# seventeen
# sixteen
# fifteen
# fourteen
# thirteen
# twelve
# eleven
# ten
# nine
# eight
# seven
# six
# five
# four
# three
# two
# one
# zero

# read the 1000 unit correctly

_dstr_base_map = {
	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
	11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
	16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}
_dstr_tens_map = {
	2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 
	6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
_dstr_high_map = {
	0: 'hundread', 1: 'thousand', 2: 'million', 3: 'billion'}

def read_kunit(num):

	if num < 0 or num >= 1000:
		print('something wrong')
		return
	if num == 0:
		return ''

	out_list = []

	hundred_digit = num // 100
	if hundred_digit > 0 and hundred_digit <= 9:
		out_list.append(_dstr_base_map[hundred_digit] + ' hundread')
	uten_digit = num % 100
	if uten_digit >= 20 and uten_digit <= 99:
		ten_digit = uten_digit // 10
		one_digit = uten_digit % 10
		out_str = _dstr_tens_map[ten_digit]
		if one_digit > 0 and one_digit <= 9:
			out_str += ' '
			out_str += _dstr_base_map[one_digit]
		out_list.append(out_str)
	elif uten_digit < 20 and uten_digit >= 1:
		out_list.append(_dstr_base_map[uten_digit])

	return " ".join(out_list)


def int_to_english(num):
	if num > 2000000000:
		print('overflow')
		return
	if num < 0: return
	if num == 0: return 'zero'

	out_list = []
	bill_digit = num // 1000000000
	if bill_digit > 0:
		out_list.append(_dstr_base_map[bill_digit] + ' billion')
	num %= 1000000000
	mill_digit = num // 1000000
	if mill_digit > 0:
		mill_str = read_kunit(mill_digit)
		out_list.append(mill_str + ' million')
	num %= 1000000
	thousand_digit = num // 1000
	if thousand_digit > 0:
		thousand_str = read_kunit(thousand_digit)
		out_list.append(thousand_str + ' thousand')

	num %= 1000
	out_list.append(read_kunit(num))

	return " ".join(out_list)
	
	
if __name__ == '__main__':
	print(int_to_english(100))
	print(int_to_english(1012341100))
	print(int_to_english(21))
	print(int_to_english(34239912))
	print(int_to_english(1397873400))

