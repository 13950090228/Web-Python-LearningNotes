import struct


res=struct.pack("i",5415131)

print(res)
print(len(res))


obj=struct.unpack("i",res)
print(obj[0])
