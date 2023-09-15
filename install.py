import fall

#todo: check if ffmpeg-python is used anywhere, could have sworn i removed it but not 100% enough to change now.
if not fall.is_installed("ffmpeg-python"):
    fall.run_pip("install ffmpeg-python", "requirements for TemporalKit extension")

if not fall.is_installed("moviepy"):
    fall.run_pip("install moviepy", "requirements for TemporalKit extension")
    
if not fall.is_installed("imageio_ffmpeg"):
    fall.run_pip("install imageio_ffmpeg", "requirements for TemporalKit extension")

if not fall.is_installed("scenedetect"):
    fall.run_pip("install scenedetect", "requirements for TemporalKit extension")
