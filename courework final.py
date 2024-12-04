# Step 1: Define the function to hide the message
def get_user_input():
    """Get user input for a secret message."""
    message = input("Enter your secret message: ")
    return message
 
def save_message_to_file(message, filename="secret_message.txt"):
    """Save the secret message to a text file."""
    with open(filename, 'w') as file:
        file.write(message)
def hide_message_in_bmp(image_path, message, output_path):
    # Step 2: Open the BMP file in binary read mode
    with open(image_path, "rb") as bmp_file:
        bmp_data = bytearray(bmp_file.read())  # Read the entire BMP file into a bytearray
    
    # Step 3: Prepare the message for hiding
    message += '\0'  # Append a null character to signify the end of the message
    message_bytes = message.encode('utf-8')  # Convert the message to bytes
    
    # Step 4: Check if there is enough space in the BMP data
    if len(message_bytes) > len(bmp_data) - 54:  # 54 bytes for BMP header
        raise ValueError("Message is too long to hide in this image.")

    # Step 5: Hide the message in the least significant bits of the pixel data
    for i in range(len(message_bytes)):
        bmp_data[54 + i] = (bmp_data[54 + i] & ~1) | (message_bytes[i] & 1)
        
    # Step 6: Write the modified data back to a new BMP file
    with open(output_path, "wb") as output_file:
        output_file.write(bmp_data)  # Save the modified BMP file

# Step 1: Import necessary module
import os

# Step 2: Change the working directory to D:\
os.chdir('D:\\')  # Change this to your specific directory if needed

# Step 3: Verify current working directory
print("Current Working Directory:", os.getcwd())

# Step 4: Define file paths
input_image_path = r"D:\test_image.bmp"  # Path to the input BMP image
output_image_path = r"D:\test_image_step1.bmp"  # Path to save the new BMP image with hidden message

# Step 5: Check if input image exists
if not os.path.exists(input_image_path):
    print(f"Error: The file {input_image_path} does not exist.")
else:
    print(f"Input image found at: {input_image_path}")

# Step 7: Main execution
if __name__ == "__main__":
    secret_message = input("Enter your secret message to hide in the image: ")  # User input for secret message
    
    output_image_path = r"D:\test_image_step1.bmp"  # Path to save the new BMP image with hidden message

    try:
        hide_message_in_bmp(input_image_path, secret_message[:200], output_image_path)  # Hide and save
        print(f"Message hidden successfully in {output_image_path}.")
    except ValueError as e:
        print(e)

