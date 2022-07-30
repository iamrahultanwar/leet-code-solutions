import (
	"sort"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) > 0 && len(nums2) > 0 {
		if nums1[0] > nums2[0] {
			t := nums1
			nums1 = nums2
			nums2 = t
		}
	}

	nums := append(nums1, nums2...)
	if len(nums) == 0 {
		return float64(0)
	}
	sort.Ints(nums)
	half := len(nums) / 2

	if len(nums)%2 > 0 {
		return float64(nums[half])
	}
	return float64(nums[half-1]+nums[half]) / 2.0
}