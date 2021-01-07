import setuptools
import os

cfg_txt = """
[file]
output_dir = /
last_file = /
last_dir = /

[sys]
help_info = 1

[plot]
show_title = 1
show_axis = 1
channel = Current
cmap = viridis

[save]
fig_dpi = 100

[about]
help = 
This tool aims to inspect and save figures fast. Load a folder, and use up/down to switch the files swiftly. Press key S to save the .png file into the configured folder(in config.ini) directly. 
Suppress this help_info in options.
info = Ver 0.2 by Cocca on 2021.1.7
"""

root_path = os.path.join(os.getcwd(), '.sxm_viewer')
if not os.path.exists(root_path):
    os.mkdir(root_path)

with open(os.path.join(root_path, "config.ini"), 'w') as f:
                f.write(cfg_txt)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sxm-viewer",
    version="0.1",
    author="Cocca Guo",
    author_email="guojiadong@bnu.edu.cn",
    description="a PyQt5 based tool for inspecting *.sxm files and save them as figures swiftly.",
    url="https://github.com/CoccaGuo/sxm-viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
     package_data={
        '': ['icon.png']
     },
    entry_points={
            "console_scripts": [
                "sxmv=sxm_viewer.main:main"
            ],
        },
    install_requires=[
    'pySPM',
    'PyQt5',
    'matplotlib'
    ],
    python_requires='>=3',
)