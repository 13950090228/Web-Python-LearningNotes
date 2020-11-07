import hashlib

#
md5=hashlib.md5(b'kanghang')
md5.update(b"hello")
#md5.update(b"yuan")

print(md5.hexdigest())
print(len(md5.hexdigest()))

##helloyuan:   d843cc930aa76f7799bba1780f578439
##             d843cc930aa76f7799bba1780f578439
#
##############################################
#
#md=hashlib.md5()
#
#with open("ssh_client.py","rb") as f:
#    for line in f:
#        md5.update(line)
#
#print(md.hexdigest()) # f.read()
#md5=hashlib.md5(b)
#md5.update(b'hello')
#print(md5.hexdigest())

