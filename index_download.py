import file_download
import pattern_matching


def download_index_file(base_url):
    file_name = pattern_matching.search_file_name(base_url)
    file_download.download_file(base_url, '',file_name ,'')
    return file_name
