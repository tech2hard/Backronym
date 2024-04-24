import pathlib
import textwrap
import google.generativeai as genai
import os
import gradio as gr


def gemini_chat_builder(language_input,type_input,name_input,details_input):
    if not details_input:
        response=chat.send_message(f"""please create full form of each letter in word {name_input} with type related to {type_input}. For clear idea use more info here,{details_input} please provide response in language {language_input}""",generation_config=generation_config)
    else:
        response=chat.send_message(f"""please create full form of each letter in word {name_input} with type related to {type_input} in language {language_input}""",generation_config=generation_config)        
    return response.text
    #return f"""The {type_input} is required for the {name_input}"""

API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

#model=genai.GenerativeModel('gemini-pro')
model=genai.GenerativeModel('gemini-pro')
generation_config=genai.GenerationConfig(
    stop_sequences=None,
    temperature=0.9,
    top_p=1.0,
    top_k=40,
    candidate_count=1,
    max_output_tokens=2000
)

chat=model.start_chat()

demo=gr.Interface(
    gemini_chat_builder,[
    gr.Dropdown(
        ["English","Spanish","Chinese","Japanese","Korean","Hindi"],multiselect=False,label="Language",info="Select Language",value="English"
    ),
    gr.Dropdown(
        ["Technology","Funny","Food","Clothing","Gaming"],multiselect=False,label="Type",info="Select Type of Backronym",value="Technology"
    ),
    gr.Textbox(
        label="Input Name",
        info="Type Name to get Acronym",
        lines=1,
        value="Google"
    ),
    gr.Textbox(
        label="Input Details",
        info="Add details to create more meaningful Backronym",
        lines=1,
        value="Google is software Company"
    )],
    "text",title="Backronym Generator",css="footer {visibility: hidden}",allow_flagging="never",submit_btn=gr.Button("Generate")
)

if __name__=='__main__':
    demo.launch()
