<!-- #region -->
# Setup the Needed Software

## Setup Gymnasium

The documentation for Gymnasium is available at https://gymnasium.farama.org/ 

Gymnasium is already preinstalled in Google Colab!

Here are the steps for VS Code:
1. Create a new folder and open it with VS Code and install all needed Python Extensions in VS Code.
2. Create a new virtual environment (CTRL-Shift P Python Create Environment...)
3. I needed to install swig and the Python C++ headers on WSL2 via the terminal
    * `sudo apt install swig`
    * `sudo apt-get install python3-dev` 
4. Install python libraries for gymnasium with the needed extras

In your virtual environment execute:
```bash
python -m pip install gymnasium[box2d,classic_control]
```

You can also add a Python code block using the magic `%`
```python
%pip install swig
%pip install gymnasium[box2d,classic_control]
```

## Setup Capturing Gymnasium Environment Visualizations in Notebooks

Additional installs for screen capturing so environment visualizations can be converted to embedded videos.
This also works on Google Colab so you can see the visualization.

For recording videos, I had to install on WSL2:    
* `sudo apt-get install xvfb ffmpeg`

In your virtual environment execute:
```bash
python -m pip install pyvirtualdisplay
python -m pip install gymnasium[other]
```

## Setup `gym_classics2`

The package is available on Github at https://github.com/mhahsler/gym-classics2

To install it, execute in your virtual environment:
```bash
python -m pip install "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

Colab users: To use `gym_classics2` with Colab, you need to add a code block with the following contents to
the notebook:

```python
%pip install "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

Run the block once, then restart the session (see pulldown next to Run). 
`gym_classics2` is now installed for this session and you can comment out the pip install line.

More detailed instructions can be found in the [package documentation](https://mhahsler.github.io/gym-classics2/)

## License
&copy; 2025 [Michael Hahsler](http://michael.hahsler.net). 
All code and documents in this repository are provided under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License.](https://creativecommons.org/licenses/by-sa/4.0/)

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)
<!-- #endregion -->
