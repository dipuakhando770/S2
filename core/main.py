import sys
from core.generator import IDGenerator

def run():
    print("--- Gemini Student Verifier Setup ---")
    name = input("Enter Student Name: ")
    school = input("Enter University Name: ")
    
    print(f"[*] Generating realistic ID for {name}...")
    id_card = IDGenerator.create_id(name, school)
    
    save_path = "output_id.jpg"
    id_card.save(save_path, "JPEG", quality=90)
    print(f"[+] Success! ID saved to {save_path}")
    print("[!] Now upload this file to the SheerID link in your browser.")

if __name__ == "__main__":
    run()
