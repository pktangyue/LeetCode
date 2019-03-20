package main

func getSum(a int, b int) int {
    for {
        a, b = a^b, a&b<<1
        if b == 0 {
            break
        }
    }
    return a
}
