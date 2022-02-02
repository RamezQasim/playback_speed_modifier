import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os


def transcriber(video_file_name='clip.mp4', time_segment=5):
    """
    transcribe mp4 videos in the local folder \n
    :param video_file_name: the name of the desired video to be transcribed, including its extension.
    :param time_segment: the interval by which the video is divided, each segment will be transcribed independently.
    :return: transcribed text in transcription.txt. each line represents the transcription of a segment, and '***'
     indicates no speech detected in that segment.
    """
    transcribed_audio_file_name = "transcribed.wav"
    audioclip = AudioFileClip(video_file_name)
    audioclip.write_audiofile(transcribed_audio_file_name)  # extract audio from video

    # get the number of chunks
    with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    total_duration = math.ceil(duration / time_segment)

    r = sr.Recognizer()  # using speech_recognition package for transcribing the audio
    f = open("transcription.txt", "w")

    # segment the audio into chunks and transcribe them sequentially
    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i*time_segment, duration=time_segment)
        f = open("transcription.txt", "a")

        try:
            f.write(r.recognize_google(audio))  # a more accurate transcriber is needed for a smoother output
            f.write("\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            f.write('***\n')  # to indicate that either nothing was said, or unintelligible sounds
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    f.close()
    os.remove(transcribed_audio_file_name)

