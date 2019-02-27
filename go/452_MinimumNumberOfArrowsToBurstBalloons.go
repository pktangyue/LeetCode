package main

import (
    "sort"
)

func findMinArrowShots(points [][]int) int {
    if len(points) == 0 {
        return 0
    }
    // 先按照左坐标排序
    sort.Slice(points, func(i, j int) bool {
        return points[i][0] < points[j][0]
    })
    // 第一支箭右坐标，因为排序后箭的左坐标肯定包含气球的左坐标，所以无需考虑
    a_x := points[0][1]
    num := 1
    for _, v := range points {
        // 如果当前气球超出当前箭能涵盖的范围，则需要一支新的箭
        if v[0] > a_x {
            a_x = v[1]
            num += 1
        } else if v[1] < a_x {
            // 更新最小范围
            a_x = v[1]
        }
    }
    return num
}
