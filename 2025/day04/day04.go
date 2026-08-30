package main

import (
	"2025/utils"
	"strings"
)

var dirs = [][]int{
	{0, 1},
	{0, -1},
	{1, 0},
	{-1, 0},
	{1, 1},
	{1, -1},
	{-1, 1},
	{-1, -1},
}

func do(input *[][]byte) int {
	res := 0

	visited := make([][]bool, len(*input))
	for i := range visited {
		visited[i] = make([]bool, len((*input)[0]))
	}

	for i := 0; i < len(*input); i++ {
		for j := 0; j < len((*input)[0]); j++ {
			if (*input)[i][j] != '@' {
				continue
			}

			cnt := 0
			for _, d := range dirs {
				nx := i + d[0]
				ny := j + d[1]
				if nx >= 0 && nx < len((*input)) && ny >= 0 && ny < len((*input)[0]) && (*input)[nx][ny] == '@' {
					cnt++
				}
			}

			if cnt < 4 {
				visited[i][j] = true
			}
		}
	}

	for i := 0; i < len(*input); i++ {
		for j := 0; j < len((*input)[0]); j++ {
			if visited[i][j] {
				res++
				(*input)[i][j] = '.'
			}
		}
	}

	return res
}

func part2(input [][]byte) any {
	res := 0

	for i := 0; i < 200; i++ {
		res += do(&input)
	}

	return res
}

func main() {
	input := strings.Split(utils.ReadInput(), "\n")

	var a [4]bool
	for _, i := range a {
		println(i)
	}

	grid := make([][]byte, len(input))
	for i, row := range input {
		grid[i] = []byte(row)
	}

	utils.Run(do(&grid), 1)

	grid = make([][]byte, len(input))
	for i, row := range input {
		grid[i] = []byte(row)
	}

	utils.Run(part2(grid), 2)
}
