package api

import (
	"encoding/json"
	"github.com/gorilla/mux"
	"harness/cache"
	"log"
	"net/http"
)

func getDeviceSerials(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	cachedDevices := cache.GetList("vharness:devices") // todo: make this key a constant

	err := json.NewEncoder(w).Encode(cachedDevices)
	if err != nil {
		return
	}
}

func getDevice(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)
	serial := vars["serial"]

	device := cache.GetDevice(serial)
	deviceData, err := json.Marshal(device)
	if err != nil {
		return
	}

	err = json.NewEncoder(w).Encode(string(deviceData))
	if err != nil {
		return
	}
}

func Start() {
	r := mux.NewRouter()
	r.HandleFunc("/devices", getDeviceSerials).Methods("GET")
	r.HandleFunc("/devices/{serial}", getDevice).Methods("GET")

	log.Fatal(http.ListenAndServe(":8000", r))
}
