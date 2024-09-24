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
