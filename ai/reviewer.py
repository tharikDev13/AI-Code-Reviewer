import sys
import json
from click import prompt
import requests

def review_code(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"

    print("\n===== PROMPT LENGTH =====")
    print(len(prompt))
    print("=========================\n")
    
    payload = {
        "model": "qwen2.5-coder:7b",
        "prompt": prompt,
        "stream": True,  # Enables streaming behavior from Ollama
        "options": {
            "temperature": 0.0,
            "repeat_penalty": 1.0,
            "num_ctx": 32768,    # 32k window safely handles multi-file, larger pull requests
            "num_predict": 1024   # Plenty of headroom to print deep structural code finding logs
        }
    }

    print("\n===== AI REVIEW (STREAMING LIVE) =====")
    
    review_buffer = []
    
    try:
        # stream=True keeps the network socket open for chunk processing
        response = requests.post(url, json=payload, stream=True, timeout=300)
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                # Parse individual JSON token events from Ollama line-by-line
                chunk = json.loads(line.decode('utf-8'))
                token = chunk.get("response", "")
                
                # Append to our local aggregator buffer
                review_buffer.append(token)
                
                # Instantly write the token out to the console terminal
                sys.stdout.write(token)
                sys.stdout.flush()

    except Exception as e:
        print(f"\nStreaming inference engine failure: {e}")
        return "Error occurred during AI local code review."

    print("\n======================================")

    # Reassemble individual tokens into one complete string response body
    full_review = "".join(review_buffer).strip()
    return full_review if full_review else "No review generated."
