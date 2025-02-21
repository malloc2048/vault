package main

import (
	"log"
	"net"
	"net/http"
	"net/rpc"
)

type TimeServer int64

func main() {
    // initialize settings
    //settings := config.NewSettings()

    // create RPC server
    timeserver := new(TimeServer)

    // register RPC server
    _ = rpc.Register(timeserver)
    rpc.HandleHTTP()

    // listen for requests on port 1234
	l, e := net.Listen("tcp", ":2233")
	if e != nil {
		log.Fatal("listen error:", e)
	}
	_ = http.Serve(l, nil)
}
