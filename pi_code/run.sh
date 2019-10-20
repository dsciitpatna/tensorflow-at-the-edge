# record video using pi_camera
python3 video_pi.py

# convert video from .h264 to .mp4 for processing
ffmpeg -framerate 24 -i video.h264 -c copy video.mp4

# send the video to gcp virtual machine
gcloud compute scp ./video.mp4 instance-1:~/program/program/input

# finally remove the video
rm video.mp4
