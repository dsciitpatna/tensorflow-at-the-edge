from picamera import PiCamera
from time import sleep

camera = PiCamera()
PATH = '/home/pi/innovation/video.h264'

camera.start_preview()
camera.start_recording(PATH)
sleep(30)
camera.stop_recording()
camera.stop_preview()


## if video has to be sent via ssh

# import paramiko
# from scp import SCPClient

# def createSSHClient(server, user, password):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(server, username=user, password=password)
#     return client

# ssh = createSSHClient(IP , USERNAME, PASSWORD)
# ssh = createSSHClient(IP , USERNAME, PASSWORD)
# std_in, std_out, std_err = ssh.exec_command('c')
# ssh.exec_command('touch a.txt')
#std_out.channel.recv_exit_status()
# scp = SCPClient(ssh.get_transport())
# scp.put('video.h264')
# ssh.exec_command('mv test.py ./innovation/')

