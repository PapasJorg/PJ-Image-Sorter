                             PJ Jewelry Image Sorter
PJ Jewelry Image Sorter is an AI-powered tool that automatically classifies jewelry images into categories such as rings, watches, earrings, bracelets, necklaces, and more. It uses state-of-the-art vision models (like OpenAI's CLIP) to recognize objects in images and sort them into folders — fully automated, with no manual labeling required.

 Features
 AI Classification with CLIP (zero-shot)

 Automatically organizes images into subfolders by category

Tailored for luxury jewelry items (including custom pieces)

 Simple interface using Google Colab

 Works directly with Google Drive

 Built on open-source foundations (Apache 2.0)

 Client-ready customization & branding support

 How It Works
Upload images to a Google Drive folder (e.g., MyDrive/ImageFolder)

Mount Drive in Google Colab

Choose a model (default: openai/clip-vit-base-patch32)

Set your desired labels (e.g., ring, watch, bracelet, etc.)

Click Start Classification

Images are sorted into subfolders like:

bash
Copy
Edit
MyDrive/ImageFolder/sorted-jewelry/
├── ring/
├── bracelet/
├── watch/
└── other/
📸 Ideal Use Cases
Jewelry retailers managing product images

Instagram/e-commerce photo sorting

Brands with mixed product catalogs (watches, rings, earrings)

Automating manual categorization workflows

🛠 Requirements
Python Packages
If you're running this outside of Colab, install dependencies:

bash
Copy
Edit
pip install pillow transformers torchvision timm huggingface_hub opencv-python

Google Colab :
No setup required — just run the notebook and mount your Google Drive.

 Powered By
This sorter uses:

OpenAI’s CLIP for image recognition
Custom logic for folder setup, labeling, and category scoring
Code originally inspired by bellingcat/smart-image-sorter (Apache 2.0)

Folder Structure

pj-image-sorter/
├── PJ_Jewelry_Image_Sorter.ipynb      # Main notebook (Colab-friendly)
└── utils/
    ├── f_manager.py                   # File and directory handling
    └── model.py                       # Image classification with CLIP

🧪 Supported Categories
These are the default labels (editable in the notebook UI):

 ring

 engagement ring

 bracelet

 earring

 pendant / necklace / chain

 watch

 custom piece

 other (fallback if no match)

🛡 License
This project is released under the Apache 2.0 License.

You are free to use, modify, distribute, and build upon this code — even commercially — as long as you include:

A copy of the Apache 2.0 license


Customization & Branding
Want to white-label this sorter for your company or brand?

We offer:

Custom categories & keywords

Private Colab links for clients

Hosted dashboard version (no coding required)

AI tuning for fashion, accessories, or general products

Contact us to learn more.