### **How to Convert any Python File to .EXE**
#### by Tim Ruscica of Tech With Tim

[Youtube Video Link][Tech With Tim]

---


<br  />

**Virtual Environment Setup**
1. Create a virtual environment:
    ```powershell
    py -m venv venv <# Syntax is py -m venv <Path\FolderNameOfVirtualEnvironment> #>
    ```
1. Run the batch file:
    ```powershell
    venv\Scripts\activate.bat
    ```
1. Open the Command Palette
1. Select the Python: Select Interpreter command
1. Select the python.exe under your workspace venv folder
1. Close the powershell terminal
1. Open a new powershell terminal to run your powershell commands in the virtual environment
1. (Optional) Upgrade pip:
    ```powershell
    py -m pip install --upgrade pip
    ```


<br  />

**Github Setup**
1. Create a new repository in [Github](https://github.com)
1. Create a .gitignore file in the project directory
1. In the .gitignore file, add the line:
    ```
    venv/
    ```
1. Initialize github with your repository default branch:
    ```powershell
    git init -b main
    <# Syntax: git init -b <branch name> #>
    ```
1. Stage README.md file for commit:
    ```powershell
    git add README.md
    ```
1. Commit README.md file:
    ```powershell
    git commit -m "Added README.md file"
    ```
1. Stage .gitignore file for commit:
    ```powershell
    git add .gitignore
    ```
1. Commit .gitignore file:
    ```powershell
    git commit -m "Added .gitignore file"
    ```
1. Add remote repository:
    ```powershell
    git remote add origin git@github.com:lorenzmiranda05/YoutubeVideoDownloader.git
    <# Syntax: git remote add origin <SSH Remote URL of your GitHub Repository> #>
    ```
1. Update remote repository with an upstream (tracking) reference:
    ```powershell
    git push -u origin main
    <# Syntax git push -u <remote> <branch>>
    ```


<br  />

**Package Setup**
1. Install Pytube:
    ```powershell
    pip install pytube
    ```
1. Install Pyinstaller:
    ```powershell
    pip install pyinstaller
    ```
1. Check installed packages:
    ```powershell
    pip list
    ```
    Output:
    ```powershell    
    Package                   Version
   ------------------------- ---------
    altgraph                  0.17.2
    future                    0.18.2
    pefile                    2022.5.30
    pip                       22.2.2
    pyinstaller               5.3
    pyinstaller-hooks-contrib 2022.9
    pytube                    12.1.0
    pywin32-ctypes            0.2.0
    setuptools                58.1.0
    ```


<br  />

**Compile to .exe file**
1. Compile main.py into one executable file that does not show the console during run-time:
    ```powershell
    pyinstaller --onefile -windowed --icon="d:\DEV\YoutubeVideoDownloader\Assets\Images\Youtube\icons8-youtube-60.ico" --name="YouTube Video Downloader" --version-file=FILE main.py
    <# Syntax: pyinstaller --onefile -windowed --icon=<.ico file path> --name=<.exe file name> --version-file=<file containing application metadata> <scriptName.py> #>
    ```
1. In the directory containing main.py file, delete the following:
    * build/ folder
    * YouTube Video Downloader.spec file
1. Move the dist/YouTube Video Downloader.exe file into the directory containing main.py file
1. Delete the dist/ folder


<br  />

**Generate an installer**
1. Download the NSIS: Nullsoft Scriptable Install System installer from [NSIS SourceForge][NSIS]
1. Install the NSIS: Nullsoft Scriptable Install System applicaton
1. Create a copy of the d:\DEV\YoutubeVideoDownloader folder
1. In the copy, delete the following:
    * .git folder
    * .gitignore file
1. Compress the d:\DEV\YoutubeVideoDownloader folder into a .zip file
1. Open the NSIS app
1. Click Installer based on .ZIP file
    <br  />
    <br  />
    ![github](https://raw.githubusercontent.com/lorenzmiranda05/YoutubeVideoDownloader/main/Assets/Images/NSIS/01%20NSIS%20Menu.png)
1. Click Open... and select the YoutubeVideoDownloader.zip file to load the files
    <br  />
    <br  />
    ![github](https://raw.githubusercontent.com/lorenzmiranda05/YoutubeVideoDownloader/main/Assets/Images/NSIS/02%20Zip2Exe%200.38.png)
1. Set the Installer name as YoutubeVideoDownloaderInstaller
1. Set the Output EXE File as YoutubeVideoDownloaderInstaller.exe
    <br  />
    <br  />
    ![github](https://raw.githubusercontent.com/lorenzmiranda05/YoutubeVideoDownloader/main/Assets/Images/NSIS/03%20Zip2Exe%200.38.png)
1. Click Generate
1. Click Close
    <br  />
    <br  />
    ![github](https://raw.githubusercontent.com/lorenzmiranda05/YoutubeVideoDownloader/main/Assets/Images/NSIS/04%20Zip2Exe%200.38.png)
1. Close NSIS

<br  />

**Tasks**
* [x] Create a Youtube Downloader tkinter application
* [x] Compile a tkinter application into a .exe file
* [x] Generate an installer for the tkinter .exe application
* [x] Add checkbutton to include subtitle files in the download
* [x] Format downloaded subtitle files in SubRip (.srt)
* [x] Recompile a tkinter application into a .exe file
* [x] Regenerate an installer for the tkinter .exe application

<br  />

**Image Sources**
*  Youtube icon by [Icons8][Icons8]
    <br  />
    [![github](https://img.icons8.com/doodle/48/youtube-play--v2.png)][Youtube]
* Converted to .ico using [FreeConvert][FreeConvert]


<!-- Reusable and Invisible URL Definitions  -->
[Github]: https://github.com
[Youtube]: https://icons8.com/icon/szxM3fi4e37N/youtube
[Icons8]: https://icons8.com
[FreeConvert]: https://www.freeconvert.com/png-to-ico
[Tech With Tim]: https://www.youtube.com/watch?v=UZX5kH72Yx4
[NSIS]: https://nsis.sourceforge.io/Download
[Download Subtitles From Youtube in Python]: https://www.youtube.com/watch?v=EG8cvSJFCc0