#!/usr/bin/env python3
"""rot13_tool - ROT13/ROTn encoding."""
import sys,argparse,json
def rotn(text,n=13):
    r=[]
    for c in text:
        if c.isalpha():
            b=ord("A") if c.isupper() else ord("a")
            r.append(chr((ord(c)-b+n)%26+b))
        else:r.append(c)
    return "".join(r)
def main():
    p=argparse.ArgumentParser(description="ROT13/ROTn")
    p.add_argument("text");p.add_argument("-n",type=int,default=13)
    args=p.parse_args()
    print(json.dumps({"input":args.text,"n":args.n,"output":rotn(args.text,args.n)}))
if __name__=="__main__":main()
