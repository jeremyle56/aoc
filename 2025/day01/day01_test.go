package day01_test

import (
	"2025/day01"
	"2025/utils"
	"testing"
)

func TestSolvePuzzle1(t *testing.T) {
	input := utils.ReadInput(t, true)
	result := day01.SolvePuzzle1(input)
	utils.LogSample(t, result)

	input = utils.ReadInput(t, false)
	result = day01.SolvePuzzle1(input)
	utils.LogActual(t, result)
}

func TestSolvePuzzle2(t *testing.T) {
	input := utils.ReadInput(t, true)
	result := day01.SolvePuzzle2(input)
	utils.LogSample(t, result)

	input = utils.ReadInput(t, false)
	result = day01.SolvePuzzle2(input)
	utils.LogActual(t, result)
}