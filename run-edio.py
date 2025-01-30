import os
from pydub import AudioSegment

# Function to calculate dB change from percentage
def percentage_to_db(percentage):
    # Convert percentage to dB: 
    # 100% = +6 dB (doubling the volume), 50% = +3 dB, -50% = -3 dB, etc.
    return 6 * (percentage / 100)

# Function to increase or decrease the volume of a single audio file
def adjust_volume(input_file, percentage):
    try:
        # Load the audio file
        audio = AudioSegment.from_file(input_file)
        
        # Calculate dB change from the percentage
        db_change = percentage_to_db(percentage)
        
        # Apply the volume change (increase or decrease)
        adjusted_audio = audio + db_change
        
        # Save the modified audio back to the same file
        adjusted_audio.export(input_file, format="mp3")  # Change format if needed
        print(f"Volume adjusted for {input_file} by {db_change} dB (Percentage: {percentage}%)")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Function to process all audio files in the specified folder
def adjust_volume_in_folder(folder_path, percentage):
    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Process only audio files (you can add more formats if needed)
        if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".ogg"):
            adjust_volume(file_path, percentage)

# Example usage
folder_path = input("Enter Path to Folder:- ").strip()  # Replace with your folder path
percentage_input = input("Enter percentage to increase/decrease volume (e.g., 100 for increase, -50 for decrease):- ").strip()

# Try to convert percentage_input to a float
try:
    percentage = float(percentage_input)
except ValueError:
    print("Invalid input for percentage. Please enter a valid number.")
else:
    adjust_volume_in_folder(folder_path, percentage)
