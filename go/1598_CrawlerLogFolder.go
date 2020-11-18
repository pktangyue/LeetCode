package main

func minOperations(logs []string) int {
	ret := 0
	for _, log := range logs {
		switch log {
		case "../":
			if ret > 0 {
				ret--
			}
		case "./":
		default:
			ret++
		}
	}
	return ret
}
