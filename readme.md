#mini-rag

```This is a minimal implementation of the RAG model for question answering.```

##Installation

###Install the required packages

$ pip install -r requirements.txt

###Setup the environment variables

```$ cp .env.example .env
Set your environment variables in the .env file. Like OPENAI_API_KEY value.```

###Run the FastAPI server
```$ uvicorn main:app --reload --host 0.0.0.0 --port 5000```