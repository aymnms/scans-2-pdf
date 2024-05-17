<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">scans-2-pdf</h3>

  <p align="center">
    Program to merge manga scans into 1 pdf per chapter
    <br />
    <br />
    <a href="https://github.com/aymnms/scans-2-pdf/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/aymnms/scans-2-pdf/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After downloading manga scans, to read them more easily, this project generates a pdf file per chapiter from all scans of the downloaded manga.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

#### macOS
1. Install Homebrew :
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install Python :

```bash
brew install python
```

3. Check installation :

```bash
python3 --version
pip3 --version
```

#### Windows

1. Download python installer from python.org.
2. Execute the installer and tick the box "Add Python to PATH".
3. Check installation :
```bash
python --version
pip --version
```

#### Linux

1. Install Python:
- Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
- Fedora:
```bash
sudo dnf install python3 python3-pip
```
- Arch Linux:
```bash
sudo pacman -S python python-pip
```

2. Check installation:
```bash
python3 --version
pip3 --version
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/votre-utilisateur/votre-repository.git
cd votre-repository
```

2. Create and active a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # Sur Windows: env\Scripts\activate
```

1. Install dependencies:
```bash
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Open the main.py file
2. Modify the `manga_folder` variable by the path where your scans are downloaded
3. Execute the command:
```bash
python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aymnms/scans-2-pdf.svg?style=for-the-badge
[contributors-url]: https://github.com/aymnms/scans-2-pdf/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aymnms/scans-2-pdf.svg?style=for-the-badge
[forks-url]: https://github.com/aymnms/scans-2-pdf/network/members
[stars-shield]: https://img.shields.io/github/stars/aymnms/scans-2-pdf.svg?style=for-the-badge
[stars-url]: https://github.com/aymnms/scans-2-pdf/stargazers
[issues-shield]: https://img.shields.io/github/issues/aymnms/scans-2-pdf.svg?style=for-the-badge
[issues-url]: https://github.com/aymnms/scans-2-pdf/issues
[license-shield]: https://img.shields.io/github/license/aymnms/scans-2-pdf.svg?style=for-the-badge
[license-url]: https://github.com/aymnms/scans-2-pdf/blob/master/LICENSE.txt