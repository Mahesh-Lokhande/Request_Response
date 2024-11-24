import asyncio
import websockets
import json

# Read prompts from a file
def load_prompts(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

async def send_messages():
    uri = "ws://localhost:8765"
    prompts = load_prompts("prompts.txt")  # Load prompts from a file
    async with websockets.connect(uri) as websocket:
        for prompt in prompts:
            message = {"prompt": prompt}
            print(f"Sending prompt: {prompt}")
            await websocket.send(json.dumps(message))
            response = await websocket.recv()
            print(f"Response: {json.loads(response)}\n")

if __name__ == "__main__":
    asyncio.run(send_messages())

