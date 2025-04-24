import cv2
import face_recognition
import numpy as np
import os


known_faces_dir = "known_faces"  
known_face_encodings = []
known_face_names = []

# Load and encode known faces
for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
       
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
        
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:  # Ensure at least one face is found
            encoding = face_encodings[0]  # Use the first face encoding
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])  # Use the filename as the name

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

  
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through detected faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
       
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown Face"  
        color = (0, 0, 255)  # Red color 

        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            color = (0, 255, 0)  # Green color

        # Scale the face location back to the original frame size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

     
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        
        cv2.putText(frame, name, (left, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()