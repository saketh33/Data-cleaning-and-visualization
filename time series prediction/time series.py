import socket as s
hostn=s.gethostname()
ipad=s.gethostbyname(hostn)
a=s.gethostbyaddr(hostn)
print(a)
print(hostn)
print(ipad)