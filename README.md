### A downloader for Python3

# How to use it

`from Download import Downloader`

`down = Downloaader(url, path)`

#path eg:`/home/test_download.jpg`

`down.isBar=Ture`

#This statement can make a progress bar in bash terminal when you downloading file. Default is False.

`down.start()`

#This statement to run a download thread after you created one object for download.

`down.stop()`

#It's a way to stop this thread for download.
