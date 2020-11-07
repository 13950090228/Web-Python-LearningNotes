

import subprocess

res=subprocess.Popen("ipconfig",
                     shell=True,
                     stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE)


print(res.stdout.read().decode("gbk"))




