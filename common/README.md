# Install the Course Environment

The code examples require an installation of Python 3.10 or later and packages like
numpy, pandas, Gymnasium, `gym-classics2`. See the repository's [`environment.yml`](./environment.yml)
for a complete list.

Deep reinforcement learning examples requires PyTorch, Stable-Baselines3.

The setup depends on your IDE.

## Google Colab

Colab runtimes are temporary. Colab has many packages already preinstalled. You need to install the additional course-specific dependencies once at
the beginning of each new session by running a notebook cell with:

```python
%pip install "gymnasium[box2d,classic-control,other]>=1.0,<2"
%pip install pyvirtualdisplay
%pip install gym-classics2
```

To install the latest development version `gym-classics2` of run:
```python
%pip install -q "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

Restart the Colab runtime if prompted after installation. 

You can test this using the 
following [example notebook](https://colab.research.google.com/github/mhahsler/Introduction_to_Reinforcement_Learning/blob/master/MC/frozen_lake_MC.ipynb)


## Local Installation with Conda

This is the suggested method for Windows.
The repository's [`environment.yml`](./environment.yml) installs the packages
with Conda used throughout the course.

1. Install a Conda distribution such as
  [Miniconda](https://www.anaconda.com/docs/getting-started/installation).
2. Download the repository's [`environment.yml`](./environment.yml) file.
3. Create and activate the environment from a terminal (e.g., a terminal in VS Code) in the 
   directory you downloaded  `environment.yml` to.

  ```bash
  conda env create --file environment.yml
  conda activate reinforcement-learning
  ```

In VS Code, create or open a Notebook and use **Python: Select Interpreter** or
**Notebook: Select Notebook Kernel** to choose the `reinforcement-learning` environment.


## Installation Without Conda

Conda is preferred because it also manages SWIG and FFmpeg. If Conda is not
available, use Python 3.12 and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel numpy pandas scipy matplotlib tqdm
python -m pip install "gymnasium[box2d,classic-control,other]>=1.0,<2" pyvirtualdisplay
python -m pip install gym-classics2
python -m pip install "stable-baselines3[extra]>=2.4,<3"
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1`. A non-Conda installation 
may require system installations of SWIG, FFmpeg, and (on Linux/WSL) Xvfb 
(see below).


## Video Capture on Linux and WSL

The Conda environment supplies FFmpeg and the Python visualization packages.
Headless recording with `pyvirtualdisplay` also requires the X virtual
framebuffer on Linux or WSL:

```bash
sudo apt-get update
sudo apt-get install xvfb
```

This operating-system packages are not needed to run non-rendering
examples.


## Updating gym-classics2 for Hotfixes

Conda can update packages:
```bash
conda activate reinforcement-learning
conda update --all
```

Pip can do this as well.

Some fixes for `gym-classics2` may not be already included in the PyPI release version. You can
install the development version from the terminal: 

```bash
python -m pip install "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

Or run the following code in a notebook cell:

```Python
%pip install "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

## Troubleshooting

- If a notebook reports a missing package after installation, confirm that its
  selected kernel is `reinforcement-learning`.
- If video capture reports that no display is available on Linux or WSL,
  install Xvfb as shown above and restart the kernel.
- Keep dependency names containing extras in quotes, for example
  `"gymnasium[box2d]"`, so shells do not interpret the brackets.

## License

&copy; 2026 [Michael Hahsler](https://michael.hahsler.net).
All code and documents in this repository are provided under the
[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License](https://creativecommons.org/licenses/by-sa/4.0/).

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)
