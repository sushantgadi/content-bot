import moviepy.editor as mp

VIDEO_DURATION_IN_SECONDS = 15



def generate_video_with_text(audio_file, video_file, output_folder, text, heading):

    audio = mp.AudioFileClip(audio_file)
    audio_new_duration = audio.set_duration(VIDEO_DURATION_IN_SECONDS)


    video = mp.VideoFileClip(video_file)
    duration = video.duration

    video_loops = int(VIDEO_DURATION_IN_SECONDS / duration) + 1

    video_looped = video.crossfadein(0.2).loop(n=video_loops)

    video_new_duration = video_looped.set_duration(VIDEO_DURATION_IN_SECONDS)

    output_video = video_new_duration.set_audio(audio_new_duration)

    texts = []
    texts = text.split("#")
    texts.append(heading)

    text_duration = int(VIDEO_DURATION_IN_SECONDS / len(texts))

    text_position = output_video.size[0]/2, output_video.size[1]/2

    text_clips = []

    for text in texts:
         text_clip = mp.TextClip(text, fontsize=15, color='black', bg_color='white', align='center').set_position(text_position)
         text_clip.set_duration(text_duration)
         text_clips.append(text_clip)


    final_text_clips = mp.concatenate_videoclips(text_clips)

    video_with_text = mp.CompositeVideoClip([output_video, final_text_clips])

    video_with_text.write_videofile(output_folder + "/output_video.mp4", codec='libx264',
                             audio_codec='aac',
                             remove_temp=True)

generate_video_with_text("/Users/sgadi3/Documents/git_repo/poc/content-bot/assets/motivation/audios/epicaly-113907.mp3", "/Users/sgadi3/Documents/git_repo/poc/content-bot/assets/motivation/videos/Pexels Videos 1580455.mp4", "/Users/sgadi3/Documents/git_repo/poc/content-bot/output/motivation",
                         "1. Be true to yourself: Live your life in accordance with your own values, beliefs, and priorities.# 2. Pursue your passions: Find something you're passionate about and make it a central part of your life.# 3. Take care of your health: Eat well, exercise regularly, get enough sleep, and take care of your mental health.# 4. Cultivate positive relationships: Surround yourself with people who support and inspire you, and who share your values.# 5. Learn from your mistakes: Accept that you will make mistakes, but use them as an opportunity to learn and grow.# 6. Practice gratitude: Take time to appreciate the good things in your life, and express gratitude to others.# 7. Be open to new experiences: Try new things and step outside of your comfort zone to broaden your horizons and discover new passions.# 8. Work hard and persevere: Achieving your goals often requires hard work and determination, so don't give up easily.# 9. Be kind and compassionate: Treat others with respect, kindness, and empathy.# 10. Make a positive impact: Look for ways to contribute to your community and make a positive difference in the world.", "Here are some general life rules that can help guide you towards a fulfilling and successful life:")
