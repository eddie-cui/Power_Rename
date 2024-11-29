import os

def rename_images(folder_path):
    files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    count = 0

    for file in files:
        new_name = f"{count:04d}.png"

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        if file != new_name:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        else:
            print(f"Skipped: {file} (already in correct order)")

        count += 1

folder_path = "path/to/your/folder"
rename_images(folder_path)
