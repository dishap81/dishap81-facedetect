import cv2
import face_recognition
import os
import pickle

name = input("Enter name of person: ")

dataset_path = "dataset"
person_path = os.path.join(dataset_path, name)

if not os.path.exists(person_path):
    os.makedirs(person_path)

cap = cv2.VideoCapture(0)
count = 0

print("Press SPACE to capture image, ESC to exit")

while True:
    ret, frame = cap.read()
    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1)

    if key % 256 == 27:  # ESC
        break
    elif key % 256 == 32:  # SPACE
        img_name = f"{person_path}/{name}_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved {img_name}")
        count += 1

cap.release()
cv2.destroyAllWindows()

# Create encodings
known_encodings = []
known_names = []

for person in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person)
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person)

data = {"encodings": known_encodings, "names": known_names}

with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("Encodings saved successfully!")