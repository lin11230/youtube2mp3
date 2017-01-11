#!/usr/bin/env python2
import os
import glob
import pipes
fo = open('./download.list', 'r')

# download
for line in fo:
    if line:
        print line
        os.system("youtube-dl -i -o '%(title)s.%(ext)s' " + line)

# convert
for f in glob.glob("./*"):
    if not (f.endswith(".mp3") or f.endswith(".py") or f.endswith(".list")):
        print f
        # command = "ffmpeg -y -i " + pipes.quote(f)  + " -b:a 128k " + pipes.quote(os.path.splitext(f)[0] + "_.mp3")
        # command = "ffmpeg -y -i " + pipes.quote(f)  + " -b:a 256k " + pipes.quote(os.path.splitext(f)[0] + "_.mp3")
        command = "ffmpeg -y -i " + pipes.quote(f)  + " -b:a 320k " + pipes.quote(os.path.splitext(f)[0] + "_.mp3")
        print command
        os.system(command)

# copy again for fixing duration
for n in glob.glob("./*_.mp3"):
    print n
    command = "ffmpeg -i " + pipes.quote(n) + " -c:a copy " + pipes.quote((os.path.splitext(n)[0])[:len(os.path.splitext(n)[0])-1] + ".mp3")
    print command
    os.system(command)


os.system("rm *_.mp3")
os.system("rm *.mp4")
os.system("rm *.mkv")
os.system("rm *.webm")

