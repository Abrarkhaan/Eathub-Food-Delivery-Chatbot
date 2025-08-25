from fastapi.responses import JSONResponse
import helper_functions

# Initialize a dictionary
orders_inprogress = {}

# Function to restart the order if called in the middle of an order
def new_order(session_id: str, parameters: dict):
    if session_id not in orders_inprogress:
        pass 
    else:
         orders_inprogress.pop(session_id, None)

# Function to add items to new or existing order
def add_items_to_order(session_id: str, parameters: dict):
    food_items = parameters["food-item"]
    quantities = parameters["number"]

    if len(quantities) != len(food_items):
        message = "Please provide both the food item and quantity clearly (e.g. 2 pizzas and one burger)"
    else:
        new_food = dict(zip(food_items, quantities))

        if session_id not in orders_inprogress:
            orders_inprogress[session_id] = new_food
        else:
            current_food = orders_inprogress[session_id]
            current_food.update(new_food)
            orders_inprogress[session_id] = current_food

        order_str = helper_functions.get_str_from_food_dict(orders_inprogress[session_id])
        message = f"Your order is: {order_str}. Is it final or Do you want to add more?"

    return JSONResponse(content={
        "fulfillmentText": message
    })

# Function to remove items from current order
def remove_items_from_order(session_id: str, parameters: dict):
    if session_id not in orders_inprogress:
        return JSONResponse(content={
            "fulfillmentText": "Trouble!! Please place a new order."
        })
    
    food_items = parameters["food-item"]
    current_order = orders_inprogress[session_id]

    items_notfound = []
    removed_items = []

    for item in food_items:
        if item not in current_order:
            items_notfound.append(item)
        else:
            removed_items.append(item)
            del current_order[item]
    
    if len(removed_items) > 0:
        message = f'Removed {helper_functions.get_str_from_food_list(removed_items)} from your order!'
    if len(items_notfound) > 0:
        message = f' Your order does not have {helper_functions.get_str_from_food_list(items_notfound)}'
        
    if len(current_order.keys()) == 0:
        message += " Your order is empty!. Please add some items"
    else:
        order_str = helper_functions.get_str_from_food_dict(current_order)
        message += f" Here is what is left in your order: {order_str}"

    return JSONResponse(content={
        "fulfillmentText": message
    })

# Function to complete the orders in progress
def complete_order(session_id: str, parameters: dict):
    if session_id not in orders_inprogress:
        message = "Trouble!! Please place a new order."
    else:
        order = orders_inprogress[session_id]
        order_id = helper_functions.insert_to_database(order)
        if order_id == -1:
            message = "Error accured!! Please place a new order."
        else:
            order_total = helper_functions.get_order_price(order_id)

            message = f"Order placed successfully. Order ID: {order_id}.\n" \
                           f"Your order total is {order_total}." \
                           f"Please pay at the time of delivery!"

        del orders_inprogress[session_id]

    return JSONResponse(content={
        "fulfillmentText": message
    })

# Function to track any order with orderID
def track_order(session_id: str, parameters: dict):
    order_id = int(parameters['order_id'])
    status = helper_functions.get_order_status(order_id)
    if status:
        message = f"The order status for order id: {order_id} is: {status}"
    else:
        message = f"No order found!"

    return JSONResponse(content={
        "fulfillmentText": message
    })
