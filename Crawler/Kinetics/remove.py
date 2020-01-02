import os
import shutil
import glob
from tqdm import tqdm


if __name__ == '__main__':
    root = '/root/ActivityNet/Crawler/Kinetics/data/*/*.mp4'
    videos = glob.glob(root)
    
    for video in tqdm(videos):
        txt = video.replace('.mp4','.txt')
        f = open(txt,'w')
        f.close()
        if os.path.exists(txt):
            os.remove(video)
            if not os.path.exists(video):
                print ('delete >>'+video)
        else:
            print('not created >> ' + txt)



    print ('ALL DONE')

