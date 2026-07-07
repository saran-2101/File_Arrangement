# File Organizer - Copy & Organize

A simple yet efficient Python script that automatically organizes files from a source directory into subdirectories based on their file extensions.

## 📋 Overview

This script scans a specified source folder, identifies files by their extension (e.g., .jpg, .pdf, .txt), and automatically moves them into organized folders named after their file types (e.g., `jpgFile`, `pdfFile`, `txtFile`). Perfect for organizing downloads, media libraries, or any cluttered directory!

## ✨ Features

- ✅ Automatic file organization by extension
- ✅ Creates extension-based folders automatically
- ✅ Moves files without overwriting (uses shutil.move)
- ✅ Detailed console output for tracking progress
- ✅ Error handling with meaningful error messages
- ✅ Skips directories, processes only files
- ✅ Handles files without extensions
- ✅ Progress counter showing files moved and folders created

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies (uses only built-in libraries)


## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

2. No additional packages to install! The script uses Python's standard library.

## 🚀 Usage

### Basic Setup

1. Open `file_organizer.py` in a text editor
2. Modify the source and destination paths according to your needs:

```python
source = r"C:\Users\location"  # Where your files are
destination = r"C:\Users\location"  # Where to organize them
```

### Running the Script

**On Windows:**
```bash
python file_organizer.py
```

**On macOS/Linux:**
```bash
python3 file_organizer.py
```

### Example Output

```
============================================================
FILE ORGANIZER - Starting Process
============================================================

✓ Source Directory: C:\Users\saran\Music\Test_Folder
✓ Destination Directory: C:\Users\saran\OneDrive\Pictures

------------------------------------------------------------

📄 Processing: photo.jpg
   └─ Extension: jpg
   └─ Destination folder: JPGFile
   └─ Current working directory: C:\Users\saran\OneDrive\Pictures
   ✓ Created new folder: JPGFile
   ✓ Moved to: C:\Users\saran\OneDrive\Pictures\JPGFile\photo.jpg

📄 Processing: document.pdf
   └─ Extension: pdf
   └─ Destination folder: PDFFile
   └─ Current working directory: C:\Users\saran\OneDrive\Pictures
   ✓ Folder already exists: PDFFile
   ✓ Moved to: C:\Users\saran\OneDrive\Pictures\PDFFile\document.pdf

============================================================
TASK COMPLETED SUCCESSFULLY
============================================================
```

## 🔑 Key Differences: COPY vs MOVE

| Operation | Effect |
|-----------|--------|
| **COPY** (This Script) | Original files stay in source, copies appear in destination |
| **MOVE** | Original files moved from source to destination |

**This script uses `shutil.copy()` - your original files are safe!**


## ⚙️ Configuration

### Custom Paths

Edit these variables in the script to point to your directories:

```python
source = r"C:\path\to\your\source_folder"
destination = r"C:\path\to\your\destination_folder"
```

**Tips for paths:**
- Use raw strings (prefix with `r`) to avoid escape character issues
- Use backslashes `\` for Windows paths
- Use forward slashes `/` for macOS/Linux paths, or use `Path` from pathlib

## 🐛 Troubleshooting

### "Source directory not found"
- Check that the source path exists and is spelled correctly
- Verify you have read permissions for the source folder

### "Permission Error"
- Ensure you have write permissions to the destination folder
- Close any files that might be open in the destination
- Try running the script as Administrator (Windows)

### Files not moving
- Check if files are already in destination (they won't be moved again)
- Ensure both directories have sufficient disk space
- Verify file paths have no special characters causing issues

### Script freezes
- If dealing with large files, the script may take time
- If it freezes, press `Ctrl+C` to stop and check for locked files

## 📝 How It Works

1. **Scans** the source directory for files
2. **Extracts** the file extension from each file
3. **Creates** a folder named `{EXTENSION}File` (e.g., `jpgFile`, `pdfFile`)
4. **Moves** the file to the appropriate folder
5. **Reports** progress with detailed output
6. **Handles** errors gracefully with meaningful messages

## 💡 Example Use Cases

- Organizing download folders
- Sorting media libraries by file type
- Cleaning up mixed file directories
- Batch organizing project assets

## 🔒 Safety Features

- ✅ Checks if folders exist before creating
- ✅ Skips processing directories (only moves files)
- ✅ Provides detailed error messages
- ✅ Shows operation summary at the end

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add new features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Saran**
- GitHub: [@saran-2101](https://github.com/saran-2101)

## 🎯 Future Enhancements

Potential improvements for future versions:
- [ ] Config file support for easier path management
- [ ] Recursive folder processing
- [ ] Dry-run mode to preview operations
- [ ] Custom naming schemes for output folders
- [ ] GUI interface using tkinter
- [ ] Support for organizing by date modified or file size
- [ ] Undo functionality

## 📞 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Open an issue on GitHub
3. Review the detailed console output for error messages

---

**Made with ❤️ for better file organization**
