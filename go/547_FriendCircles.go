package main

func findCircleNum(M [][]int) int {
	if len(M) == 0 {
		return 0
	}
	ret := 0
	// 把 i 的朋友集中在自己这一行，并且把扫过的朋友所在行全部设为0
	for i := 0; i < len(M); i++ {
		if M[i][i] == 0 {
			continue
		}
		for {
			hasNew := false
			for j := i + 1; j < len(M); j++ {
				if M[i][j] == 1 && M[j][j] != 0 {
					for k := 0; k < len(M); k++ {
						if M[j][k] == 1 {
							M[j][k] = 0
							M[i][k] = 1
							hasNew = true
						}
					}
				}
			}
			if !hasNew {
				break
			}
		}
		ret++
	}
	return ret
}
