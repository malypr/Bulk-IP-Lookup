# Bulk IP Geolocation Lookup
Intentionally simple Python script to lookup the geolocation of IP addresses via IPInfo.

### Requirements:
* requests
* csv

`pip install requests csv`

### Usage:
Lookup IP Addresses from a file names "ip_list.txt and output the geolocation information to a CSV file names "out.csv"

```python lookup.py -f ip_list.txt --csv out.csv```

Usage:

```python phecon.py -h
usage: lookup.py [-h] -f ipList.txt [--csv out.csv]

Bulk IP Lookup

optional arguments:
  -h, --help     show this help message and exit
  -f ipList.txt  File containing list of IP addresses
  --csv out.csv  Output to CSV```
