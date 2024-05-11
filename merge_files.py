import time
import subprocess
from pathlib import Path
from natsort import os_sorted
import os,sys
import shutil
import datetime
cwd = os.getcwd()
import ffmpeg

def exception_log(e):
    with open('error_log.txt', 'a') as error:
        error.write(f'{datetime.datetime.now()} : f{repr(e)}\n')

def success_log(start_time, end_time, file_size):
    with open('success_log.txt', 'a') as success:
        success.write(f'{datetime.datetime.now()} : {end_time - start_time}s - {file_size}mb\n')


def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
    print(f'Removed {path}')


def merge_files(folder_name):
    try:
        start_time = time.time()
        with open(f'{folder_name}/{folder_name}.ts', 'wb') as merged:
            for i in os_sorted(os.listdir(f'{cwd}/{folder_name}')):
                if i.endswith('.ts') and i != f'{folder_name}.ts':
                    with open(f'{folder_name}/{i}', 'rb') as mergefile:
                        shutil.copyfileobj(mergefile, merged)
                    remove(f'{folder_name}/{i}')
        end_time = time.time()
        # with open(f'files.txt', 'w') as f:
        #     f.write(f"file '{folder_name}/{folder_name}.ts'\n")
        # subprocess.run(f'ffmpeg -f concat -safe 0 -i files.txt -c copy {folder_name}/{folder_name}.mp4') #very fast but need to create a file
        # subprocess.run(['ffmpeg', '-i', f'{folder_name}/{folder_name}.ts', f'{folder_name}/{folder_name}.mp4']) #takes long time
        # subprocess.run(f'ffmpeg -i {folder_name}/{folder_name}.ts -filter_complex "concat=n=1:v=0:a=1" -y {folder_name}/{folder_name}.mp4') #takes longer tie
        # subprocess.run(f'ffmpeg -f {folder_name}/{folder_name}.ts -c copy {folder_name}/{folder_name}.mp4') #very fast but need to create a file
        input_file = f'{folder_name}/{folder_name}.ts'
        output_file = f'{folder_name}/{folder_name}.mp4'
        # subprocess.run(['ffmpeg', '-i', f'concat:{input_file}', '-c', 'copy', output_file]) #works as fast
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='copy', acodec='copy')
            .overwrite_output()
            .run()
        )
        remove(f'{folder_name}/{folder_name}.ts')
        # (
        # ffmpeg
        # .input(input_file)
        # .output(output_file, vcodec='libx264', acodec='aac', strict='experimental')
        # .run()) # slow
        
        file_size = Path(f'{folder_name}/{folder_name}.mp4').stat().st_size / (1000 * 1000)
        success_log(start_time,end_time, file_size)
        return file_size
    except Exception as e:
        exception_log(e)
        return repr(e);

if __name__ == '__main__':
    folder_name_ = sys.argv[1]
    merge_files(folder_name_)
