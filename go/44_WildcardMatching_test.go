package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsMatch(t *testing.T) {
	assert.Equal(t,
		true,
		isMatch("aaaa", "***a"),
	)
	assert.Equal(t,
		false,
		isMatch("aa", "a"),
	)
	assert.Equal(t,
		false,
		isMatch(
			"abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
			"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb",
		),

	)
	assert.Equal(t,
		true,
		isMatch("", "*****"),
	)
	assert.Equal(t,
		true,
		isMatch("adceb", "*a*b"),
	)
	assert.Equal(t,
		false,
		isMatch("acdcb", "a*c?b"),
	)
	assert.Equal(t,
		true,
		isMatch("aa", "*"),
	)
	assert.Equal(t,
		false,
		isMatch("cb", "?a"),
	)
}
