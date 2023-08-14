# Python intern at SYNC INTERN'S
# Author: Bishoy Kamel Mamdouh
# Task 4: Build your own Chatbot


import tkinter as tk
from tkinter import ttk
import random

def get_random_response(responses):
    return random.choice(responses)

def get_bot_response(user_input):
    user_input = user_input.lower()
    bot_responses = {
        "hello": ["Hello! How can i help you?"],
        "how are you": ["I'm just a tour guide chatbot, I have no feelings, but thank you for asking."],
        "what is your name": ["I'm an Egypt Explorers chatbot. You can call me Pharaoh."],
        "bye": ["Wishing you good health! Goodbye!"],
        "please tell me about the pyramids": ["The pyramids are one of the most recognizable landmarks in the world, located primarily on the outskirts of Cairo, Egypt. The three largest and most famous ones are the Pyramids of Giza."],
        "what activities can i do there": ["You can visit the Great Pyramid of Giza, Khafre's Pyramid, Menkaure's Pyramid, and the Sphinx, Experience a unique mode of transportation by taking a camel or horseback ride around the pyramids' complex."],
        "tell me food recommendations": ["Egypt is known for its delicious cuisine. Here are some food recommendations for your visit to Egypt: Koshari, Ful Medames, Shawarma, Molokhia, Kunafa. These are just a few examples of the many delicious dishes you can try during your visit to Egypt."],
        "what is the best time of year to visit egypt": ["The peak tourist season in Egypt is during the winter months (November to February) when temperatures are milder, This is an ideal time for sightseeing, especially in Cairo, Luxor, and Aswan."],
        "thank you": ["You're welcome! If you have any more questions or need further assistance, feel free to ask. Have a great trip to Egypt!"],
        "": [""],
        "": [""],
        "": [""],
        "default": ["I'm sorry, I don't understand."]
    }
    return bot_responses.get(user_input, bot_responses["default"])

def on_send_message():
    user_input = user_entry.get()
    if user_input.lower() == "bye":
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        chat_log.insert(tk.END, "Pharaoh: " + get_random_response(get_bot_response("bye")) + "\n\n")
        user_entry.delete(0, tk.END)
    else:
        response = get_bot_response(user_input)
        bot_response = "Pharaoh: " + get_random_response(response) + "\n\n"
        chat_log.insert(tk.END, "You: " + user_input + "\n\n")
        chat_log.insert(tk.END, bot_response)
        user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Egypt Explorers Chatbot")

chat_frame = ttk.Frame(root)
chat_frame.pack(expand=True, fill="both")

chat_log = tk.Text(chat_frame, wrap="word", bg="white", font=("Arial", 14))
chat_log.pack(expand=True, fill="both")

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

user_entry = ttk.Entry(input_frame, width=50, font=("Arial", 14))
user_entry.pack(side="left", padx=5)

send_button = ttk.Button(input_frame, text="Send", command=on_send_message)
send_button.pack(side="left", padx=5)

user_entry.bind("<Return>", on_send_message)

root.mainloop()
