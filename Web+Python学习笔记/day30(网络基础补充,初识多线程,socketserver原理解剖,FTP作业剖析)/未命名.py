import uuid
import requests
import time
import threading

start=time.time()
lst=['https://www3.autoimg.cn/newsdfs/g1/M0A/49/2D/120x90_0_autohomecar__ChsEj13Kjw-AKySoAACEnDgajfQ186.jpg',
     'https://www3.autoimg.cn/newsdfs/g24/M0B/90/4B/120x90_0_autohomecar__ChsEeV3Kg7iAeFsaAAGvgowE1W0270.jpg',
     'https://www2.autoimg.cn/newsdfs/g28/M01/30/42/120x90_0_autohomecar__ChsEnl3KeqiAAUCbAAIeSNLhPeE263.jpg']

def task(url):
    ret=requests.get(url)
    data=ret.content
    filename=uuid.uuid4()
    with open(str(filename)+'.jpg',mode='wb') as f:
        f.write(data)
for url in lst:
    t=threading.Thread(target=task,args=(url,))
    t.start()
        
end=time.time()
print(end-start)