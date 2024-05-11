import shutil
import os, sys
import subprocess
import ffmpeg
from pathlib import Path
from natsort import os_sorted
import time
cwd = os.getcwd()
files = []


def convert_to_mp4(file_name, folder_name):
    print(os.getcwd())
    if os.path.exists(f'{folder_name}/{file_name}.ts'):
        print("File Exists")

    print(f'Converting {file_name}')
    converted_file_name = file_name.split('.')[0]
    subprocess.run(['ffmpeg', '-i', f'{folder_name}/{file_name}.ts', f'{folder_name}/{converted_file_name}.mp4'])
    print(f'Conversion {file_name} done.')


def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
    print(f'Removed {path}')

def generate_file(folder_name):
    with open(f'files.txt', 'w') as f:
        for i in os_sorted(os.listdir(f'{cwd}/{folder_name}')):
            if i.endswith('.ts') and i != f'{folder_name}.mp4':
                f.write(f"file '{folder_name}/{i}'\n")


def merge_files(folder_name):
    try:
        generate_file(folder_name)
        # os.system(f'ffmpeg -f concat -safe 0 -i files.txt -c copy {folder_name}/{folder_name}.mp4')
        subprocess.run(f'ffmpeg -f concat -safe 0 -i files.txt -c copy {folder_name}/{folder_name}.mp4')
        return Path(f'{folder_name}/{folder_name}.mp4').stat().st_size / (1000 * 1000)

    except Exception as e:
        print(repr(e))
        return repr(e)


def merge_files2(folder_name):
    try:
        start_time = time.time()
        with open(f'{folder_name}/{folder_name}.ts', 'wb') as merged:
            for i in os_sorted(os.listdir(f'{cwd}/{folder_name}')):
                if i.endswith('.ts') and i != f'{folder_name}.ts':
                    with open(f'{folder_name}/{i}', 'rb') as mergefile:
                        shutil.copyfileobj(mergefile, merged)
                    remove(f'{folder_name}/{i}')
        end_time = time.time()
        with open(f'files.txt', 'w') as f:
            f.write(f"file '{folder_name}/{folder_name}.ts'\n")
        subprocess.run(f'ffmpeg -f concat -safe 0 -i files.txt -c copy {folder_name}/{folder_name}.mp4')
        remove(f'{folder_name}/{folder_name}.ts')
        # print(files)

        return Path(f'{folder_name}/{folder_name}.mp4').stat().st_size / (1000 * 1000)
    except Exception as e:
        print(repr(e))
        return repr(e)

# to convert ts file to mp4 but takes long time
# subprocess.run(['ffmpeg', '-i', 'p/merged.ts', 'p/merged.mp4'])


if __name__ == '__main__':
    folder_name_ = sys.argv[1]
    start_time = time.time()
    file_size = merge_files2(folder_name_)
    end_time = time.time()
    print(end_time-start_time)
    print(file_size)
