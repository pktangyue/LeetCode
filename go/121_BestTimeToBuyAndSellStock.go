package main

func maxProfit(prices []int) int {
	if len(prices) <= 1 {
		return 0
	}
	min := prices[0]
	ret := 0
	for _, v := range prices[1:] {
		if diff := v - min; diff > ret {
			ret = diff
		}
		if v < min {
			min = v
		}
	}
	return ret
}
