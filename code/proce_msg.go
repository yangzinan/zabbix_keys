package main

import "github.com/shirou/gopsutil/load"
import "os"
import "fmt"

func main() {
	argv := os.Args
	if len(argv) != 2 {
		os.Exit(0)
	}
	t := argv[1]

	v, _ := load.Misc()
	procsRunning := v.ProcsRunning
	ProcsBlocked := v.ProcsBlocked
	if t == "o" {
		fmt.Printf("%d", procsRunning)
	} else if t == "b" {
		fmt.Printf("%d", ProcsBlocked)
	} else {
		os.Exit(0)
	}
}
