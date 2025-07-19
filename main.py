# локально беру веса со своего диска 
# !pip install -U diffusers

# Импорты
import torch
from diffusers import StableDiffusionPipeline  # Используем StableDiffusionPipeline для .safetensors
from google.colab import drive

# drive.mount('/content/drive')

# Путь к вашему файлу на Google Drive 
local_path = "/content/drive/MyDrive/AnythingV4.5VAE.safetensors"

# Загрузка модели из локального .safetensors файла , файл весов оказался слишком большим для гитхаба, так что лучше используйте репозиторий и можете оттуда скачать файл весов

# Loading the model from the local .safetensors file, the weights file turned out to be too large for the github, so it's better to use the repository and you can download the weights file from there


# pipe = StableDiffusionPipeline.from_single_file(
#     local_path,
#     torch_dtype=torch.float32,  # float16 Half-precision для ускорения и экономии памяти
#     safety_checker=None  # Отключаем цензуру
# )

repo_id = "Yntec/AnythingV4.5.6.7.8"  #  repo; если не то, замените на другой (поиск на huggingface.co)
pipe = DiffusionPipeline.from_pretrained(
    repo_id,
    torch_dtype=torch.float32,  # float16 Half-precision для ускорения и экономии памяти
    safety_checker=None  # Отключаем цензуру 
)
# Переносим модель на GPU (ОБЯЗАТЕЛЬНО!)
pipe = pipe.to("cuda")

# Включаем оптимизации для ускорения (опционально, если xformers установлен; иначе закомментируйте)
# !pip install xformers  # Установите, если нужно
#pipe.enable_xformers_memory_efficient_attention()

# Negative prompt 
negative_prompt = 'blurry, deformed, ugly, mutated hands, extra limbs, low quality, watermark, text, censored, poorly drawn face, bad anatomy, low resolution'

# Prompt 
prompt = "playful anime girl, high resolution, masterpiece, 4k, vibrant sunlight"

# Генерация изображения
image = pipe(prompt, negative_prompt=negative_prompt, height=768, width=768).images[0]
image.save("test1.png")
image  # Отобразить изображение в Colab (если нужно)
