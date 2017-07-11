# Let us assume that the given array is sorted 
# but starts with negative numbers and ends with positive numbers.
# In this array, find the starting index of the positive numbers.
# Assume that we know the length of the input array. 
# Design a O(log n) algorithm

def find_mono_point(nums):
	if not nums: return

	len_nums = len(nums)

	def _findp(low, high):
		if low > high: return -1 # check later

		if high == low: 
			if nums[low] > 0:
				return low

		mid = low + (high-low)//2

		left_val = nums[mid-1] if mid > low else nums[low]
		right_val = nums[mid+1] if mid < high else nums[high]

		if left_val <= 0 and nums[mid] > 0:
			return mid
		if left_val > 0: # the point should be left
			return _findp(low, mid-1)
		else: 
			return _findp(mid+1, high)
	return _findp(0, len_nums-1)



if __name__ == '__main__':
	nums1 = [-4, -3, 0, 1, 2, 4, 6, 7, 8]
	nums2 = [-6, -4, -3, -2, 0, 1]
	nums3 = [-6, -4, -3, -2]
	nums4 = [1, 2, 3, 4]

	print(find_mono_point(nums1))
	print(find_mono_point(nums2))
	print(find_mono_point(nums3))
	print(find_mono_point(nums4))
