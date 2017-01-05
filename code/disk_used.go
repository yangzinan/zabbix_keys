package main

import (
	"fmt"
	"os"

	"github.com/shirou/gopsutil/disk"
)

const MSG = "[%s]_Status: %s - Total:%vG, Free:%vG, UsedPercent:%f%% | UsedPercent=%f;%f;0;100\n"

func main() {
	argv := os.Args
	if len(argv) != 2 {
		os.Exit(0)
	}
	d := argv[1]
	v, _ := disk.Usage(d)
	UsedPercent := v.UsedPercent
	fmt.Printf("%.2f", UsedPercent)
}
