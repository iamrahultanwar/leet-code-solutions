import "strings"

var symbolMap map[string]int = map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
}


func romanToInt(s string) int {
	str := strings.Split(s, "")
	total := symbolMap[str[len(str)-1]]

	for i := len(str) - 2; i >= 0; i-- {
		prevValue := symbolMap[str[i+1]]
		currentValue := symbolMap[str[i]]

		if currentValue >= prevValue {
			total += currentValue
		} else {
			total -= currentValue
		}

	}

	return total

}
