package main

import (
    "strings"
)

func simplifyPath(path string) string {
    stacks := []string{}
    for _, v := range strings.Split(path, "/") {
        if v == "." || v == "" {
            continue
        } else if v == ".." {
            if len(stacks) > 0 {
                stacks = stacks[:len(stacks)-1]
            }
        } else {
            stacks = append(stacks, v)
        }
    }
    return "/" + strings.Join(stacks, "/")
}
