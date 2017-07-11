# Let A be an array of n distinct integers. 
# Suppose A has the following property: 
# there exists an index 1 <= k <= n such that A[1],...,A[k] is an increasing sequence 
# and A[k+1],...,A[n] is a decreasing sequence.
# Design and analyze an efficient algorithm for finding k.


def finding_peak(nums):
	if not nums: return

	len_nums = len(nums)

	def _fpeak(low, high):
		if low > high: return -1 # check later.. no use case.

		mid = low + (high-low)//2
		
		left_val = nums[mid-1] if mid > low else nums[low]
		right_val = nums[mid+1] if mid < high else nums[high]

		if left_val <= nums[mid] and nums[mid] >= right_val:
			return mid
		
		if left_val >= nums[mid]: # peak should be left
			return _fpeak(low, mid-1)
		else:  # peak should be right 
			return _fpeak(mid+1, high)
	

	return _fpeak(0, len_nums-1)+1


if __name__ == '__main__':
	nums1 = [1, 3, 8, 7, 5, 4, 2]
	nums2 = [1, 2, 3, 4, 5, 6, 7]
	nums3 = [7, 6, 5, 4, 3, 2, 1]

	print(finding_peak(nums1))
	print(finding_peak(nums2))
	print(finding_peak(nums3))

