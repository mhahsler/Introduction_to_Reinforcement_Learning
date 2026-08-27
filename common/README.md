# Install the Course Environment

The repository's [`environment.yml`](../environment.yml) installs the packages
used throughout the course, including JupyterLab, Gymnasium, `gym-classics2`,
PyTorch, Stable-Baselines3, and the visualization dependencies. This Conda-based
setup is the recommended local installation method.

## Google Colab

Colab runtimes are temporary. Install the course-specific dependencies once at
the beginning of each new runtime, before importing them:

```python
!apt-get -qq update
!apt-get -qq install -y swig xvfb ffmpeg
%pip install -q "gymnasium[box2d,classic-control,other]>=1.0,<2" pyvirtualdisplay
%pip install -q "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
```

Restart the Colab runtime if prompted after installation. Package installations
inside individual notebooks are otherwise unnecessary when using the local
Conda environment.

More information about the custom teaching environments is available in the
[`gym-classics2` documentation](https://mhahsler.github.io/gym-classics2/).


## Local Installation with Conda

Install the Conda distribution such as
[Miniconda](https://www.anaconda.com/docs/getting-started/installation). Then clone the
repository, or open a terminal in an existing clone:

```bash
git clone https://github.com/mhahsler/Introduction_to_Reinforcement_Learning.git
cd Introduction_to_Reinforcement_Learning
```

Create and activate the environment from the repository root:

```bash
conda env create --file environment.yml
conda activate reinforcement-learning
```

In VS Code, open the repository and use **Python: Select Interpreter** or
**Notebook: Select Notebook Kernel** to choose `reinforcement-learning`.

## Video Capture on Linux and WSL

The Conda environment supplies FFmpeg and the Python visualization packages.
Headless recording with `pyvirtualdisplay` also requires the X virtual
framebuffer on Linux or WSL:

```bash
sudo apt-get update
sudo apt-get install xvfb
```

This operating-system package is not needed merely to run non-rendering
examples. Native desktop windows also do not use `pyvirtualdisplay`.

## Installation Without Conda

Conda is preferred because it also manages SWIG and FFmpeg. If Conda is not
available, use Python 3.12 and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel numpy pandas scipy matplotlib tqdm
python -m pip install "gymnasium[box2d,classic-control,other]>=1.0,<2" pyvirtualdisplay
python -m pip install "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git"
python -m pip install "stable-baselines3[extra]>=2.4,<3"
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1`. A non-Conda installation also requires Git and
may require system installations of SWIG, FFmpeg, and (on Linux/WSL) Xvfb.

## Updating gym-classics2 for Hotfixes
i
Sometimes I will fix things in the package. If I pump the version and conda will update the environment. Sometime it may
be a fix without a version jump. To catch both do:

```bash
conda activate reinforcement-learning
conda env update --file environment.yml --prune

python -m pip install \
  --upgrade \
  --force-reinstall \
  --no-deps \
  "gym-classics2 @ git+https://github.com/mhahsler/gym-classics2.git@main"

python -m pip check
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
