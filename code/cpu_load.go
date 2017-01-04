package main

import "github.com/shirou/gopsutil/load"
import "os"
import "fmt"

func main() {
	argv := os.Args
	if len(argv) != 2 {
		os.Exit(0)
	}
	pa := argv[1]
	v, _ := load.Avg()
	if pa == "1" {
		fmt.Println(v.Load1)
	} else if pa == "5" {
		fmt.Println(v.Load5)
	} else if pa == "15" {
		fmt.Println(v.Load15)
	} else {
		os.Exit(0)
	}
}
