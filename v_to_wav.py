from moviepy.editor import AudioFileClip
import os

def convert_mp4_audio_to_wav(input_file, output_file):
    # Load the audio clip
    audio_clip = AudioFileClip(input_file)
    
    # Write the audio clip to a WAV file
    audio_clip.write_audiofile(output_file)
    
    # Close the audio clip
    audio_clip.close()

# File paths
input_file = "111/apj/WhatsApp Video 2024-07-27 at 17.03.23_b36c6a62.mp4"
output_file = "output/audio1.wav"

# Convert .mp4 to .wav
convert_mp4_audio_to_wav(input_file, output_file)

print("Conversion complete!")