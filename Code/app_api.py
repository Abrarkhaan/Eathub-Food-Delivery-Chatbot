from fastapi import FastAPI
from fastapi import Request
import helper_functions
import backend_functions

# Create app object
app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract data from the payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = helper_functions.get_session_id(output_contexts[0]["name"])

    # Call the functions on webhook calls
    intent_handler = {
        'new_order': backend_functions.new_order,
        'order_add': backend_functions.add_items_to_order,
        'order_remove': backend_functions.remove_items_from_order,
        'order_complete': backend_functions.complete_order,
        'order_tracked': backend_functions.track_order
    }
    
    return intent_handler[intent](session_id, parameters)
