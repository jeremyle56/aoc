package main

import (
	"2025/utils"
	"strconv"
	"strings"
)

func part1(input []string) any {
	res := 0

	for _, line := range input {
		l := []int{}

		for i := 0; i < len(line); i++ {
			l = append(l, int(line[i]-'0'))
		}

		largest := 0
		second := 0
		for _, i := range l {
			if i > largest {
				second = largest
				largest = i
			} else if i > second && i < largest {
				second = i
			}
		}

		next := -1
		num := largest * 10
		after := false
		for i := 0; i < len(l); i++ {
			if after {
				next = max(next, l[i])
			}

			if l[i] == largest {
				after = true
			}
		}

		if next == -1 {
			num = second * 10
			after := false
			for i := 0; i < len(l); i++ {
				if after {
					next = max(next, l[i])
				}

				if l[i] == second {
					after = true
				}
			}
		}

		res += num + next
	}

	return res
}

func solve(s string) int {
	n := len(s)
	res := []byte{}
	start := 0

	for i := 0; i < 12; i++ {
		take := start
		for j := start; j <= n-12+i; j++ {
			if s[j] > s[take] {
				take = j
				if s[take] == '9' {
					break
				}
			}
		}

		res = append(res, s[take])
		start = take + 1
	}

	a, err := strconv.Atoi(string(res[:]))
	if err != nil {
		print("BRUH")
	}

	return a
}

func part2(input []string) any {
	res := 0

	for _, line := range input {
		res += solve(line)
	}

	return res
}

func main() {
	input := strings.Split(utils.ReadInput(), "\n")

	utils.Run(part1(input), 1)
	utils.Run(part2(input), 2)
}
