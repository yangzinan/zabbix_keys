package main

import (
	"fmt"

	"github.com/shirou/gopsutil/mem" //引入内存操作库
)

func main() {
	v, _ := mem.VirtualMemory()
	fmt.Printf("%.2f", v.UsedPercent)
}
