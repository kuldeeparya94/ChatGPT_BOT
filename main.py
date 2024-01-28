import gradio as gr
import openai

# Set your OpenAI API key
openai.api_key = "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"


def chat_gpt(input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input},
        ],
        temperature=0.2,
        max_tokens=150
    )

    text = completion.choices[0].message.content
    return text


iface = gr.Interface(fn=chat_gpt, inputs="text", outputs="text")
iface.launch()
