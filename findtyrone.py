import re
import argparse
import subprocess
import numpy as np
from multiprocessing import Process, Array

def ordinary_scanner(hosts, a, min_, tried):
    pattern = re.compile(r"host key algorithms:")
    for host in hosts:
        #print(f"At {host}")
        tried[host - min_] = 1
        process = subprocess.Popen(f"ssh user@10.222.72.{host} -vvv".split(),stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
            out,err = process.communicate()
            if len(out.decode()) > 0:
                a[host - min_] = 1
            if len(pattern.findall(out.decode())) > 0:
                a[host - min_] = 1
            if len(pattern.findall(err.decode())) > 0:
                a[host - min_] = 1
        else:
            out,err = process.communicate()
            if len(out.decode()) > 0:
                a[host - min_] = 1
            if len(pattern.findall(out.decode())) > 0:
                a[host - min_] = 1
            if len(pattern.findall(err.decode())) > 0:
                a[host - min_] = 1

def nmap_scanner(hosts, a, min_, tried):
    pattern = re.compile(r"22/tcp.*open.*(?:ssh|tcpwrapped)")
    host_pattern = re.compile(r"\d+\.\d+\.\d+\.(\d+)")
    for ip in hosts:
        #print(f"At {host}")
        m = host_pattern.match(ip)
        host = int(m.group(1))
        tried[host - min_] = 1
        process = subprocess.Popen(f"nmap -sV -Pn -p 22 {ip}".split(),stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            out,err = process.communicate()
            if len(pattern.findall(out.decode())) > 0:
                a[host - min_] = 1
            if len(pattern.findall(err.decode())) > 0:
                a[host - min_] = 1
        else:
            out,err = process.communicate()
            if len(pattern.findall(out.decode())) > 0:
                a[host - min_] = 1
            if len(pattern.findall(err.decode())) > 0:
                a[host - min_] = 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dont-use-nmap","-dn",default=False,action='store_true')
    parser.add_argument("--min",default=100,type=int)
    parser.add_argument("--max",default=255,type=int)
    parser.add_argument("--nworkers","-w",default=12,type=int)
    parser.add_argument("--scan-subnet","-s",default=False,action='store_true')
    args = parser.parse_args()
    use_nmap = not args.dont_use_nmap
    nworkers = args.nworkers
    min_ = args.min
    max_ = args.max
    if use_nmap:
        host_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)")
        if not args.scan_subnet:
            process = subprocess.Popen(f"nmap -sL -n 10.222.72.{min_}-{max_}".split(), stdout=subprocess.PIPE)
            out,_ = process.communicate()
            out = out.decode()
            host_match = host_pattern.findall(out)
        else:
            min_ = 0
            process = subprocess.Popen(f"nmap -sL -n 10.222.72.1/24".split(), stdout=subprocess.PIPE)
            out,_ = process.communicate()
            out = out.decode()
            host_match = host_pattern.findall(out)
        nhosts = len(host_match)
        bucket_size = nhosts // nworkers + 1
        processes = []
        arr = Array('i',[0 for _ in range(nhosts)])
        tried = Array('i',[0 for _ in range(nhosts)])
        for n in range(nworkers):
            hosts = host_match[n * bucket_size:min((n + 1) * bucket_size,nhosts)]
            processes.append(Process(target=nmap_scanner,args=(hosts,arr,min_,tried)))
            processes[-1].start()
        for p in processes:
            p.join()
        print("Hosts found:")
        for idx, a in enumerate(arr):
            if a == 1:
                print(f"{host_match[idx]}")
    else:
        if args.scan_subnet:
            raise NotImplementedError("Scan subnet option not implemented for"
                    " non-nmap usage. If you want to scan the subnet, enter min"
                    " and max host accordingly.")
        bucket_size = (max_ - min_) // nworkers + 1
        processes = []
        arr = Array('i',[0 for _ in range(min_,max_)])
        tried = Array('i',[0 for _ in range(min_,max_)])
        for n in range(nworkers):
            hosts = range(min_ + n * bucket_size, min(min_ + (n + 1) * bucket_size, max_))
            processes.append(Process(target=ordinary_scanner,args=(hosts,arr,min_,tried)))
            processes[-1].start()
        for p in processes:
            p.join()
        print("\nHosts found:")
        for idx, a in enumerate(arr):
            if a == 1:
                print(f"10.222.72.{idx+min_}")
    if np.all(np.array(tried)==1):
        print("Tried all")
    else:
        print("Some left")
        print(f"{np.array(tried) = }")
if __name__=="__main__":
    main()
