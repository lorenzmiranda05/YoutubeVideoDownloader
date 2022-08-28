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
1. Install Pillow:
    ```powershell
    pip install pytube
    ```
1. Check installed packages:
    ```powershell
    pip list
    ```
    Output:
    ```powershell    
    Package    Version
    ---------- ---------
    pip        22.2.2
    pytube     12.1.0
    setuptools 58.1.0
    ```

<br  />

**Tasks**
* [ ] Create a Youtube Downloader tkinter application
* [ ] Compile a tkinter application into a .exe file
* [ ] Generate an installer for the tkinter .exe application

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