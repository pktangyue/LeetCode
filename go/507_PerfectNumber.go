package main

func checkPerfectNumber(num int) bool {
	if num <= 2 {
		return false
	}
	// num 肯定包含因子1
	sum := 1
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			sum += i + num/i
		}
	}
	return sum == num
}
