import asyncio
import websockets
import json

async def mock_server(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        response = process_prompt(data["prompt"])
        await websocket.send(json.dumps(response))

def process_prompt(prompt):
    # Basic AI question analysis and scoring
    score = {"correctness": 85, "clarity": 90, "creativity": 75}
    feedback = "Good attempt! Improve creativity."
    return {"score": score, "feedback": feedback}

async def main():
    # Start the WebSocket server
    server = await websockets.serve(mock_server, "localhost", 8765)
    print("Server is running on ws://localhost:8765")
    await server.wait_closed()

# Use asyncio.run to start the server
if __name__ == "__main__":
    asyncio.run(main())
