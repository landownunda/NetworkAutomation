import json

jsonObject = {
  "_exclude": [],
  "vrf": {
    "default": {
      "address_family": {
        "ipv4": {
          "routes": {
            "0.0.0.0/0": {
              "active": 'true',
              "metric": 0,
              "next_hop": {
                "next_hop_list": {
                  "1": {
                    "index": 1,
                    "next_hop": "10.10.20.254",
                    "outgoing_interface": "GigabitEthernet1"
                  }
                }
              },
              "route": "0.0.0.0/0",
              "route_preference": 1,
              "source_protocol": "static",
              "source_protocol_codes": "S*"
            },
            "1.1.1.1/32": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "Loopback0": {
                    "outgoing_interface": "Loopback0"
                  }
                }
              },
              "route": "1.1.1.1/32",
              "source_protocol": "connected",
              "source_protocol_codes": "C"
            },
            "1.2.3.4/32": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "Loopback601": {
                    "outgoing_interface": "Loopback601"
                  }
                }
              },
              "route": "1.2.3.4/32",
              "source_protocol": "connected",
              "source_protocol_codes": "C"
            },
            "10.10.20.0/24": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "GigabitEthernet1": {
                    "outgoing_interface": "GigabitEthernet1"
                  }
                }
              },
              "route": "10.10.20.0/24",
              "source_protocol": "connected",
              "source_protocol_codes": "C"
            },
            "10.10.20.48/32": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "GigabitEthernet1": {
                    "outgoing_interface": "GigabitEthernet1"
                  }
                }
              },
              "route": "10.10.20.48/32",
              "source_protocol": "local",
              "source_protocol_codes": "L"
            },
            "15.25.35.45/32": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "Loopback555": {
                    "outgoing_interface": "Loopback555"
                  }
                }
              },
              "route": "15.25.35.45/32",
              "source_protocol": "connected",
              "source_protocol_codes": "C"
            },
            "192.0.2.0/24": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "GigabitEthernet1": {
                    "outgoing_interface": "GigabitEthernet1"
                  }
                }
              },
              "route": "192.0.2.0/24",
              "source_protocol": "static",
              "source_protocol_codes": "S"
            },
            "203.0.113.0/24": {
              "active": 'true',
              "metric": 0,
              "next_hop": {
                "next_hop_list": {
                  "1": {
                    "index": 1,
                    "next_hop": "10.10.20.254"
                  }
                }
              },
              "route": "203.0.113.0/24",
              "route_preference": 1,
              "source_protocol": "static",
              "source_protocol_codes": "S"
            },
            "74.74.74.1/32": {
              "active": 'true',
              "next_hop": {
                "outgoing_interface": {
                  "Loopback74": {
                    "outgoing_interface": "Loopback74"
                  }
                }
              },
              "route": "74.74.74.1/32",
              "source_protocol": "connected",
              "source_protocol_codes": "C"
            }
          }
        }
      }
    }
  }
}

routeData = jsonObject['vrf']['default']['address_family']['ipv4']['routes']
routeTableLength = len(routeData)

print("*********************************************")
print("There is " + str(routeTableLength) + " routes currently in the Global Route Table")

for routes in routeData:
    if routes == "0.0.0.0/0":
        print(routes + ": The Next Hop is - " + str(routeData['0.0.0.0/0']['next_hop']['next_hop_list']['1']['next_hop']))
    else:
        print(routes)
