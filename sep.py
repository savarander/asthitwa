import os
from pydub import AudioSegment
from pyAudioAnalysis import audioSegmentation as aS
from pyAudioAnalysis import audioBasicIO as aIO

def extract_segments(input_audio_path, segments, output_dir):
    audio = AudioSegment.from_wav(input_audio_path)
    speaker_audios = {}

    for segment in segments:
        start_time = int(segment[0] * 1000)
        end_time = int(segment[1] * 1000)
        speaker = segment[2]

        if speaker not in speaker_audios:
            speaker_audios[speaker] = AudioSegment.empty()

        speaker_audios[speaker] += audio[start_time:end_time]

    for speaker, speaker_audio in speaker_audios.items():
        speaker_audio.export(os.path.join(output_dir, f"speaker_{speaker}.wav"), format="wav")

def perform_diarization(input_audio_path, output_dir):
    # Read audio file
    [fs, x] = aIO.read_audio_file(input_audio_path)
    segments = aS.speaker_diarization(input_audio_path, 2)  # Assuming 2 speakers

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract and save segments
    extract_segments(input_audio_path, segments, output_dir)

    print(f"Extracted audio segments saved in {output_dir}")

if __name__ == "__main__":
    input_audio_path = "Astithwa/output1/oo1.wav"  # Replace with your input audio file path
    output_dir = "Astithwa/output1"  # Replace with your desired output directory

    perform_diarization(input_audio_path, output_dir)
