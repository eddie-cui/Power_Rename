# Power_Rename
This script is designed to standardize image filenames by renaming them into sequential order, making it ideal for scenarios where photo numbers are inconsistent or missing, ensuring a clean and orderly dataset for processing or analysis.

# Image Renaming Tool

This Python script renames `.png` image files in a specified folder to a sequential numeric format (e.g., `0000.png`, `0001.png`, etc.). It ensures a clean and standardized naming convention, especially useful for scenarios like fixing inconsistent or missing photo numbers, preparing datasets for machine learning, or organizing large collections of images.

---

## Features

- Automatically renames `.png` files in a folder to a sequential, zero-padded numeric format.
- Handles missing or inconsistent numbering by reordering files in a proper sequence.
- Logs renamed and skipped files for user reference.

---

## Real-World Use Case

### Scenario: Handling Missing Numbers in Photo Names

Suppose you have a folder of images with filenames that are inconsistent or have gaps in their numbering, such as:

```
images/
├── 0000.png
├── 0002.png
├── 0005.png
```

This script will rename them to ensure proper sequential numbering:

```
images/
├── 0000.png
├── 0001.png
├── 0002.png
```

This is particularly useful when working with machine learning models or image processing pipelines where proper sequential ordering is crucial.

---

## Requirements

- Python 3.6 or higher

---

## Installation

No additional dependencies are required. Just ensure Python is installed on your system.

---

## Usage

### Running the Script

```bash
python rename.py <folder_path>
```

### Arguments

- `<folder_path>`: Path to the folder containing `.png` files to be renamed.

### Example

```bash
python rename.py ./images
```

---

## How It Works

1. **File Sorting**:
   - The script lists all `.png` files in the target folder and sorts them alphabetically.

2. **Renaming**:
   - Files are renamed sequentially (e.g., `0000.png`, `0001.png`), ensuring gaps in numbering are eliminated.

3. **Skipping Unnecessary Renames**:
   - Files already correctly named (e.g., `0000.png`) are skipped to save processing time.

4. **Logging**:
   - The script logs renamed and skipped files in the terminal for user transparency.

---

## File Structure Example

### Before Running the Script:

```
images/
├── img1.png
├── img5.png
├── img2.png
```

### After Running the Script:

```
images/
├── 0000.png
├── 0001.png
├── 0002.png
```

---

## Customization

1. **Change File Extension**:
   - Modify the script to handle other file types (e.g., `.jpg` or `.bmp`) by updating the file filter in the code.

2. **Adjust Naming Format**:
   - Update the naming convention (e.g., `image_0000.png`) by editing the format string in the script: 
     ```python
     new_name = f"image_{count:04d}.png"
     ```

---

## Troubleshooting

- **No Files Renamed**: Ensure the folder contains `.png` files and the path is correct.
- **Permission Denied**: Use appropriate permissions when running the script (e.g., `sudo` on Unix-based systems).

---

## Contributions

Feel free to contribute by submitting issues or pull requests to improve this tool or add new features.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

- [eddie.cui](https://github.com/eddie-cui)

--- 

Let me know if further adjustments are needed!
