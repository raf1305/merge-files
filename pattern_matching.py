import re


def search_file_name(s):
    m = re.search(r'([\w-])+.m3u8', s)
    return m[0]

'''
    sample: hoichoi,chorki
'''


def search_base_url(s):
    m = re.search(r'([\w./:,-_=]*/)', s)
    return m[0]


def ts_file_name(s):
    m = re.search(r'([\w-])+.ts', s)
    return m[0]

