from pydub import AudioSegment
from pydub.playback import play
from src.ollama_api import ask_question
from src.speech_to_text import recognize_speech
from src.text_to_speech import synthesize_speech
from src.real_time_audio import record_audio

from dotenv import load_dotenv

load_dotenv()

def main():
    question = "Tell me about your experience with Python."
    synthesize_speech(question, "audio_samples/question.mp3")
    
    question_audio = AudioSegment.from_mp3("audio_samples/question.mp3")
    play(question_audio)
    
    
     # Record candidate's response in real time
    record_audio("audio_samples/candidate-response.wav", record_seconds=10)
    
    # Convert recorded audio to text
    candidate_response = recognize_speech("audio_samples/candidate-response.wav")
    print(f"Candidate response Response: {candidate_response}")
    
    ollama_response = ask_question(candidate_response)
    print(f"Ollama Response: {ollama_response}")
    
    synthesize_speech(ollama_response, "audio_samples/response.mp3")
    
    response_audio = AudioSegment.from_mp3("audio_samples/response.mp3")
    play(response_audio)

if __name__ == "__main__":
    main()
