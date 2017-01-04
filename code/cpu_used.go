package main

import (
	"fmt"

	"github.com/shirou/gopsutil/cpu"
)

func main() {
	v, _ := cpu.Percent(1000000000, true)
	fmt.Printf("%.2f", v[0])
}
