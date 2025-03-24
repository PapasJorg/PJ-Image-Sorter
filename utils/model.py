import shutil,requests, os, torch, transformers
from tqdm import tqdm
import pandas as pd
from pathlib import Path
from transformers import pipeline

transformers.logging.set_verbosity_error()

#no longer used, could be used to list hugginface models and let the user pick
def list_models(task="zero-shot-image-classification"):
    url = "https://huggingface.co/api/models"
    params = {"pipeline_tag": task, "sort": "downloads"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        models = response.json()
        model_names = [model["id"] for model in models]
        return model_names
    else:
        raise Exception(f"Error fetching models: {response.text}")

def classify_images(image_files, destination, model_name, labels, operation='copy', output_file="output.csv", batch_size=32, verbose=True):
    destination = Path(destination)
    data = pd.DataFrame(columns=['image_name', 'label', 'score'])

    #Build a prompt-to-label map
    prompt_map = {
        f"a photo of a {label.strip()}": label.strip()
        for label in labels
    }
    prompt_labels = list(prompt_map.keys())  # used as candidate_labels for CLIP

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    detector = pipeline(model=model_name, task="zero-shot-image-classification", device=device)
    print(f"Model loaded  in {str(device).upper()}: {model_name}")
    results = []

    for start in tqdm(range(0, len(image_files), batch_size), desc=f"Classifying {len(image_files)} images in batches of {batch_size}..."):
        batch_files = image_files[start:start+batch_size]
        for image in batch_files:
            #print(f"Processing {image}")
            try:
                result = detector(image, candidate_labels=prompt_labels)

                #modifying label logic here
                best_prompt = result[0]['label']
                label = prompt_map[best_prompt]
                # print(f"Label: {label}")
                score = round(result[0]['score'],2)
                results.append((image, label, score))
                label_dir = os.path.join(destination, label)
                if not os.path.exists(label_dir):
                    os.makedirs(label_dir)
                # Extract the filename
                image_filename = os.path.basename(image)
                if operation == "move":
                    shutil.move(image, os.path.join(label_dir, image_filename))
                elif operation == "copy":
                    shutil.copy2(image, os.path.join(label_dir, image_filename))
            except Exception as e:
                print(f"Error processing {image}: {e}")
            
        columns = ['image_name', 'label', 'score']
        data = pd.DataFrame(results, columns=columns)
    
    output_file = os.path.join(destination, output_file)
    data.to_csv(output_file, index=False)
    if verbose:
        print(f"Classification finished. Results saved to {output_file}")