# AVrecordeR
Audio and video recording using Python and ffmpeg

branched from https://github.com/JRodrigoF/AVrecordeR

You can use it like this:
    
    import time
    from AVrecordeR import start_AVrecording, stop_AVrecording, file_manager
    start_AVrecording("MyAVRecording")
    time.sleep(5)
    stop_AVrecording("MyAVRecording")
    file_manager("MyAVRecording")

which will create a AV-Recording named "MyAVRecording.avi" in the same directory as your script is in.

for your convenience a setup file is provided.

GNU General Public License v2.0
