import PIL
from PIL import Image
from PIL import ImageDraw
import gradio as gr
import torch
import easyocr
import re

# Download example images (same as before)
# Download example images
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/english.png', 'english.png')
torch.hub.download_url_to_file('https://i.imgur.com/mwQFd7G.jpeg', 'Hindi.jpeg')
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/thai.jpg', 'thai.jpg')
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/french.jpg', 'french.jpg')
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/chinese.jpg', 'chinese.jpg')
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/japanese.jpg', 'japanese.jpg')
torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/korean.png', 'korean.png')

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def format_extracted_text(bounds):
    return " ".join([text for _, text, _ in bounds])

def highlight_search_results(text, search_query):
    if not search_query:
        return text, []
    pattern = re.compile(re.escape(search_query), re.IGNORECASE)
    matches = list(pattern.finditer(text))
    highlighted_text = pattern.sub(lambda m: f"**{m.group()}**", text)
    return highlighted_text, matches

def inference(img, lang):
    reader = easyocr.Reader(lang)
    bounds = reader.readtext(img)
    im = PIL.Image.open(img)
    draw_boxes(im, bounds)
    im.save('result.jpg')
    
    extracted_text = format_extracted_text(bounds)
    
    return ['result.jpg', extracted_text]

def search_text(text, search_query):
    highlighted_text, matches = highlight_search_results(text, search_query)
    
    if matches:
        result = f"Found {len(matches)} occurrence(s) of \"{search_query}\":\n"
        for i, match in enumerate(matches, 1):
            context_start = max(0, match.start() - 20)
            context_end = min(len(text), match.end() + 20)
            context = text[context_start:context_end]
            result += f"{i}. ...{context}...\n"
    else:
        result = f"No occurrences of \"{search_query}\" found."
    
    return highlighted_text, result

title = 'Image To Text OCR Converter'
subtitle = 'Extract Hindi/English or both or any Text From Image'
description = 'This application is being built on the request of IIT R Internship Assignment. It allows users to upload a single image, processes the image to extract text using OCR, and provides a basic search feature.'

note = 'Please keep patience while processing the OCR, as it may take a few seconds to complete'


alternative_link = "[Alternative: Ready-to-use OCR using Vercel](https://iitr-haq-nawaz-maliks-projects.vercel.app/)"

examples = [
    ['english.png', ['en']],
    ['Hindi.jpeg', ['hi', 'en']],
    ['thai.jpg', ['th', 'en']],
    ['french.jpg', ['fr', 'en']],
    ['chinese.jpg', ['ch_sim', 'en']],
    ['japanese.jpg', ['ja', 'en' ]],
    ['korean.png', ['ko', 'en' ]]
]

css = """
.output_image, .input_image {height: 40rem !important; width: 100% !important;}
.search_results {margin-top: 1rem; padding: 1rem; background-color: #f0f0f0; border-radius: 4px;}
.centered-title {text-align: center; font-size: 2.5em; font-weight: bold; margin-bottom: 0.5em;}
.centered-subtitle {text-align: center; font-size: 1.5em; margin-bottom: 1em;}
.alternative-link {text-align: center; margin-top: 1em; font-style: italic;}
"""


choices = [
    "abq", "ady", "af", "ang", "ar", "as", "ava", "az", "be", "bg", "bh", "bho", "bn", "bs", "ch_sim", "ch_tra", 
    "che", "cs", "cy", "da", "dar", "de", "en", "es", "et", "fa", "fr", "ga", "gom", "hi", "hr", "hu", "id", 
    "inh", "is", "it", "ja", "kbd", "kn", "ko", "ku", "la", "lbe", "lez", "lt", "lv", "mah", "mai", "mi", "mn", 
    "mr", "ms", "mt", "ne", "new", "nl", "no", "oc", "pi", "pl", "pt", "ro", "ru", "rs_cyrillic", "rs_latin", 
    "sck", "sk", "sl", "sq", "sv", "sw", "ta", "tab", "te", "th", "tjk", "tl", "tr", "ug", "uk", "ur", "uz", "vi"
]

with gr.Blocks(css=css) as iface:
    gr.Markdown(f"# {title}")
    gr.Markdown(f"## {subtitle}")
    gr.Markdown(description)
    gr.Markdown(note)
    gr.Markdown(alternative_link)
    with gr.Row():
        with gr.Column(scale=2):
            input_image = gr.Image(type="filepath", label="Upload Image")
            lang_select = gr.CheckboxGroup(choices=choices, label="Select Languages", value=['hi', 'en'])
            ocr_button = gr.Button("Perform OCR")
        
        with gr.Column(scale=3):
            output_image = gr.Image(type="filepath", label="OCR Result")
            extracted_text = gr.Markdown(label="Extracted Text")
            search_box = gr.Textbox(label="Search in extracted text")
            search_button = gr.Button("Search")
            search_results = gr.Markdown(label="Search Results")
    
    ocr_button.click(inference, inputs=[input_image, lang_select], outputs=[output_image, extracted_text])
    search_button.click(search_text, inputs=[extracted_text, search_box], outputs=[extracted_text, search_results])
    
    gr.Examples(examples, inputs=[input_image, lang_select])

iface.launch()