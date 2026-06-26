import json
import copy
import config

config.load_page(config.current_page)

def create_page():
    with open(f"pages/template.json", "r", encoding="utf-8") as f:
        EMPTY_PAGE = json.load(f)
    page = copy.deepcopy(EMPTY_PAGE)

    page_number = config.total_pages + 1

    with open(f"pages/page{page_number}.json", "w", encoding="utf-8") as f:
        json.dump(page, f, indent=4)

def save_page(page):
    with open(f"pages/page{page}.json", "w", encoding="utf-8") as f:
        json.dump(config.keys, f, indent=4)



def edit_key(scan_code, name, type, shortcut):
    config.keys[str(scan_code)] = {
        "name": name,
        "type": type,
        "shortcut": shortcut
    }

    save_page(config.current_page)

edit_key(55,"Test","url","https://www.music.youtube.com")
