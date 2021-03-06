import os
from setuptools import find_packages, setup

setup(
    name="screenrecord",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Record screen with python.",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['record = screenrecord.srecord:main']
    },
	install_requires=["imageio", "imageio-ffmpeg"]
)
