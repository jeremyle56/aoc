package day01

import (
	"log"
	"math"
	"strconv"
	"strings"
)

func SolvePuzzle1(input string) int {
	res, start := 0, 50

	for _, line := range strings.Split(input, "\n") {
		num, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Fatalf("Error converting string to int: %v", err)
		}

		if line[0] == 'L' {
			start += num
			start %= 100
		} else {
			start -= num
			start %= 100
		}

		if start == 0 {
			res++
		}
	}

	return res
}

func SolvePuzzle2(input string) int {
	res, start := 0, 50

	for _, line := range strings.Split(input, "\n") {
		num, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Fatalf("Error converting string to int: %v", err)
		}

		if line[0] == 'R' {
			num = -num
		}

		res += int(math.Abs(float64(num))) / 100
		r := int(math.Abs(float64(num))) % 100

		if (num > 0 && start+r >= 100) || (num < 0 && start-r < 0) {
			res++
		}

		start += num
		start %= 100
	}

	return res
}
