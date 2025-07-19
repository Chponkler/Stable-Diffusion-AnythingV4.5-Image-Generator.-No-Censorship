A project for generating anime-style images using the AnythingV4.5 model via the Stable Diffusion Pipeline. Allows you to create high-quality images (768 x 768) with fine control through prompta.

## 🔥 Features
- Loading custom weights of the `.safetensors` model
- GPU acceleration (CUDA) support
- Memory optimization via `xformers`
- Flexible generation settings via:
- Positive/negative prompta
  - Arbitrary resolution
  - Censorship and nsfw content settings
- Integration with Google Colab

## ⚙️ Requirements
- Python 3.8+
- PyTorch (CUDA version)
- Libraries:
 pip install diffusers transformers accelerate safetensors xformers

## BETTER USE GOOGLE COLAB
## COPY THE CONTENTS OF THE CODE FILE AND PASTE IT INTO GOOGLE COLAB notebook, AND THEN UPLOAD THE WEIGHTS TO GOOGLE DRIVE IN THE ROOT FOLDER FIRST, AND THEN EVERYTHING WILL WORK 
## CHOOSE A THREAD WITH GPU GPU (T4 IS FREE)



<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/8be6cfbd-e1c6-41cd-81c1-7cd970840db8" />



Проект для генерации изображений в аниме-стиле с использованием модели AnythingV4.5 через Stable Diffusion Pipeline. Позволяет создавать высококачественные изображения (768x768) с тонким контролем через промпты.

## 🔥 Особенности
- Загрузка кастомных весов модели `.safetensors`
- Поддержка GPU-ускорения (CUDA)
- Оптимизация памяти через `xformers`
- Гибкая настройка генерации через:
  - Положительные/негативные промпты
  - Произвольное разрешение
  - Настройки цензуры и nsfw контента
- Интеграция с Google Colab

## ⚙️ Требования
- Python 3.8+
- PyTorch (CUDA версия)
- Библиотеки:
 pip install diffusers transformers accelerate safetensors xformers

## ЛУЧШЕ ИСПОЛЬЗУЙТЕ GOOGLE COLAB
## СКОПИРУЙТЕ СОДЕРЖИМОЕ ФАЙЛА С КОДОМ И ВСТАВЬТЕ В GOOGLE COLAB notebook, А ВЕСА ЗАГРУЗИТЕ НА СНАЧАЛА НА GOOGLE ДИСК В КОРНЕВУЮ ПАПКУ, И ТОГДА ВСЕ БУДЕТ РАБОТАТЬ 
## ВЫБЕРИТЕ СТРЕДУ С ГПУ GPU (Т4-БЕСПЛАТНАЯ)
