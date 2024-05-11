import os,sys
from threading import Thread
from queue import Queue

import m3u8
import file_download, merge_files, index_download, pattern_matching
import time, math

global folder_name
global base_url
global file_count
global dloaded_file_count
global progressbar
global root
index_url = ''

# print(f'file name : {file_name}\n base url : {base_url} \n  {playlist.files}')


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            sub_url = self.queue.get()
            ts_file_name = pattern_matching.ts_file_name(sub_url)
            try:
                file_download.download_file(base_url, sub_url, ts_file_name, folder_name)
            finally:
                self.queue.task_done()
                global dloaded_file_count
                global file_count
                dloaded_file_count += 1


def init(index_url, no_merge = False, file_name = None, _root= None):
    global folder_name 
    global base_url
    global root
    if _root:
        root = _root
    if not file_name:
        file_name = index_download.download_index_file(index_url)
        base_url = pattern_matching.search_base_url(index_url)
    folder_name = file_name.split('.')[0]
    playlist = m3u8.load(file_name)  # this could also be an absolute filename
    qu = Queue()
    
    # initiate_progressbar()
    # create a folder with file name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    # start worker to download ts files
    for x in range(4):
        worker = DownloadWorker(qu)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    # push to worker to download
    global file_count
    global dloaded_file_count
    file_count = len(playlist.files)
    dloaded_file_count = 0
    
    
    
    for sub_url in playlist.files:
        qu.put(sub_url)

    qu.join()
    
    
    
    if not no_merge:
        merge_files.merge_files(folder_name)
        
def initiate_progressbar():
    import tkinter as tk
    from tkinter import ttk
    global progressbar
    global root
    progressbar = ttk.Progressbar(root, orient="horizontal",mode="determinate",length=1000)
    
    progressbar['maximum'] = 100
    progressbar.pack()
    root.update()
    
# def animate(steps):
#     print(steps)
#     global progressbar
#     global root
#     progressbar.step(steps)
#     root.update()
    
if __name__ == '__main__':
    index_url = sys.argv[1]
    init(index_url)

