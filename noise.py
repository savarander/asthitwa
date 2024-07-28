import noisereduce as nr
import librosa
import soundfile as sf

def load_audio(file_path):
    try:
        audio_data, sample_rate = librosa.load(file_path, sr=None)
        return audio_data, sample_rate
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None, None

def save_audio(file_path, audio_data, sample_rate):
    try:
        sf.write(file_path, audio_data, sample_rate)
        print(f"Cleaned audio saved to {file_path}")
    except Exception as e:
        print(f"Error saving audio file: {e}")

def reduce_noise(input_audio_path, output_audio_path):
    audio_data, sample_rate = load_audio(input_audio_path)
    if audio_data is None:
        return
    
    # Perform noise reduction
    reduced_noise_audio = nr.reduce_noise(y=audio_data, sr=sample_rate)
    
    # Save the cleaned audio
    save_audio(output_audio_path, reduced_noise_audio, sample_rate)

if __name__ == "__main__":
    input_audio_path = "output/audio1.wav"  # Replace with your audio file path
    output_audio_path = "Astithwa/output1/oo1.wav"  # Replace with your desired output file path
    reduce_noise(input_audio_path, output_audio_path)
