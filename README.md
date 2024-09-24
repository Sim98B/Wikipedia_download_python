# Wikipedia Page Downloader

This repository contains a Python script that downloads summaries of random Wikipedia pages and stores them in a text file. The script is designed to scrape Wikipedia pages in a specified language (default: Italian) and save both the title and summary of the pages. Additionally, it allows the user to download a set number of random pages and fetch links to child pages, building a comprehensive corpus of Wikipedia content.

## Features
- Scrape random Wikipedia pages and their summaries.
- Fetch links from parent pages to download additional child pages.
- Automatically update existing page lists, avoiding duplicates.
- Save the list of downloaded pages for future use and incremental updates.
- Clean up downloaded content by removing unnecessary blank lines.
  
## Requirements
Before running the script, the required Python packages must be installed. This will be handled automatically if the script is run as described in the usage instructions.

The script uses the following libraries:
- `os`: To check for file existence and manipulate paths.
- `time`: To manage delays between requests.
- `tqdm`: To display progress bars for various operations.
- `wikipedia`: To interact with the Wikipedia API and fetch pages and summaries.

## Setup and Usage

### 1. Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/wiki-page-downloader.git
cd wiki-page-downloader
```

### 2. Install Requirements
You can install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```

### 3. Running the script
To run the script, open a terminal and navigate to the project directory. You can execute the script with the following command:
```bash
python get_wiki_pages.py
```

### 4. Modifying Parameters
You can modify how many random Wikipedia pages you want to download and set different paths for the output files. The script provides the following parameters:
- total_pages: Number of Wikipedia pages to download (default is 10).
- id_text_path: Path to save the downloaded page summaries (default is wiki_ita.txt).
- page_list_path: Path to store the list of downloaded page titles (default is page_list.txt).
- language

### 5. 	Output
- The script generates a wiki_ita.txt file containing the titles and summaries of the downloaded Wikipedia pages.
- A separate page_list.txt file is maintained, containing the titles of all downloaded pages to prevent re-downloading duplicates.

### 6. Cleaning the text file
The script will also clean up the text file by ensuring that only two newlines (\n\n) are used between entries. This helps maintain a clean, readable format for the downloaded content.
**Example Command**
```bash
python get_wiki_pages.py --total_pages 10 --id_text_path wiki_ita.txt --page_list_path page_list.txt
```

**License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
