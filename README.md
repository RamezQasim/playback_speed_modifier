# playback_speed_modifier

 This program dynamically modifies the playback speed of videos to maintain a constant word/second ratio. The user
 inputs the desired ratio, and the program updates the playback speed every 3 second of the video to maintain the
 desired ratio.

Dependencies
 - wave
 - contextlib
 - speech_recognition
 - moviepy.editor

Inputs:
  - The video file name with extension .mp4
  - desired words/second ratio. 

Output:
 - Video in an HTML5 file, with the desired words/second. 
 - transcription of video in a .txt file.
