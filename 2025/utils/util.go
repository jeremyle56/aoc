package utils

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"runtime"
)

type Solver struct {
	Name string
	Run  func([]string) any
}

func Run(res any, partNumber int) {
	fmt.Printf("Part %d: \x1b[35m%v\x1b[0m\n", partNumber, res)
}

func ReadInput() string {
	_, file, _, ok := runtime.Caller(1)
	if !ok {
		log.Fatal("Failed to get caller information. Can't determine which day to load.")
	}

	content, err := os.ReadFile(filepath.Join(filepath.Dir(file), "in.txt"))
	if err != nil {
		log.Fatal("Input file not found.")
	}

	return string(content)
}
