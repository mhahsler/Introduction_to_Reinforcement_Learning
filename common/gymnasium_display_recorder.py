import gymnasium as gym

from gymnasium.wrappers import RecordVideo
import glob
import io
import base64
from IPython.display import HTML
from IPython import display as ipythondisplay
from pyvirtualdisplay import Display

import os
os.environ['PYVIRTUALDISPLAY_DISPLAYFD'] = '0'

# Start virtual display
display = Display(visible=0, size=(640, 480))
display.start()

def VideoWrapper(env, run_name, render_fps=30):
    """"Wrap an environment with a video recorder."""
    
    env.metadata['render_fps'] = render_fps
    
    files = glob.glob(f'./videos/video_{run_name}*.mp4')
    if len(files):
        print("Videos already exist, I remove them first!")
        for f in files:
            os.remove(f)
    
    env = RecordVideo(env, 
                      video_folder='./videos', 
                      episode_trigger=lambda episode_id: True,
                      name_prefix=f'video_{run_name}')
    
    return env


def show(env, episode_id=None):
    """
    Display the last recorded episode video in a Jupyter notebook. Important note: close the environment before calling show!
    
    :param video_folder: Description
    """
    
    # make sure files are written
    env.close()
    
    if episode_id is None:
        episode_id=env.episode_id
    
    file = glob.glob(f'./videos/{env.name_prefix}-episode-{episode_id}.mp4')
    if len(file)<1:
        raise RuntimeError("No video found!")
    
    file = file[0]
    print (f"Showing: {file}")
    video = io.open(file, 'r+b').read()
    encoded = base64.b64encode(video)
    ipythondisplay.display(HTML(data='''
        <video width="640" height="480" controls>
            <source src="data:video/mp4;base64,{0}" type="video/mp4" />
        </video>
    '''.format(encoded.decode('ascii'))))