package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsBipartite(t *testing.T) {
	assert.Equal(t,
		true,
		isBipartite([][]int{{1}, {0}, {3}, {2}}),
	)
	assert.Equal(t,
		true,
		isBipartite([][]int{{1}, {0, 3}, {3}, {1, 2}}),
	)
	assert.Equal(t,
		true,
		isBipartite([][]int{{1, 3}, {0, 2}, {1, 3}, {0, 2}}),
	)
	assert.Equal(t,
		false,
		isBipartite([][]int{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}),
	)
}
