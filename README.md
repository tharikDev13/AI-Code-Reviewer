AI Code Reviewer

Requirements:
- Python 3.14+
- Ollama
- Git

Install:

pip install -r requirements.txt

Run:

python -m uvicorn main:app --reload

Required:
- GitHub App ID
- Installation ID
- Private Key (.pem)
- Webhook Secret
- Ollama model (qwen3:8b)