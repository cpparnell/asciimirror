import cv2
import numpy as np

# ASCII characters for intensity mapping
# ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII_CHARS = "@%&#*+=-:. "

def frame_to_ascii(frame, cols=300, darkness_threshold=76):
    """
    Convert a frame to ASCII art with a darkness threshold.
    Args:
    - frame: Grayscale frame as a numpy array.
    - cols: Number of columns in the ASCII output.
    - darkness_threshold: Intensity below which pixels are turned into blank space.
    """
    # Resize frame
    height, width = frame.shape
    aspect_ratio = width / height
    new_width = cols
    new_height = int(new_width / aspect_ratio * 0.55)  # Adjust for character aspect ratio
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Map pixels to ASCII with threshold
    ascii_frame = [
        ASCII_CHARS[pixel // 25] if pixel > darkness_threshold else " "
        for pixel in resized_frame.flatten()
    ]

    # Return as multiline string
    ascii_art = "\n".join(
        "".join(ascii_frame[i : i + new_width])
        for i in range(0, len(ascii_frame), new_width)
    )
    return ascii_art

def main():
    # Open video stream
    cap = cv2.VideoCapture(0)  # 0 for default camera

    try:
        while True:
            # Read frame from video
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Convert frame to ASCII
            ascii_art = frame_to_ascii(gray_frame)

            # Clear console and print ASCII
            print("\033c", end="")  # Clear screen
            print(ascii_art)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        cap.release()

if __name__ == "__main__":
    main()