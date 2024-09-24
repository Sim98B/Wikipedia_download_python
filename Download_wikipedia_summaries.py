#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
import sys
import os

def install_requirements():
    try:
        if os.path.exists('requirements.txt'):
            print("Installing packages from requirements.txt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        else:
            print("File 'requirements.txt' non trovato!")
    except Exception as e:
        print(f"Error during import packaging: {e}")

install_requirements()

import os
import wikipedia
from tqdm.auto import tqdm
import time

def get_wiki_pages(total_pages: int = 1, id_text_path: str = 'wiki_ita.txt', page_list_path: str = 'page_list.txt', language: str = 'it'):
    wikipedia.set_lang(language)

    if os.path.exists(id_text_path) and os.path.exists(page_list_path):
        print(f'Text file found -> {id_text_path}\nPage list file found -> {page_list_path}\nUpdating...')
        
        with open(page_list_path, 'r', encoding = 'utf-8') as f:
            page_list = [line.strip() for line in f.readlines()]
            
        initial_length = len(page_list)
        target_length = len(page_list) + total_pages
            
        with tqdm(total = target_length, initial = initial_length, desc = 'Getting pages') as pbar:
            while len(page_list) < target_length:
                try:
                    title = wikipedia.page(wikipedia.random()).title
                    if title not in page_list:
                        page_list.append(title)
                        pbar.update(1)
                    else:
                        None
                except Exception as e:
                    print(f"!!! Can't get {title}, {e}")
                time.sleep(1)
                
        children_pages = []
        for name in tqdm(page_list[-total_pages:], desc = 'Getting children pages'):
            links = wikipedia.page(name).links
            for link in links:
                children_pages.append(link)
        
        page_list = sorted(list(set(page_list + children_pages)))
        
        with open(id_text_path, 'w', encoding = "utf-8") as file:
            for page in tqdm(page_list, desc = 'Downloading text'):
                try:
                    text = wikipedia.page(page).summary
                    file.write(page + '\n\n')
                    file.write(text + '\n\n')
                except Exception as e:
                    print(f"!!! No summary in {page}, {e}")
                    page_list.remove(page)
                time.sleep(1)
                
        with open(id_text_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        cleaned_content = '\n\n'.join([line.strip() for line in content.split('\n\n') if line.strip()])
        
        with open(id_text_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        print(f"File {id_text_path} cleaned.")
                
        with open(page_list_path, 'w', encoding='utf-8') as f:
            for page in page_list:
                f.write(page + '\n')
            
    else:
        print(f"Creating new pages' file -> {id_text_path}\nCreating new page list file -> {page_list_path}")
        
        parent_page_list = []
        with tqdm(total = total_pages, desc = 'Getting pages') as pbar:
            while len(parent_page_list) < total_pages:
                try:
                    title = wikipedia.page(wikipedia.random()).title
                    parent_page_list.append(title)
                    pbar.update(1)
                except Exception as e:
                    print(f"!!! Can't get {title}, {e}")
                time.sleep(1)
        
        children_pages = []
        for name in tqdm(parent_page_list, desc = 'Getting children pages'):
            links = wikipedia.page(name).links
            for link in links:
                children_pages.append(link)
                
        page_list = sorted(list(set(parent_page_list + children_pages)))
        
        with open(id_text_path, 'w', encoding = "utf-8") as file:
            for page in tqdm(page_list, desc = 'Downloading text'):
                try:
                    text = wikipedia.page(page).summary
                    file.write(page + '\n\n')
                    file.write(text + '\n\n')
                except Exception as e:
                    print(f"!!! No summary in {page}, {e}")
                    page_list.remove(page)
                time.sleep(1)
                
        with open(id_text_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        cleaned_content = '\n\n'.join([line.strip() for line in content.split('\n\n') if line.strip()])
        
        with open(id_text_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        print(f"File {id_text_path} cleaned.")
                
        with open(page_list_path, 'w', encoding='utf-8') as f:
            for page in page_list:
                f.write(page + '\n')
                    
if __name__ == "__main__":
    get_wiki_pages()

