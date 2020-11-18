package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestWordBreak(t *testing.T) {
	assert.ElementsMatch(t,
		[]string{
			"a a a a a a a", "aa a a a a a", "a aa a a a a", "a a aa a a a", "aa aa a a a", "aaaa a a a", "a a a aa a a", "aa a aa a a", "a aa aa a a", "a aaaa a a", "a a a a aa a", "aa a a aa a", "a aa a aa a", "a a aa aa a", "aa aa aa a", "aaaa aa a", "a a aaaa a", "aa aaaa a", "a a a a a aa", "aa a a a aa", "a aa a a aa", "a a aa a aa", "aa aa a aa", "aaaa a aa", "a a a aa aa", "aa a aa aa", "a aa aa aa", "a aaaa aa", "a a a aaaa", "aa a aaaa", "a aa aaaa",
		},
		wordBreak("aaaaaaa", []string{"aaaa", "aa", "a"}),
	)
	assert.ElementsMatch(t,
		[]string{
			"cats and dog",
			"cat sand dog",
		},
		wordBreak("catsanddog", []string{"cat", "cats", "and", "sand", "dog"}),
	)
	assert.ElementsMatch(t,
		[]string{},
		wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
			[]string{"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"}),
	)
	assert.ElementsMatch(t,
		[]string{
			"pine apple pen apple",
			"pineapple pen apple",
			"pine applepen apple",
		},
		wordBreak("pineapplepenapple", []string{"apple", "pen", "applepen", "pine", "pineapple"}),
	)
	assert.ElementsMatch(t,
		[]string{},
		wordBreak("catsandog", []string{"cats", "dog", "sand", "and", "cat"}),
	)
}
