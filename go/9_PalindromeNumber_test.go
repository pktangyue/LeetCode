package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPalindrome(t *testing.T) {
	assert.Equal(t,
		true,
		isPalindrome(121),
	)
	assert.Equal(t,
		false,
		isPalindrome(-121),
	)
	assert.Equal(t,
		false,
		isPalindrome(10),
	)
	assert.Equal(t,
		true,
		isPalindrome(0),
	)
	assert.Equal(t,
		true,
		isPalindrome(1),
	)
	assert.Equal(t,
		true,
		isPalindrome(12344321),
	)
	assert.Equal(t,
		true,
		isPalindrome(1233321),
	)
}
