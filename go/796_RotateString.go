package main

func rotateString(A string, B string) bool {
	if A == "" && B == "" {
		return true
	}
	if len(A) != len(B) {
		return false
	}
	startOfB := 0
	for startOfB < len(B) {
		same := true
		for i := 0; i < len(A); i++ {
			if A[i] != B[(startOfB+i)%len(B)] {
				same = false
				break
			}
		}
		if same {
			return true
		}
		startOfB++
	}
	return false
}
