# 🗣️ Ollama IT Interviewer with Audio Capabilities

This project demonstrates how to create an IT interviewer using Ollama and Python, integrating audio capabilities.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Cloud Account
- Ollama Account or Ollama in localhost

### 📂 Project Structure

```
ollama-it-interviewer/
│
├── audio_samples/
│   ├── candidate-response.mp3
│
├── src/
│   ├── interviewer.py
│   ├── ollama_api.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/josmel/ollama-it-interviewer.git
   cd ollama-it-interviewer
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Cloud**:

   - Enable **Speech-to-Text** and **Text-to-Speech** APIs.
   - Create a service account and download the JSON credentials file.
   - Set the environment variable for credentials.

5. **Edit `src/config.py`** for your credentials and Ollama model.

6. **Add sample audio files** in `audio_samples/`.

### Running the Project

To run the interviewer, use:

```bash
python src/interviewer.py
```
