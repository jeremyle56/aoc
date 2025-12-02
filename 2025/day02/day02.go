package main

import (
	"2025/utils"
	"log"
	"strconv"
	"strings"
)

func isRepeated(s string, part2 bool) bool {
	n := len(s)
	if n <= 1 || (!part2 && n%2 != 0) {
		return false
	}

	i := 1
	if !part2 {
		i = n / 2
	}

	for ; i <= n/2; i++ {
		if n%i == 0 {
			ss := s[:i]
			rs := strings.Repeat(ss, n/i)

			if rs == s {
				return true
			}
		}
	}

	return false
}

func solve(input []string, part2 bool) any {
	res := 0

	for _, r := range input {
		thing := strings.Split(r, "-")

		i, err := strconv.Atoi(thing[0])
		if err != nil {
			log.Fatalf("Error converting string to int: %v", err)
		}

		hi, err := strconv.Atoi(thing[1])
		if err != nil {
			log.Fatalf("Error converting string to int: %v", err)
		}

		for ; i <= hi; i++ {
			num := strconv.Itoa(i)

			if isRepeated(num, part2) {
				res += i
			}
		}
	}

	return res
}

func main() {
	input := strings.Split(utils.ReadInput(), ",")

	utils.Run(solve(input, false), 1)
	utils.Run(solve(input, true), 2)
}
