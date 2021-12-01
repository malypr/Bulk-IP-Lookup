import requests,conf,argparse,json,csv

def L_IPInfo(ip):
    a=""
    if conf.CONF['ipinfo']['api_key']!="":
        a="?token="+conf.CONF['ipinfo']['api_key']
    r=json.loads(requests.get(conf.CONF['ipinfo']['endpoint']+ip+"/json"+a).text)
    return r
if __name__=="__main__":
    a=argparse.ArgumentParser(description="Bulk IP Lookup")
    a.add_argument("-f",required=True,metavar="ip_list.txt",help="List of IPs")
    a.add_argument("--csv",metavar="output.csv",help="Output to CSV File")
    a.add_argument("--ipinfo",action="store_true",help="Lookup in IPInfo")
    a=a.parse_args()
    with open(a.f) as f:
        o=[]
        for l in f:
            if a.ipinfo==True:
                o.append(L_IPInfo(l.split("\n")[0]))
        if a.csv!=None:
            with open(a.csv,'w', newline='\n') as x:
                v=["ip","hostname","anycast","city","region","country","org","postal"]
                w=csv.DictWriter(x,fieldnames=v)
                w.writeheader()
                for i in o:
                    b={}
                    for y in v:
                        if y in i:
                            b[y]=i[y]
                    w.writerow(b)
        else:
            for i in o:
                print(i)
