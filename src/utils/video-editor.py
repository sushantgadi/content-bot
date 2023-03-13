import moviepy.editor as mp
import os
import random
import json


VIDEO_DURATION_IN_SECONDS = 90
VIDEO_TEXT_WIDTH = 600
VIDEO_FONT_FAMILY = "Helvetica Bold"
VIDEO_FONT_COLOR = "yellow"
VIDEO_FONT_BACKGROUND = "red"
VIDEO_FONT_SIZE = 30
VIDEO_FONT_OPACITY = 0.7
VIDEO_TEXT_POSITION = 'center', 'center'
VIDEO_FPS = 65
VIDEO_WRITE_THREADS = 4
AUDIO_FPS = 44100


def generate_video_with_text(topic_name, audio_file, video_file, output_folder, heading, thanks_message, text):

    audio = mp.AudioFileClip(audio_file)
    audio_new_duration = audio.set_duration(VIDEO_DURATION_IN_SECONDS)

    video = mp.VideoFileClip(video_file)
    duration = video.duration

    video_loops = int(VIDEO_DURATION_IN_SECONDS / duration) + 1

    video_looped = video.crossfadein(0.2).loop(n=video_loops)

    video_new_duration = video_looped.set_duration(VIDEO_DURATION_IN_SECONDS)

    output_video = video_new_duration.set_audio(audio_new_duration)

    texts = []
    text_clips = []

    texts = text.split("#")

    text_duration = int((VIDEO_DURATION_IN_SECONDS - 8) / len(texts))

    print("text_duration= ", text_duration)

    heading_text_clip = mp.TextClip(heading, fontsize=VIDEO_FONT_SIZE, font=VIDEO_FONT_FAMILY,
                                    color=VIDEO_FONT_COLOR, bg_color=VIDEO_FONT_BACKGROUND).set_duration(4)
    text_clips.append(heading_text_clip)

    for text in texts:
        text_clip = mp.TextClip(text, fontsize=VIDEO_FONT_SIZE, font=VIDEO_FONT_FAMILY,
                                color=VIDEO_FONT_COLOR, bg_color=VIDEO_FONT_BACKGROUND).set_duration(text_duration)
        text_clips.append(text_clip)

    thanks_text_clip = mp.TextClip(thanks_message, fontsize=VIDEO_FONT_SIZE, font=VIDEO_FONT_FAMILY,
                                   color=VIDEO_FONT_COLOR, bg_color=VIDEO_FONT_BACKGROUND).set_duration(4)
    text_clips.append(thanks_text_clip)

    video_with_text = mp.CompositeVideoClip([output_video, mp.concatenate_videoclips(
        text_clips, method="compose").set_opacity(VIDEO_FONT_OPACITY).set_position(VIDEO_TEXT_POSITION)])

    video_with_text.write_videofile(output_folder + "/"+topic_name+".mp4", codec='libx264',
                                    audio_codec='aac',
                                    remove_temp=True,
                                    audio_fps=AUDIO_FPS,
                                    threads=VIDEO_WRITE_THREADS, fps=VIDEO_FPS)


def select_audio_video(audio_folder, video_folder):
    audio_files = os.listdir(audio_folder)
    video_files = os.listdir(video_folder)
    audio_file = random.choice(audio_files)
    video_file = random.choice(video_files)
    selected_audio_file = audio_folder+"/"+audio_file
    selected_video_file = video_folder+"/"+video_file
    print("selected_audio_file= ", selected_audio_file)
    print("selected_video_file= ", selected_video_file)
    return selected_audio_file, selected_video_file


def initiate_content_generation():
    f = open(
        '/Users/sgadi3/Documents/git_repo/poc/content-bot/assets/text/data.json', "r")
    json_data = json.loads(f.read())

    output_folder = "/Users/sgadi3/Documents/git_repo/poc/content-bot/output/motivation"

    for data in json_data:
        selected_audio_file, selected_video_file = select_audio_video(
            "/Users/sgadi3/Documents/git_repo/poc/content-bot/assets/motivation/audios", "/Users/sgadi3/Documents/git_repo/poc/content-bot/assets/motivation/videos")
        generate_video_with_text(data['topic_name'], selected_audio_file,
                                 selected_video_file, output_folder, data['heading'], data['thanks_message'], data['text'])
    f.close()

initiate_content_generation()