# by luffycity.com



import json



# d={"name":"alex"}
#
#
# s=json.dumps(d)
#
#
# with open("json.txt","w") as f:
#     f.write(s)


with open("data.txt","r") as f:
    data=f.read()

data=json.loads(data)

print(data)