package main

func canCompleteCircuit(gas []int, cost []int) int {
	l := len(gas)
	remain := 0
	ret := 0
	for i := 0; i < l; i++ {
		// 从ret开始，到ret+i点时，剩余的gas，如果小于0，需要重置
		remain += gas[(ret+i)%l] - cost[(ret+i)%l]
		if remain < 0 {
			ret++
			// 所有起始点都遍历过之后还无法满足条件，返回-1
			if ret == l {
				return -1
			}
			ret = ret % l
			remain = 0
			i = -1
			continue
		}
	}
	return ret
}
