# Standalone AI Travel Planner

A standalone Python travel-planning project that uses the OpenAI API and Pydantic structured outputs to generate practical multi-day itineraries.

## Project structure

- `travel_planner.py` — main application
- `requirements.txt` — Python dependencies
- `.gitignore` — files that should not be committed

## Requirements

- Python 3.9+
- An OpenAI API key
- GitHub Codespaces, local Python, or another Python environment

## Setup in GitHub Codespaces

Install the dependencies:

```bash
python -m pip install --upgrade -r requirements.txt
```

Set your API key for the current terminal session:

```bash
export OPENAI_API_KEY="YOUR_REAL_API_KEY"
```

Verify that it is configured without displaying the key:

```bash
python -c "import os; print('API key configured:', bool(os.environ.get('OPENAI_API_KEY')))"
```

Expected result:

```text
API key configured: True
```

Run the application:

```bash
python travel_planner.py
```

The program prints the generated itinerary as formatted JSON.

## Security

Never commit an OpenAI API key to GitHub. Keep secrets in environment variables or a secure Codespaces secret.
