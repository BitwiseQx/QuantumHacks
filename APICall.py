import os
import openai
import gradio as gr
import webbrowser

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:"

def openai_create(prompt):
    stop_sequence = " Human:"
    if not prompt.endswith(stop_sequence):
        prompt += stop_sequence
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", "AI:"]
    )
    return response.choices[0].text

def conversation_history(input, history):
    history = history or []
    
    # Open the specified URL unconditionally
    webbrowser.open("https://bitwise.zapier.app/")
    history.append(("Command to open URL", "Redirected to URL"))
    
    return history, history

blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Click")
    submit.click(conversation_history, inputs=[message, state], outputs=[chatbot, state])

blocks.launch(debug=True)
