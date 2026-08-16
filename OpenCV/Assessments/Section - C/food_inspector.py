### Section C — Mini Capstone Project

## Mini Project: Food Delivery Image Quality Inspector

### Objective:
# Build a menu-driven console utility for a food delivery platform that accepts food images, runs a standardised inspection pipeline, and produces a quality report — combining image loading and validation, colour-channel analysis, transformation chaining (rotate, crop, flip), Gaussian filtering, and Canny edge-based texture assessment into a single working program.



### Your project must:
# The program must present a menu with at least four options: (1) Load & inspect image, (2) Resize and analyse colour channels, (3) Apply transformation pipeline, (4) Run edge-based quality scan, and (5) Exit — and loop back to the menu after each operation until the user selects Exit.
# Option 1 must load the image, print its height, width, and channel count, convert it to grayscale, display both versions, and save the grayscale copy as <original_name>_gray.jpg.
# Option 2 must resize the image to 256×256 using INTER_AREA, split into B/G/R channels, print each channel's average intensity, and display the three channel images in named windows.
# Option 3 must rotate the image by a user-entered angle (degrees), crop the central 60% region from the rotated image, and flip it horizontally — displaying all three intermediate results in labelled windows.
# Option 4 must apply Gaussian blur (5×5) followed by Canny edge detection, display the edge map, count the total edge pixels using cv2.countNonZero(), and print a quality verdict: 'High texture (good detail)' if edge pixels exceed 5 000, or 'Low texture (may need re-shoot)' otherwise.







import cv2
import numpy as np
import os

def load_and_inspect():
    filename = input("Enter image filename to load (e.g., sample_food.jpg): ")
    img = cv2.imread(filename)
    if img is None:
        print("Error: Could not read image.")
        return None, None
        
    h, w, c = img.shape
    print(f"Height: {h}, Width: {w}, Channels: {c}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray)
    
    name, ext = os.path.splitext(filename)
    save_name = f"{name}_gray.jpg"
    cv2.imwrite(save_name, gray)
    print(f"Saved grayscale copy as {save_name}")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img, filename

def resize_and_analyse(img):
    if img is None:
        print("Please load an image first (Option 1).")
        return
        
    resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    b, g, r = cv2.split(resized)
    
    print(f"Average Blue Intensity: {round(np.mean(b), 2)}")
    print(f"Average Green Intensity: {round(np.mean(g), 2)}")
    print(f"Average Red Intensity: {round(np.mean(r), 2)}")
    
    cv2.imshow('Resized Image', resized)
    cv2.imshow('Blue Channel', b)
    cv2.imshow('Green Channel', g)
    cv2.imshow('Red Channel', r)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform_pipeline(img):
    if img is None:
        print("Please load an image first (Option 1).")
        return
        
    try:
        angle = float(input("Enter rotation angle in degrees: "))
    except ValueError:
        print("Invalid angle. Using 0.")
        angle = 0.0
        
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    
    crop_h = int(h * 0.60)
    crop_w = int(w * 0.60)
    
    start_y = (h - crop_h) // 2
    start_x = (w - crop_w) // 2
    
    cropped = rotated[start_y:start_y+crop_h, start_x:start_x+crop_w]
    
    flipped = cv2.flip(cropped, 1)
    
    cv2.imshow('Rotated', rotated)
    cv2.imshow('Cropped (Central 60%)', cropped)
    cv2.imshow('Flipped Horizontally', flipped)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return flipped

def quality_scan(img):
    if img is None:
        print("Please load an image first (Option 1).")
        return
        
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    cv2.imshow('Edge Map', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    edge_pixels = cv2.countNonZero(edges)
    print(f"Total edge pixels: {edge_pixels}")
    
    if edge_pixels > 5000:
        print("Verdict: High texture (good detail)")
    else:
        print("Verdict: Low texture (may need re-shoot)")

def main():
    current_img = None
    transformed_img = None
    
    while True:
        print("\n--- Food Delivery Image Quality Inspector ---")
        print("1. Load & inspect image")
        print("2. Resize and analyse colour channels")
        print("3. Apply transformation pipeline")
        print("4. Run edge-based quality scan")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            current_img, _ = load_and_inspect()
            transformed_img = current_img.copy() if current_img is not None else None
        elif choice == '2':
            resize_and_analyse(current_img)
        elif choice == '3':
            transformed_img = transform_pipeline(current_img)
        elif choice == '4':
            scan_img = transformed_img if transformed_img is not None else current_img
            quality_scan(scan_img) 
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()