# AI Image Detector

## Overview

AI Image Detector is a web application that identifies whether an uploaded image is AI-generated or a real photograph. The project uses a pre-trained deep learning model from Hugging Face and provides predictions through a FastAPI backend.

## Features

* Upload images through a simple interface
* Detect AI-generated images
* Classify images as:

  * AI Generated
  * Real Image
* FastAPI-based REST API
* Deep learning inference using PyTorch
* Hugging Face Transformers integration

## Project Structure

```text
project/
│
├── backend/
│   ├── app.py
│   ├── detector.py
│   ├── model_loader.py
│   └── __init__.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* FastAPI
* PyTorch
* Hugging Face Transformers
* Pillow (PIL)
* HTML
* CSS
* JavaScript

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-image-detector
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn backend.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### Predict Image

**POST** `/predict`

Upload an image file and receive a prediction.

Response:

```json
{
  "result": "AI Generated"
}
```

or

```json
{
  "result": "Real Image"
}
```

## How It Works

1. User uploads an image.
2. The image is processed using a Hugging Face processor.
3. The trained model performs inference.
4. The prediction is returned through the API.
5. The frontend displays the result.

## Future Improvements

* Drag-and-drop image upload
* Confidence score display
* Support for multiple image formats
* Batch image prediction
* Deployment on cloud platforms
* Improved AI detection models

## Author

Karan Patil

## License

This project is intended for educational and research purposes.
