package cache

import (
	"context"
	"fmt"
	"github.com/redis/go-redis/v9"
	"log"
	"strconv"
)

type Device struct {
	ID                 string `json:"id"`
	MaintenanceMode    bool   `json:"maintenance_mode"`
	Controller         string `json:"controller"`
	Console            string `json:"console"`
	ConsolePort        string `json:"console_port"`
	ConsolePassword    string `json:"console_password"`
	SharedDirectory    string `json:"shared_directory"`
	SharedUsername     string `json:"shared_username"`
	SharedPassword     string `json:"shared_password"`
	MobileNumber       string `json:"mobile_number"`
	Model              string `json:"model"`
	IPv4Address        string `json:"ipv4_address"`
	IMEI1              string `json:"imei_1"`
	IMEI2              string `json:"imei_2"`
	OperatorNumeric    string `json:"operator_numeric"`
	OperatorIsoCountry string `json:"operator_iso_country"`
	OperatorAlpha      string `json:"operator_alpha"`
	MacAddress         string `json:"mac_address"`
	InternalIP         string `json:"internal_ip"`
	Status             string `json:"status"`
}

const cacheDeviceKeyBase = "vharness:device"

var cacheDeviceKeys = [...]string{
	"shared_password",
	"status",
	"console_port",
	"shared_username",
	"console_password",
	"console",
	"maintenance_mode",
	"shared_directory",
}

func GetList(key string) []string {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "192.168.50.141:6379", // make this configurable
		Password: "",                    // no password set
		DB:       0,                     // use default DB
	})

	val, err := rdb.LRange(ctx, key, 0, -1).Result()
	if err != nil {
		panic(err)
	}
	log.Println("key", val)

	return val
}

func GetDevice(serial string) *Device {
	deviceKey := fmt.Sprintf("%s:%s", cacheDeviceKeyBase, serial)
	device := &Device{
		ID:              serial,
		MaintenanceMode: getBool(fmt.Sprintf("%s:%s", deviceKey, "maintenance_mode")),
		Controller:      "adb",
		Console:         getString(fmt.Sprintf("%s:%s", deviceKey, "console")),
		ConsolePort:     getString(fmt.Sprintf("%s:%s", deviceKey, "console_port")),
		ConsolePassword: getString(fmt.Sprintf("%s:%s", deviceKey, "console_password")),
		SharedDirectory: getString(fmt.Sprintf("%s:%s", deviceKey, "shared_directory")),
		SharedUsername:  getString(fmt.Sprintf("%s:%s", deviceKey, "shared_username")),
		SharedPassword:  getString(fmt.Sprintf("%s:%s", deviceKey, "shared_password")),
		Status:          getString(fmt.Sprintf("%s:%s", deviceKey, "status")),
	}
	return device
}

func getBool(key string) bool {
	ctx := context.Background()
	rdb := redis.NewClient(&redis.Options{
		Addr:     "192.168.50.141:6379", // make this configurable
		Password: "",                    // no password set
		DB:       0,                     // use default DB
	})
	val, err := rdb.Get(ctx, key).Result()
	if err != nil {
		log.Println(err)
		return false
	}

	boolVal, err := strconv.ParseBool(val)
	if err != nil {
		log.Println(err)
		return false
	}
	return boolVal
}

func getString(key string) string {
	ctx := context.Background()
	rdb := redis.NewClient(&redis.Options{
		Addr:     "192.168.50.141:6379", // make this configurable
		Password: "",                    // no password set
		DB:       0,                     // use default DB
	})
	val, err := rdb.Get(ctx, key).Result()
	if err != nil {
		log.Println(err)
		return ""
	}
	return val
}
