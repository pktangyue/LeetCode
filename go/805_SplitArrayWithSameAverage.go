package main

import (
	"sort"
)

func splitArraySameAverage(A []int) bool {
	if len(A) == 1 {
		return false
	}
	sum := 0
	for _, v := range A {
		sum += v
	}
	// 放大 len(A) 倍，用整数运算，避免小数精度问题
	// 这时 sum 就为新数组的平均值
	for i := 0; i < len(A); i++ {
		A[i] = A[i]*len(A) - sum
		// 只要有一个数字和平均数相等，让它单独组成一个列表，其他的为另一个列表就能满足条件了
		if A[i] == 0 {
			return true
		}
	}
	sort.Ints(A)
	left, right := 0, 0
	for i := 0; i < len(A)-1; i++ {
		// 找到小于平均值和大于平均值的分界点
		if A[i] < 0 && A[i+1] > 0 {
			left = i
			right = i + 1
		}
	}
	// 找出小于平均数所有可能的和，已经组成所需最小元素个数
	leftMap := make(map[int]int)
	for i := left; i >= 0; i-- {
		m := make(map[int]int)
		for k, v := range leftMap {
			m[k] = v
			m[k+A[i]] = leftMap[k] + 1
		}
		m[A[i]] = 1
		leftMap = m
	}
	// 找出大于平均数所有可能的和，已经组成所需最小元素个数
	rightMap := make(map[int]int)
	for i := right; i < len(A); i++ {
		m := make(map[int]int)
		for k, v := range rightMap {
			// 发现左侧已有相同可能，并且不包含所有元素，则返回true
			if n, ok := leftMap[-(k + A[i])]; ok && (n+rightMap[k]+1) < len(A) {
				return true
			}
			m[k] = v
			m[k+A[i]] = rightMap[k] + 1
		}
		// 发现左侧已有相同可能，并且不包含所有元素，则返回true
		if n, ok := leftMap[-A[i]]; ok && (n+1) < len(A) {
			return true
		}
		m[A[i]] = 1
		rightMap = m
	}
	return false
}
