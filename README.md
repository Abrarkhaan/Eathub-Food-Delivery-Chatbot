# Eathub Food Delivery Chatbot

Eathub Food Delivery Chatbot is an intelligent chatbot built with
**Dialogflow**, **Python (FastAPI)**, and a simple **frontend** to
handle food delivery orders. It allows users to interact naturally while
placing and managing their orders.

------------------------------------------------------------------------

## 🚀 Features

-   Greet users with a **Welcome message**
-   Display **working hours**
-   Show **menu for ordering**
-   Create a **new order**
-   **Add items** to an order
-   **Remove items** from an order
-   **Complete an order**
-   **Track order** status

------------------------------------------------------------------------

## 📂 Project Structure

    Eathub_Food_Delivery_Chatbot/
    │── requirements.txt
    │
    ├── Code/
    │   ├── app_ai.py                # Main FastAPI application with Dialogflow webhook integration
    │   ├── backend_functions.py     # Functions for handling intents (new_order, add/remove items, complete order, etc.)
    │   ├── helper_functions.py      # Utility functions (dict/list to string, database operations, etc.)
    │
    ├── DB/
    │   └── eathub_db.sql            # SQL script for database setup
    │
    ├── UI/
    │   └── site.html                # Frontend chatbot interface

------------------------------------------------------------------------

## ⚙️ Installation & Setup

1.  Clone the repository:

    ``` bash
    git clone https://github.com/Abrarkhaan/Eathub_Food_Delivery_Chatbot.git
    cd Eathub_Food_Delivery_Chatbot
    ```

2.  Create and activate a virtual environment:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate    # On Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Setup the database:

    -   Import `DB/eathub_db.sql` into your SQL database.

5.  Run the FastAPI app:

    ``` bash
    uvicorn Code.app_ai:app --reload
    ```

6.  Open the chatbot frontend:

    -   Open `UI/site.html` in your browser.

------------------------------------------------------------------------

## 💡 Intents

This chatbot is powered by **Dialogflow Intents**: - **Default Welcome
Intent** - **New Order** - **Order Add** - **Order Remove** - **Order
Complete** - **Order Track** - **Order Tracked** - **Work Timings**

------------------------------------------------------------------------

## 📸 Screenshots

### Dialogflow Intents

<img width="742" height="527" alt="Intents" src="https://github.com/user-attachments/assets/bb662d27-e4c8-4862-9455-95459186ef6e" />

### Database Tables

<img width="280" height="157" alt="Food_table" src="https://github.com/user-attachments/assets/e05b2f89-acdb-4237-902a-2e0f56388a70" />
<img width="336" height="189" alt="order_table" src="https://github.com/user-attachments/assets/bd5383fa-9fde-42a9-8cc7-03d6de0dd51a" />
<img width="226" height="127" alt="tracking_table" src="https://github.com/user-attachments/assets/c8a9456d-5e7e-46e3-b7e2-e723f986a72a" />

### Frontend with Chatbot

<img width="1366" height="768" alt="UI_Bot" src="https://github.com/user-attachments/assets/17d03836-3efa-4997-8673-616b2c35906c" />

### Chatbot in Action

<img width="370" height="556" alt="Chat1" src="https://github.com/user-attachments/assets/94ce8e03-74b8-4c06-a9fd-d3d85a3f3fa8" />
<img width="370" height="555" alt="Chat2" src="https://github.com/user-attachments/assets/07696608-24d4-4872-99f1-0bafe94b6a2a" />
<img width="370" height="556" alt="Chat3" src="https://github.com/user-attachments/assets/6afa764c-c741-43dd-b552-8af946a2443c" />
<img width="370" height="555" alt="Chat4" src="https://github.com/user-attachments/assets/19c7aa16-a10a-443d-a851-0ecaa71c849d" />
<img width="370" height="556" alt="Chat5" src="https://github.com/user-attachments/assets/9614876a-bac1-47da-b6ab-c48a67df4a27" />
<img width="370" height="555" alt="Chat6" src="https://github.com/user-attachments/assets/481cd914-aa14-4b9d-b40c-7fd0f1236f78" />

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Python (FastAPI)**
-   **Dialogflow**
-   **SQL Database**
-   **HTML/CSS/JS (Frontend)**

------------------------------------------------------------------------

## 🤝 Contribution

Contributions are welcome! Feel free to fork, open issues, and submit
pull requests.

------------------------------------------------------------------------

## 📜 License

---.
