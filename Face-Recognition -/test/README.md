# Face Recognition Application

A Python-based face recognition application that uses OpenCV for face detection and scikit-learn for face matching. No complex compilation requirements!

## Features

- **Face Encoding**: Encode known faces into a searchable database
- **Image Recognition**: Recognize faces in static images
- **Webcam Recognition**: Real-time face recognition from your webcam
- **Easy Menu Interface**: Simple command-line interface for all operations

## Installation

### Requirements
- Python 3.8+
- Webcam (for webcam feature)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `known_faces` directory and organize your reference images:
```
known_faces/
├── person1/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── ...
├── person2/
│   ├── photo1.jpg
│   └── ...
└── ...
```

3. Run the main application:
```bash
python main.py
```

## Usage

### Option 1: Encode Faces
Creates a database of face encodings from images in the `known_faces` directory:
```bash
python main.py
# Select option 1
```

### Option 2: Recognize Faces in an Image
Detects and recognizes faces in a single image file:
```bash
python recognize_image.py path/to/image.jpg
```

Output will be saved to `output/` directory with bounding boxes drawn around recognized faces.

### Option 3: Real-time Webcam Recognition
Runs live face recognition from your webcam:
```bash
python recognize_webcam.py
```

**Controls:**
- `ESC` or `q` - Exit
- `Space` - Pause/Resume

## Configuration

Edit `config.py` to adjust:
- `TOLERANCE` - Recognition strictness (lower = stricter, default 0.6)
- `PROCESS_EVERY_N_FRAMES` - Skip frames for performance (higher = faster but less responsive)
- `FRAME_WIDTH/HEIGHT` - Resolution for processing
- `MODEL` - Face detection model (HOG faster, CNN more accurate)

## Architecture

The app uses:
- **OpenCV DNN**: For face detection (HOG detector)
- **HOG Features**: For face feature extraction
- **Cosine Similarity**: For face matching against the database
- **scikit-learn**: For similarity calculations

## Troubleshooting

**No faces detected:**
- Ensure good lighting
- Face should be clearly visible and roughly 50+ pixels wide
- Check that images are in JPEG/PNG format

**Webcam not working:**
- Verify webcam is connected and working
- Check system permissions for camera access
- Try the alternative VideoCapture method

**Low recognition accuracy:**
- Adjust `TOLERANCE` in config.py (lower = stricter)
- Add more reference images per person
- Ensure reference images have good lighting

## Files

- `main.py` - Main menu interface
- `encode_faces.py` - Face encoding script
- `recognize_image.py` - Image recognition script
- `recognize_webcam.py` - Webcam recognition script
- `face_utils.py` - Utility functions
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies

## Limitations

- Accuracy depends on image quality and lighting
- Works best with frontal or near-frontal faces
- Slower than GPU-accelerated methods but works on CPU
- No advanced features like face alignment or multi-angle detection

## Future Improvements

- GPU acceleration support
- Better face alignment
- Multiple face detection per image
- Face attributes (age, emotion, etc.)
- Web interface
- Database backend for many faces

## License

MIT License

## Support

For issues or questions, please check the troubleshooting section or review the code comments.
