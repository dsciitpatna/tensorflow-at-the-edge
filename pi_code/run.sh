python3 video_pi.py
ffmpeg -framerate 24 -i video.h264 -c copy video.mp4
gcloud compute scp ./video.mp4 instance-1:~/program/program/input
rm video.mp4
