"""
Script to encode known faces and store them in a database (OpenCV DNN version)
Place images in known_faces/ directory, organized as: known_faces/person_name/image.jpg

This version uses OpenCV instead of face_recognition to avoid dlib compilation issues.

Usage:
    python encode_faces.py
"""

import os
import cv2
from face_utils import (
    get_face_files_from_directory,
    save_encoded_faces,
    load_image,
    detect_faces_opencv,
    extract_face_features
)
import config


def encode_faces():
    """
    Scan known_faces directory, encode all faces, and save to database
    """
    print("Starting face encoding process (OpenCV DNN version)...")
    print(f"Reading from: {config.KNOWN_FACES_DIR}")
    print(f"Saving to: {config.ENCODINGS_FILE}\n")
    
    # Get all face images organized by person
    face_files = get_face_files_from_directory(config.KNOWN_FACES_DIR)
    
    if not face_files:
        print(f"No subdirectories found in {config.KNOWN_FACES_DIR}")
        print("Please organize your images as: known_faces/person_name/image.jpg")
        return
    
    known_encodings = []
    known_names = []
    
    total_images = sum(len(images) for images in face_files.values())
    processed = 0
    skipped = 0
    
    # Process each person
    for person_name, image_paths in face_files.items():
        print(f"\nProcessing: {person_name}")
        print(f"  Images found: {len(image_paths)}")
        
        person_encoding_count = 0
        
        for image_path in image_paths:
            processed += 1
            print(f"  [{processed}/{total_images}] {os.path.basename(image_path)}", end=" ... ")
            
            # Load image
            image = load_image(image_path)
            if image is None:
                print("FAILED (could not load)")
                skipped += 1
                continue
            
            # Detect faces in image
            try:
                face_rects = detect_faces_opencv(image, conf_threshold=0.5)
            except Exception as e:
                print(f"FAILED (detection error: {e})")
                skipped += 1
                continue
            
            if len(face_rects) == 0:
                print("FAILED (no faces detected)")
                skipped += 1
                continue
            elif len(face_rects) > 1:
                print(f"WARNING (found {len(face_rects)} faces, using first)")
            
            # Extract features from first face in image
            try:
                features = extract_face_features(image, face_rects[0])
                if features is None:
                    print("FAILED (could not extract features)")
                    skipped += 1
                    continue
                
                known_encodings.append(features)
                known_names.append(person_name)
                person_encoding_count += 1
                print("OK")
            
            except Exception as e:
                print(f"FAILED (feature extraction error: {e})")
                skipped += 1
                continue
        
        print(f"  Encodings created: {person_encoding_count}")
    
    # Save to database
    if known_encodings:
        save_encoded_faces(known_encodings, known_names)
        print(f"\n{'='*50}")
        print(f"SUCCESS!")
        print(f"  Total images processed: {processed}")
        print(f"  Successfully encoded: {len(known_encodings)}")
        print(f"  Skipped: {skipped}")
        print(f"  Database saved to: {config.ENCODINGS_FILE}")
        print(f"{'='*50}")
    else:
        print("\nFAILED: No faces were successfully encoded.")
        print("Please check your images and try again.")


if __name__ == "__main__":
    encode_faces()
