package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindRedundantDirectedConnection(t *testing.T) {
	assert.Equal(t,
		[]int{23, 50},
		findRedundantDirectedConnection([][]int{
			// 这个例子找环路有问题
			{37, 30},
			{21, 34},
			{10, 40},
			{8, 36},
			{18, 10},
			{50, 11},
			{13, 6},
			{40, 7},
			{14, 38},
			{41, 24},
			{32, 17},
			{31, 15},
			{6, 27},
			{45, 3},
			{30, 42},
			{43, 26},
			{9, 4},
			{4, 31},
			{1, 29},
			{5, 23},
			{44, 19},
			{15, 44},
			{49, 20},
			{26, 5},
			{23, 50},
			{48, 41},
			{47, 22},
			{3, 46},
			{11, 16},
			{12, 35},
			{33, 50},
			{34, 45},
			{38, 2},
			{2, 32},
			{24, 49},
			{35, 37},
			{29, 13},
			{46, 48},
			{28, 12},
			{7, 21},
			{27, 18},
			{17, 39},
			{42, 14},
			{20, 47},
			{36, 1},
			{22, 9},
			{25, 8},
			{39, 25},
			{16, 28},
			{19, 43},
		}),
	)
	assert.Equal(t,
		[]int{4, 1},
		findRedundantDirectedConnection([][]int{{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5}}),
	)
	assert.Equal(t,
		[]int{5, 1},
		findRedundantDirectedConnection([][]int{
			{4, 1}, {1, 5}, {4, 2}, {5, 1}, {4, 3},
		}),
	)
	assert.Equal(t,
		[]int{3, 1},
		findRedundantDirectedConnection([][]int{
			{5, 2}, {5, 1}, {3, 1}, {3, 4}, {3, 5},
		}),
	)
	assert.Equal(t,
		[]int{2, 3},
		findRedundantDirectedConnection([][]int{{1, 2}, {1, 3}, {2, 3}}),
	)
	assert.Equal(t,
		[]int{2, 1},
		findRedundantDirectedConnection([][]int{{2, 1}, {3, 1}, {4, 2}, {1, 4}}),
	)
}
