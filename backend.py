from fastapi import FastAPI, Query
from pydantic import BaseModel
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"]  # Allows all headers
)

# Load the Hugging Face model and tokenizer
model_name = "facebook/blenderbot-400M-distill"  # Change to the desired model
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Define a Pydantic model for the chat request
class ChatRequest(BaseModel):
    user_input: str

# Define a root endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"message": "Server is running"}

# Define a POST endpoint for the chat functionality
@app.post("/chat")
def chat_post(request: ChatRequest):
    print(f"Received POST request: {request.user_input}")
    # Tokenize input and generate response
    inputs = tokenizer(request.user_input, return_tensors="pt")
    print(f"Tokenized input: {inputs}")
    outputs = model.generate(
        **inputs,
        max_length=100,
        temperature=0.7,  # Adjust temperature for more randomness
        top_p=0.9,        # Use nucleus sampling
        do_sample=True    # Enable sampling
    )
    print(f"Model output: {outputs}")
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated response: {response}")
    return {"response": response}

# Define a GET endpoint for the chat functionality
@app.get("/chat")
def chat_get(user_input: str = Query(..., description="User input for the chatbot")):
    print(f"Received GET request: {user_input}")
    # Tokenize input and generate response
    inputs = tokenizer(user_input, return_tensors="pt")
    print(f"Tokenized input: {inputs}")
    outputs = model.generate(
        **inputs,
        max_length=100,
        temperature=0.7,  # Adjust temperature for more randomness
        top_p=0.9,        # Use nucleus sampling
        do_sample=True    # Enable sampling
    )
    print(f"Model output: {outputs}")
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated response: {response}")
    return {"response": response}
