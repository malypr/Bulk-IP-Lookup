import requests,argparse,json,csv
def IPInfo(ip,fields,token=None):
    if token!=None:
        append="?token="+token
    else:
        append=''
    r=json.loads(requests.get("https://ipinfo.io/"+ip+"/json"+append).text)
    o={}
    for field in fields:
        if field in r:
            o[field]=r[field]
    return o
if __name__=="__main__":
    prs=argparse.ArgumentParser(description="Bulk IP Lookup")
    prs.add_argument("-f",required=True,metavar="ipList.txt",help="File containing list of IP addresses")
    prs.add_argument("--csv",required=False,metavar="out.csv",help="Output to CSV")
    arg=prs.parse_args()
    fields=['ip','org','hostname','city','region','country','org','postal']
    with open(arg.f) as f:
        if arg.csv != None:
            with open(arg.csv,'w') as x:
                w=csv.DictWriter(x,fieldnames=fields)
                w.writeheader()
                for i in f:
                    w.writerow(IPInfo(i.split("\n")[0],fields))
        else:
            for i in f:
                print(IPInfo(i.split("\n")[0],fields))
