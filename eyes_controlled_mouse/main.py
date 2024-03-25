'''
This code is designed to create an "eye-controlled mouse"
where you can control the mouse cursor by moving your
eye and perform a click by winking. It uses facial
landmarks to achieve this interaction.
'''

import cv2 # openCV-python for computer vision tasks
import mediapipe as mp # from google Mediapipe for facial landmark detection
import pyautogui # PyAutoGUI for controlling the mouse

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Initialize the FaceMesh model from the Mediapipe library
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)# to improve the accuracy of landmark points.

# Get the screen dimensions using pyautogui
screen_w, screen_h = pyautogui.size()

# Main loop for processing frames from the webcam
while True:
    # Read a frame from the webcam
    _, frame = cam.read()

    # Flip the frame horizontally for a mirrored effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB (required by Mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using the FaceMesh model
    output = face_mesh.process(rgb_frame)

    # Get the detected landmark points from the output
    landmark_points = output.multi_face_landmarks

    # Get the height and width of the frame
    frame_h, frame_w, _ = frame.shape

    # Check if any landmark points were detected
    if landmark_points:
        # Get the landmark points for the first detected face
        landmarks = landmark_points[0].landmark

        # Iterate through specific landmarks and mark them with green circles
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            # If it's the second landmark (id == 1), move the mouse cursor
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Get the left eye landmarks for wink detection
        left = [landmarks[145], landmarks[159]]

        # Mark left eye landmarks with yellow circles
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Check if the difference in y-coordinates of left eye landmarks is small
        if (left[0].y - left[1].y) < 0.01:#0.004
            # Perform a mouse click action
            pyautogui.click()
            pyautogui.sleep(1)

    # Display the modified frame with annotations
    cv2.imshow('Eye Controlled Mouse', frame)
    # Wait for a key press event for a short duration
    cv2.waitKey(1)

# Release the webcam and close the OpenCV window
#cam.release()
#cv2.destroyAllWindows()