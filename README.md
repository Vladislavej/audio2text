# **Whisper Audio Transcription with Python**

This project uses **Whisper by OpenAI**, an advanced speech recognition model, to transcribe audio and video files into text. Whisper supports multiple languages and is highly accurate. This repository demonstrates how to install and use Whisper for transcription, with support for both **CPU** and **GPU**.

## **Features**

- Automatic language detection
- Transcription of audio and video files
- Support for multiple Whisper model sizes (from `tiny` to `large`)
- GPU acceleration for faster processing

## **Installation**

### 1. Install Whisper

Whisper is available as an open-source Python package, and you can install it via pip:

```bash
pip install git+https://github.com/openai/whisper.git
```

### 2. Install `ffmpeg`

Whisper relies on `ffmpeg` to handle audio processing. Download and install `ffmpeg`:

- Download `ffmpeg` from the official website: [FFmpeg Download](https://ffmpeg.org/download.html).
- Choose the version that matches your operating system and follow the installation instructions.
- **Note:** Ensure `ffmpeg` is added to your system's PATH so that Whisper can locate it.

### 3. Install PyTorch with GPU Support (Optional but Recommended)

To enable GPU acceleration, you need PyTorch installed with **CUDA** support. Install PyTorch as follows:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

- Replace `cu118` with your correct CUDA version if necessary.
- You can check your CUDA version by running:
  ```bash
  nvcc --version
  ```

Visit the [PyTorch Installation Guide](https://pytorch.org/get-started/locally/) for more details.

## **Whisper Model Sizes**

Whisper provides several model sizes to balance between speed and accuracy. You can choose the model size that fits your needs:

- **Tiny model**: Fast, but less accurate.
- **Base model**: Balanced between speed and accuracy.
- **Small model**: More accurate but slower than base.
- **Medium model**: Even more accurate but slower.
- **Large model**: Most accurate, but the slowest.

Model size choice will depend on your requirements (speed vs accuracy) and available hardware.
