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
