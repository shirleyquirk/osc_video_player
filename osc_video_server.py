#python osc listener
#on osc message in
#play randomly selected video files from some folder
import os
import random
from pythonosc import dispatcher,osc_server
import subprocess
osc_port = 5005
videopath = "./videos"

def play_random(unused_addr,args):
    print("Received message addr: ",unused_addr,", args:",args) 
    if (len(play_random.videolist) == 0):
        play_random.videolist = os.listdir(videopath)
        random.shuffle(play_random.videolist)
    random_vid1 = play_random.videolist.pop()
    if (len(play_random.videolist) == 0):
        play_random.videolist = os.listdir(videopath)
        random.shuffle(play_random.videolist)
    random_vid2 = play_random.videolist.pop()

    print("Playing file: ",random_vid1," on screen 1")
    print("Playing file: ",random_vid2," on screen 2")
    subprocess.run(["killall","omxplayer"])
    subprocess.run(["omxplayer",videopath+'/'+random_vid1])
    subprocess.run(["omxplayer",videopath+'/'+random_vid2,"--display","7"])
play_random.videolist = os.listdir(videopath)
random.shuffle(play_random.videolist)

print("Initialized video list with:",play_random.videolist)
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/playrandom",play_random)

server = osc_server.ThreadingOSCUDPServer(("0.0.0.0",osc_port),dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()
