import os
import gdown

def download_model():
    model_url = 'https://drive.google.com/uc?id=1J_VeEgua7TZQU8KJ0bJzWaAPyhv-Euwf'  # remplace par ton vrai ID
    output_path = 'alzheimer_model_201.h5'

    if not os.path.exists(output_path):
        print("Téléchargement du modèle depuis Google Drive...")
        gdown.download(model_url, output_path, quiet=False)
    else:
        print("Modèle déjà présent.")
