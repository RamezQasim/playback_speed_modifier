"""
Main
 This program dynamically modifies the playback speed of videos to maintain a constant word/second ratio. The user
 inputs the desired ratio, and the program updates the playback speed every 3 second of the video to maintain the
 desired ratio.

Inputs:
  - The video file name with extension .mp4
  - desired words/second ratio. \n

Output:
 - Video in an HTML5 file, with the desired words/second. \n
 - transcription of video in a .txt file.
"""
from transcriber import *
vf = []  # speed factor: controls the playback speed
t = []  # a list of corresponding timestamps for the speed factor
wps = int(input('input your desired words/second\n'))
video_file_name = input('Input your video file name.mp4')
time_segment = 3  # update playback speed every [time_segment] seconds || this needs to be optimised.

transcriber(video_file_name, time_segment)  # transcribe and outputs the transcription in a .txt file
fhand = open('transcription.txt')
n = 0
for line in fhand:
    line = line.rstrip().split()
    if line[0] == '***':  # if nothing was said, set the speed to 1 (normal)
        vf.append(1.0)
    else:
        vf.append(wps*time_segment/len(line))
    t.append(n * time_segment)
    n += 1

f = open('mod_video.html', 'w')

content ="""<!DOCTYPE html>
<html>
<body>


<video id="myVideo" width="500" height="400" controls>
    <source src= %s type="video/mp4">
error
</video>


<script>

var vid = document.getElementById("myVideo");

function getPlaySpeed() {
  alert(vid.playbackRate);
}

function getTime() {
  alert(vid.currentTime);
}

var Stamps =%s ;
var Speed  = %s;
var i = 0;

var test = 0;
var interval;

function check_test() {
console.log( vid.currentTime );
    if(vid.currentTime >= Stamps[i] && vid.currentTime < Stamps[i+1]){
		vid.playbackRate = Speed[i];
        console.log( "Time now: " + Stamps[i] + "Speed: " + Speed[i]);
		i = i + 1;
    }
}

interval = window.setInterval( check_test, 1 );

</script>

</body>
</html>
""" % (video_file_name, t, vf)

f.write(content)
f.close()
