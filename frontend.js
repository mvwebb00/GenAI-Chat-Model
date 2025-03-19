import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    // State to store user input
    const [userInput, setUserInput] = useState('');
    // State to store AI response
    const [response, setResponse] = useState('');

    // Function to handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent default form submission behavior
        console.log("Sending request to /chat endpoint with user input:", userInput);
        try {
            // Send GET request to the /chat endpoint with user input as query parameter
            const result = await axios.get('http://127.0.0.1:8000/chat', {
                params: { user_input: userInput }
            });
            console.log("Received response from /chat endpoint:", result.data);
            // Update response state with the AI response
            setResponse(result.data.response);
        } catch (error) {
            console.error("Error sending request:", error);
            // Update response state with error message
            setResponse("Error: Unable to get response from server.");
        }
    };

    return (
        <div>
            <h1>AI Chatbot</h1>
            {/* Form to capture user input and submit */}
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    placeholder="Ask me anything..."
                />
                <button type="submit">Send</button>
            </form>
            {/* Display AI response */}
            <p><strong>AI Response:</strong> {response}</p>
        </div>
    );
};

export default App;
