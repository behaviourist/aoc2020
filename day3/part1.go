package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	var lines []string

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var count, a, b = 1, len(lines), len(lines[0])
	var m = make([][]int, 5)

	m[0] = []int{1, 3}
	m[1] = []int{1, 1}
	m[2] = []int{1, 5}
	m[3] = []int{1, 7}
	m[4] = []int{2, 1}

	for _, e := range m {
		var x, y, current = 0, 0, 0

		for x < a {
			if lines[x][y] == '#' {
				current++
			}
			x += e[0]
			y += e[1]
			y %= b
		}

		count*=current
		// break (part1)
	}

	fmt.Println(count)
}
