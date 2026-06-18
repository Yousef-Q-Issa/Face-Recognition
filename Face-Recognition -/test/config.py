"""
Configuration file for Face Recognition App
Adjust these parameters based on your needs and hardware
"""

# Path settings
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
OUTPUT_DIR = "output"
ENCODINGS_DIR = "encodings"
ENCODINGS_FILE = "encodings/encodings.pkl"

# Face recognition settings
# Tolerance: lower = stricter matching, higher = more permissive
# Range: 0.4-0.7, default 0.6
TOLERANCE = 0.6

# Model type for face detection
# "hog" = faster (10-30 FPS), suitable for CPU
# "cnn" = slower (1-5 FPS) but more accurate, requires GPU
MODEL = "cnn"

# Webcam settings
PROCESS_EVERY_N_FRAMES = 1  # Process every Nth frame for speed (1 = all frames, 5 = every 5th)
FRAME_WIDTH = 800  # Reduced resolution for real-time processing
FRAME_HEIGHT = 600

# Display settings
SHOW_FACE_LABELS = True
LABEL_FONT_SIZE = 0.6
LABEL_THICKNESS = 2
BOX_COLOR = (0, 255, 0)  # Green (BGR format)
TEXT_COLOR = (0, 255, 0)  # Green
