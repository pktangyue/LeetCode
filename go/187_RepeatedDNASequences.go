package main

func findRepeatedDnaSequences(s string) []string {
	if len(s) < 10 {
		return []string{}
	}
	m := make(map[string]int)
	for i := 0; i <= len(s)-10; i++ {
		m[s[i:i+10]] += 1
	}
	ret := make([]string, 0)
	for k, v := range m {
		if v > 1 {
			ret = append(ret, k)
		}
	}
	return ret
}
