import re,fractions as f
exec('a,b,c=map(int,re.split("\D",input())[::2]);print("yneos"[c%f.gcd(a,b)>0::2]);'*int(input()))
