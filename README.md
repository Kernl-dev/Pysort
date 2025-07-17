# Pysort
An easy way to organize your files.

###### ***Access [[Changelog]] here***

# Code Idea in Python
## Python Auto File Organizer
The idea consists in a python script that auto organizes a folder full of downloads. i.e. If you have a folder full of files of all sorts without a proper organization, just run the script, specify the directory and it should organize files automatically. 

## Expected usage/Output
Imagine the following directory:
```
Downloads/ file.ext file.ext2 file.ext3
```
After running the script and specifying the folder (in this example downloads) it should create a folder for each extension and place them into those folders. So now, the output should be:

```
Downloads/ext ext2 ext3
```
Inside of each containing their files.

***Later Documentation will be added later***

## Implementation Ideas (By ChatGPT)

- **Clarify edge cases and behavior:**

  - What happens if the folder already contains folders with the extension names?
	  - Handled. If a folder already exists, it'll use it

  - How should the script handle files with no extension?
	  - It'll create a folder containing all those files

  - What if files have uppercase or mixed-case extensions? (e.g., `.JPG` vs `.jpg`)
	  - It's not case sensitive, so as long as the extension is on the list, it'll work

  - Should symbolic links or hidden files be processed or ignored?

- **Error handling:**

  - What if the folder path is invalid or inaccessible?

  - What if a file cannot be moved (permissions issue)?

- **Extension grouping:**

  - Consider grouping similar file types (e.g., `.jpg`, `.png` → `images`) as a future enhancement.
	  - Done!

- **Performance and logging:**

  - Will it print what it moves or create a log file?

  - How will it handle very large folders?
