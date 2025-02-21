package config

import (
	"flag"
)

const (
	DefaultIpv6Host      = "::1"
	DefaultIpv4Host      = "localhost"
	DefaultRegistryHost  = "255.255.255.255"
	DefaultMetricsPort   = 8002
	DefaultServerPort    = 18812
	DefaultServerSslPort = 18821
	RegistryPort         = 18811
)

type Settings struct {
	Mode          string
	Port          int
	Host          string
	IPV6          bool
	EnableMetrics bool
	MetricsPort   int
	LogFile       string
	Quiet         bool
	SSLKeyFile    string
	SSLCertFile   string
	SSLCAFile     string
	AutoRegister  bool
	RegistryType  string
	RegistryPort  int
	RegistryHost  string
}

func (s *Settings) validate() {
	// todo: validate parsed command line args are in range
}

func NewSettings() Settings {
	settings := Settings{}
	flag.StringVar(&settings.Mode, "mode", "threaded", "The serving mode (threaded, forking, or 'stdio' for inetd, etc.)")
	flag.IntVar(&settings.Port, "port", DefaultServerPort, "The TCP listener port")
	flag.StringVar(&settings.Host, "host", DefaultIpv4Host, "The host to bind to")
	flag.BoolVar(&settings.IPV6, "ipv6", false, "Enable IPv6")
	flag.BoolVar(&settings.EnableMetrics, "metrics", false, "Enable Prometheus metrics")
	flag.IntVar(&settings.MetricsPort, "metrics_port", DefaultMetricsPort, "The Prometheus metrics port")
	flag.StringVar(&settings.LogFile, "log_file", "stderr", "Specify the log file to use")
	flag.BoolVar(&settings.Quiet, "quiet", false, "Quiet mode (only errors will be logged)")
	flag.StringVar(&settings.SSLKeyFile, "ssl_key_file", "", "The SSL key file")
	flag.StringVar(&settings.SSLCertFile, "ssl_cert_file", "", "The SSL certificate file")
	flag.StringVar(&settings.SSLCAFile, "ssl_ca_file", "", "The SSL CA file")
	flag.BoolVar(&settings.AutoRegister, "auto_register", false, "Enable automatic registration")
	flag.StringVar(&settings.RegistryType, "registry_type", "docker", "The registry type")
	flag.IntVar(&settings.RegistryPort, "registry_port", RegistryPort, "The TCP listener port")
	flag.StringVar(&settings.RegistryHost, "registry_host", DefaultRegistryHost, "The registry host")

	flag.Parse()
	settings.validate()

	return settings
}
