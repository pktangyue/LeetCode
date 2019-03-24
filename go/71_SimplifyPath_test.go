package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestSimplifyPath(t *testing.T) {
    assert.Equal(t,
        "/home",
        simplifyPath("/home/"),
    )
    assert.Equal(t,
        "/",
        simplifyPath("/../"),
    )
    assert.Equal(t,
        "/home/foo",
        simplifyPath("/home//foo/"),
    )
    assert.Equal(t,
        "/c",
        simplifyPath("/a/./b/../../c/"),
    )
    assert.Equal(t,
        "/c",
        simplifyPath("/a/../../b/../c//.//"),
    )
    assert.Equal(t,
        "/a/b/c",
        simplifyPath("/a//b////c/d//././/.."),
    )
}
