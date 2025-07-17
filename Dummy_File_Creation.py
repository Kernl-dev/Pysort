import os

file_categories = {
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp'],
    'Documents': ['pdf', 'doc', 'docx', 'txt', 'odt', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx', 'csv', 'epub'],
    'Compressed': ['zip', 'rar', '7z', 'tar', 'gz', 'tar.gz', 'bz2', 'xz', 'deb', 'tar.xz', 'tgz', 'iso'],
    'Executables': ['exe', 'msi', 'bat', 'apk', 'xapk'],
    'Audio': ['mp3', 'wav', 'aac', 'flac'],
    'Video': ['mp4', 'mkv', 'avi', 'mov'],
}

count = 5

os.makedirs("test_files", exist_ok=True)
os.chdir("test_files")

for category, extensions in file_categories.items():
    for ext in extensions:
        for i in range(1, count + 1):
            filename = f"sample_{category.lower()}_file_{i}.{ext}"
            with open(filename, "w") as f:
                f.write("")  # creates empty file

print(f"Created {count} dummy files per extension in {os.getcwd()}")
