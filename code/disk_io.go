package main

import (
	"fmt"

	"os"

	"github.com/shirou/gopsutil/disk"
)

func main() {
	argv := os.Args
	if len(argv) != 3 {
		os.Exit(0)
	}
	disk_name := argv[2]
	t := argv[1]
	v, _ := disk.IOCounters()
	if t == "r" {
		fmt.Printf("%d", int(v[disk_name].ReadBytes)>>10)
	} else if t == "w" {
		fmt.Printf("%d", int(v[disk_name].WriteBytes)>>10)
		fmt.Println(v)
	} else {
		os.Exit(0)
	}
}
