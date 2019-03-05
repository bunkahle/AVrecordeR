#!/usr/bin/env python
from distutils.core import setup

setup(
    name='AVrecordeR',
    version='1.0',
    author='Andreas Bunkahle',
    author_email='abunkahle@t-online.de',
    description='AudioVideoRecorder generates AV-Recordings along with ffmpeg',
    license='GPL 2.0',
    py_modules=['AVrecordeR'],
    python_requires='>=2.7',
    url='https://github.com/bunkahle/AVrecordeR',
    long_description=open('README.md').read(),
    platforms = ['any'],
    install_requires=['pyaudio', 'numpy', 'opencv-python']
)
