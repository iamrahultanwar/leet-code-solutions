func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	a, n := x, x
	b := 0

	count := 0
	for n > 0 {
		n = n / 10
		count++
	}
	for a > 0 {
		count--
		b = b + ((a % 10) * int((math.Pow(float64(10), float64(count)))))
		a = a / 10
	}
	return b == x
}
