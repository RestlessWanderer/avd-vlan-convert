# avd-vlan-convert
This script takes a range input of vlans directly from a configuration and converts it to the l2vlans data model for AVD outputting it to a vlan.txt file.

Example input:  1-12,15,20,23-30,40,47,145

Example output: vlan.txt

```yaml
  - id: 1
    name: "1"
    tags: [ "1" ]
  - id: 2
    name: "2"
    tags: [ "2" ]
  - id: 3
    name: "3"
    tags: [ "3" ]
  - id: 4
    name: "4"
    tags: [ "4" ]
  - id: 5
    name: "5"
    tags: [ "5" ]
  - id: 6
    name: "6"
    tags: [ "6" ]
  - id: 7
    name: "7"
    tags: [ "7" ]
  - id: 8
    name: "8"
    tags: [ "8" ]
  - id: 9
    name: "9"
    tags: [ "9" ]
  - id: 10
    name: "10"
    tags: [ "10" ]
  - id: 11
    name: "11"
    tags: [ "11" ]
  - id: 12
    name: "12"
    tags: [ "12" ]
  - id: 15
    name: "15"
    tags: [ "15" ]
  - id: 20
    name: "20"
    tags: [ "20" ]
  - id: 23
    name: "23"
    tags: [ "23" ]
  - id: 24
    name: "24"
    tags: [ "24" ]
  - id: 25
    name: "25"
    tags: [ "25" ]
  - id: 26
    name: "26"
    tags: [ "26" ]
  - id: 27
    name: "27"
    tags: [ "27" ]
  - id: 28
    name: "28"
    tags: [ "28" ]
  - id: 29
    name: "29"
    tags: [ "29" ]
  - id: 30
    name: "30"
    tags: [ "30" ]
  - id: 40
    name: "40"
    tags: [ "40" ]
  - id: 47
    name: "47"
    tags: [ "47" ]
  - id: 145
    name: "145"
    tags: [ "145" ]
```


**Special thanks to the Wizard for your help!**
