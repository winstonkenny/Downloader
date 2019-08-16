from Download import Downloader
import time
from multiprocessing import Process

def download(url, path):
    down = Downloader(url, path)
    down.set_filename('7771234.jpg')
    down.isBar = True
    down.start()

p1 = Process(target=download, args = ('http://58.218.213.204:88/uploads/tu/201509171/5obepvmsj3y.jpg','./abc/123456.jpg'))
p1.start()
p1.join()


#while True:
#    if down.status_index in [1, 3, 4, 6]:
#        print(down.status_source[down.status_index])
#        print('not done')
#        break
#    else:
#        if down.status_index == 2:
#            break
#        pass

print("all ok")
        

