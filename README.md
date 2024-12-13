## Object-Detection
Hosted API Inference with results in JSON format

## Overview
This project provides an API for object detection that accepts image inputs, performs inference using a pre-trained object detection model, and returns results in a structured JSON format. The system is designed for ease of use and integration into applications requiring object detection functionality.

## Features
- API : An API endpoint to upload images and receive inference results.
- Annotation : Images are Manulally labelled in Roboflow. 
- Model : Pre-trained model using Roboflow with yolov8.
- Result : Inference results include detected objects, bounding box coordinates, and confidence scores in JSON.

## Prerequisites
To run this project locally, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (optional, but recommended)

- Python Libraries:
    - Python Libraries:
        - requests
        - Pillow
        - requests_toolbelt
        - opencv-python
     
  ## Detected Images with its JSON inference

  Image 1 - ![image](https://github.com/user-attachments/assets/69dc9544-888a-4274-8a0f-973342898664)

  
  Result - {
  "predictions": [
    {
      "x": 281.5,
      "y": 764,
      "width": 263,
      "height": 378,
      "confidence": 0.982,
      "class": "T-shirt",
      "class_id": 4,
      "detection_id": "96811166-46fc-466d-ace1-2b5c27869561"
    },
    {
      "x": 169.5,
      "y": 919.5,
      "width": 71,
      "height": 209,
      "confidence": 0.973,
      "class": "Glove",
      "class_id": 0,
      "detection_id": "d259da8b-8f8c-43fb-bfb5-7cd0e62b47f4"
    },
    {
      "x": 602.5,
      "y": 889.5,
      "width": 129,
      "height": 231,
      "confidence": 0.969,
      "class": "Glove",
      "class_id": 0,
      "detection_id": "5b3563a8-66c3-4423-ae95-c404899ab313"
    },
    {
      "x": 543,
      "y": 686,
      "width": 276,
      "height": 368,
      "confidence": 0.968,
      "class": "T-shirt",
      "class_id": 4,
      "detection_id": "1c9c4560-aa83-4251-80ab-42f3e5937405"
    },
    {
      "x": 817,
      "y": 1511,
      "width": 184,
      "height": 154,
      "confidence": 0.967,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "e8bf0dfb-0c3d-4a85-989a-b646ef7b0177"
    },
    {
      "x": 306.5,
      "y": 478,
      "width": 135,
      "height": 104,
      "confidence": 0.962,
      "class": "Helmet",
      "class_id": 1,
      "detection_id": "894d943c-e095-4bb5-a9c4-2d5348b7a80b"
    },
    {
      "x": 525,
      "y": 393,
      "width": 144,
      "height": 114,
      "confidence": 0.957,
      "class": "Helmet",
      "class_id": 1,
      "detection_id": "7b2abd8f-4ca1-4584-9def-a277e6f70747"
    },
    {
      "x": 808.5,
      "y": 215,
      "width": 171,
      "height": 122,
      "confidence": 0.954,
      "class": "Helmet",
      "class_id": 1,
      "detection_id": "993f1a0c-9b6f-436b-aa98-c3c66c501f49"
    },
    {
      "x": 322,
      "y": 1331,
      "width": 74,
      "height": 110,
      "confidence": 0.947,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "ac6ecede-58ab-458e-9daf-5bc2d71daa7f"
    },
    {
      "x": 694,
      "y": 1394.5,
      "width": 122,
      "height": 97,
      "confidence": 0.946,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "813ae17d-8487-4864-a063-6753bb59d0d7"
    },
    {
      "x": 457.5,
      "y": 1350,
      "width": 151,
      "height": 112,
      "confidence": 0.946,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "27bacf6d-fce9-4ca8-ba36-1b7b1075cdfd"
    },
    {
      "x": 853,
      "y": 561.5,
      "width": 342,
      "height": 429,
      "confidence": 0.936,
      "class": "T-shirt",
      "class_id": 4,
      "detection_id": "567cfa70-d281-44cb-b4af-dd4704cac4c7"
    },
    {
      "x": 413.5,
      "y": 896,
      "width": 55,
      "height": 220,
      "confidence": 0.919,
      "class": "Glove",
      "class_id": 0,
      "detection_id": "c8586116-8a64-42e9-952d-0c59f7ecd086"
    },
    {
      "x": 942.5,
      "y": 824,
      "width": 141,
      "height": 290,
      "confidence": 0.918,
      "class": "Glove",
      "class_id": 0,
      "detection_id": "2a23b614-de58-4edc-8be0-f9e977cb47e3"
    },
    {
      "x": 362,
      "y": 913,
      "width": 72,
      "height": 214,
      "confidence": 0.8,
      "class": "Glove",
      "class_id": 0,
      "detection_id": "bd4da41c-4946-45bf-b42e-ff16568595b6"
    },
    {
      "x": 190,
      "y": 1314.5,
      "width": 128,
      "height": 79,
      "confidence": 0.735,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "b2cca92c-b89a-49da-82a3-fa220736794a"
    }
  ]

}

Image 2 - ![image](https://github.com/user-attachments/assets/751336e6-cbae-4e2d-a0bf-f8f157404727)

Result - {
  "predictions": [
    {
      "x": 342.5,
      "y": 593.5,
      "width": 269,
      "height": 389,
      "confidence": 0.983,
      "class": "T-shirt",
      "class_id": 4,
      "detection_id": "20c35f60-0c02-49d2-b67e-06aa5d0a3b93"
    },
    {
      "x": 584,
      "y": 611,
      "width": 240,
      "height": 388,
      "confidence": 0.976,
      "class": "T-shirt",
      "class_id": 4,
      "detection_id": "b7ad7762-fa0c-4da7-8265-d6fdd57c26e0"
    },
    {
      "x": 572.5,
      "y": 300.5,
      "width": 133,
      "height": 97,
      "confidence": 0.953,
      "class": "Helmet",
      "class_id": 1,
      "detection_id": "14beb2de-e059-4e2e-896d-6301ae37cb9d"
    },
    {
      "x": 628,
      "y": 1154.5,
      "width": 98,
      "height": 113,
      "confidence": 0.949,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "3b4ad6fd-79d0-4d2f-a5db-d487fc540b9d"
    },
    {
      "x": 491,
      "y": 1140.5,
      "width": 104,
      "height": 97,
      "confidence": 0.946,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "999c38fd-3167-4992-a300-74da2c45c39c"
    },
    {
      "x": 345.5,
      "y": 279.5,
      "width": 133,
      "height": 101,
      "confidence": 0.942,
      "class": "Helmet",
      "class_id": 1,
      "detection_id": "ea2a2336-fa92-4659-845c-b5d2195d1b2b"
    },
    {
      "x": 750.5,
      "y": 1105,
      "width": 129,
      "height": 82,
      "confidence": 0.907,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "d17948bd-8b3f-4d4e-858f-86034c7e9f2e"
    },
    {
      "x": 842,
      "y": 1151.5,
      "width": 98,
      "height": 99,
      "confidence": 0.865,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "c8d04ba7-d381-4f36-9049-b165b5cae996"
    },
    {
      "x": 410,
      "y": 1173.5,
      "width": 58,
      "height": 97,
      "confidence": 0.588,
      "class": "Shoe",
      "class_id": 3,
      "detection_id": "619aa235-ea11-441d-a4dd-bc3585923bc6"
    }
  ]
}

Image 3 - ![image](https://github.com/user-attachments/assets/5084f66d-8d6c-4150-8bae-a7d63a950964)

Result - 




