import os
from pathlib import Path
import shutil

# Step 1: Create a "bader" directory if it doesn't exist
bader_dir = Path("./bader")
bader_dir.mkdir(exist_ok=True)

# Step 2: Read the first 7 lines in the XDATCAR file
with open("XDATCAR", "r") as f:
    lines = [next(f) for _ in range(7)]
file_head = "".join(lines)
atom_number = sum(int(num) for num in lines[6].split())

# Function to process a single frame
def process_frame(frame_number):
    with open("XDATCAR", "r") as f:
        content = f.read()
    occurrences = content.split("=")
    try:
        frame_content = occurrences[frame_number].splitlines()[1:atom_number + 1]
    except IndexError:
        print(f"Frame {frame_number} is out of range.")
        return
    atomic_coordinates = "\n".join(frame_content)

    # Create a folder for the frame and write the POSCAR file
    frame_dir = bader_dir / str(frame_number)
    frame_dir.mkdir(exist_ok=True)
    with open(frame_dir / "POSCAR", "w") as f:
        f.write(file_head + "Direct\n" + atomic_coordinates + "\n")

    # Step 4: Copy files from /home/kdc2016/bd-anly and POTCAR to the frame folder
    src_dir = Path("/home/kdc2016/bd-anly")
    for item in src_dir.iterdir():
        if item.is_file():
            shutil.copy(item, frame_dir)
    shutil.copy("POTCAR", frame_dir)

# Step 3: Ask the user for frame numbers and process each
frame_numbers = input("Which frame to extract (starting from 0, separate with comma): ")
for frame_num in map(int, frame_numbers.split(",")):
    process_frame(frame_num + 1)

