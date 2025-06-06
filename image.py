from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Simple encryption: Add 50 (wrap using % 256)
            pixels[i, j] = ((r + 50) % 256, (g + 50) % 256, (b + 50) % 256)

    img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Reverse the encryption by subtracting 50
            pixels[i, j] = ((r - 50) % 256, (g - 50) % 256, (b - 50) % 256)

    img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter choice (1 or 2): ").strip()

    input_path = input("Enter path to the image file: ")
    output_path = input("Enter path to save the new image: ")

    if choice == '1':
        encrypt_image(input_path, output_path)
    elif choice == '2':
        decrypt_image(input_path, output_path)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
