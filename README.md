# Bulk-IP-Lookup
Super quick and simple Python 3 script to get geolocations of IP addresses via IPInfo.

### Requirements:
* requests
* csv

`pip install requests csv`

### Usage:
Example: `python lookup.py -f ip_list.txt --csv test_out.csv --ipinfo`

`-f ip_list.txt | Input file containing a \n separated list of IP addresses`

`--ipinfo |  Lookup IPs on IPInfo`

`--csv file.csv | Output to CSV`

You can input an API key for IPInfo in the `conf.py`
