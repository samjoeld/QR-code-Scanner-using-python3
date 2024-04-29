import cv2
from pyzbar.pyzbar import decode
import pygame

def play_scan_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("pip.mp3")  # Provide the path to your sound file
    pygame.mixer.music.play()

def scan_qr_code():
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()

        # Decode QR code
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # Draw bounding box around the QR code
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 0), 3)

            # Decode data and display it
            qr_data = obj.data.decode("utf-8")
            print("QR Code data:", qr_data)
            cv2.putText(frame, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
            # Play sound when QR code is detected
            play_scan_sound()

        # Show the frame
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting QR Code scanner...")
    scan_qr_code()
