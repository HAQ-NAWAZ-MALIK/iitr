---
title: Ocr Iitr
emoji: 📚
colorFrom: yellow
colorTo: yellow
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---
# OCR Image to Text Converter

## Overview

This project is an OCR (Optical Character Recognition) application that allows users to extract text from images. It supports multiple languages and provides a user-friendly interface for uploading images, performing OCR, and searching within the extracted text.

## Features

- Upload images for text extraction
- Support for multiple languages (including Hindi, English, Thai, French, Chinese, Japanese, and Korean)
- Visualize OCR results with bounding boxes around detected text
- Search functionality within the extracted text
- Example images provided for testing
## Alternative Version

An alternative, ready-to-use version of this OCR application is available on Vercel. You can access it [here](https://iitr-haq-nawaz-maliks-projects.vercel.app/).
## Technologies Used

- Python
- Gradio (for the web interface)
- EasyOCR (for optical character recognition)
- PIL (Python Imaging Library)
- PyTorch

## Setup and Installation

1. Clone this repository:
   ```
   git clone https://huggingface.co/spaces/Omarrran/ocr_iitr
   cd ocr_iitr
   ```

2. Install the required dependencies:
   ```
   pip install pillow gradio torch easyocr
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to the local URL provided by Gradio (usually `http://127.0.0.1:7860`).

## Usage

1. Upload an image or select one of the provided examples.
2. Choose the language(s) for OCR processing.
3. Click the "Perform OCR" button to extract text from the image.
4. View the result image with bounding boxes and the extracted text.
5. Use the search box to find specific text within the extracted content.

## Example Images

The application includes several example images for testing:

- English text
- Hindi text
- Thai text
- French text
- Chinese text
- Japanese text
- Korean text

These images are automatically downloaded when you run the application.



## Notes

- The OCR process may take a few seconds to complete, especially for larger or more complex images.
- The accuracy of text extraction may vary depending on the quality of the input image and the complexity of the text.

## Contributing

Contributions to improve the application are welcome. Please feel free to submit issues or pull requests.

## License

license: mit
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
