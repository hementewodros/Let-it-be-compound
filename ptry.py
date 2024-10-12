import asyncio
import websockets
import google.generativeai as genai

genai.configure(api_key="AIzaSyAt4dwOTU23gq-xO4KXwD8uMdcgXmygAo0")
async def handle_websocket(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        
        Final="Write all the compunds possible by synthenizing only and all the following elements"+message+"and a line about the propertis of each compund"
        # Create chat completions
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction="You are the robot that returns an HTML code( you can only bold, italic, create a space no more no less) imaging your response is embeded in a div, lists all possible compounds using all the given elements and talks about their chemical structure, toxicity, ...",
        )
        chat_session = model.start_chat(
        history=[
            {
            "role": "user",
            "parts": [
                "From now on you will get my data and will give me the possible compounds and their toxicity level and more imagining your response is embeded in an HTML div\n",
            ],
            },
            {
            "role": "model",
            "parts": [
                "Yes, Sir. From now on I'll do what you say, Sir."            ],
            }
            
            
        ]
        )
        answer = chat_session.send_message(message)
        print(answer.text)
        print("Given message:", message)
        print("Processed message from Gen:", answer.text)

        # Send the processed message back to the WebSocket client
        await websocket.send(answer.text)

async def main():

    async with websockets.serve(handle_websocket, "localhost", 8766):
        await asyncio.Future()  # Keep the server running indefinitely

asyncio.run(main())