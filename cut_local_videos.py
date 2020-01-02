import argparse
import glob
import json
import os
import shutil
import subprocess
import uuid
from collections import OrderedDict

from joblib import delayed
from joblib import Parallel
import pandas as pd
from tqdm import tqdm

if __name__ == '__main__':
    root = ''
    raw_videos = glob.glob(root)
    for raw_video in tqdm(raw_videos):
        start_time = raw_video.split('_')
        end_time = raw_video.split('_')
        output_filename = raw_video.replace('')
        tmp_filename = raw_video.replace('')
        # Construct command to trim the videos (ffmpeg required).
        command = ['ffmpeg',
                   '-i', '"%s"' % tmp_filename,
                   '-ss', str(start_time),
                   '-t', str(end_time - start_time),
                   '-c:v', 'libx264', '-c:a', 'copy',
                   '-threads', '1',
                   '-loglevel', 'panic',
                   '"%s"' % output_filename]
        command = ' '.join(command)
        try:
            output = subprocess.check_output(command, shell=True,
                                             stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as err:
            print (err.output)

        # Check if the video was successfully saved.
        status = os.path.exists(output_filename)
        os.remove(tmp_filename)
        print ('cut >> '+raw_video)
    print ('ALL DONE')


