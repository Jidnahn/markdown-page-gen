from textnode import *
import os
import shutil
from markdown_blocks import (
    extract_title, 
    markdown_to_html_node
)

def main():
    copy_to_public()
    from_path = "./content"
    template_path = "./content/template.html"
    dest_path = "./public"
    generate_pages_recursevely(from_path, template_path, dest_path)


def copy_to_public():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    path = "./static"
    target = "./public"
    copy_from_dir(path, target)

def copy_from_dir(path, target_path):
    content = os.listdir(path)
    for item in content:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, target_path)
        else: 
            new_path = os.path.join(path, item)
            new_target_path = os.path.join(target_path, item)
            os.mkdir(new_target_path)
            copy_from_dir(new_path, new_target_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, encoding="utf-8") as f:
        content = f.read()
        title = extract_title(content)
        html = markdown_to_html_node(content).to_html()
        
        with open(template_path, encoding="utf-8") as t:
            template = t.read()
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)
            
            with open(dest_path, "w") as h:
                h.write(template)
                h.close()    
            t.close()
        f.close()
        
def generate_pages_recursevely(from_path, template_path, dest_path):
    dir = os.listdir(from_path)
    for item in dir:
        item_path = os.path.join(from_path, item)
        item_dest_path = os.path.join(dest_path, item)
        if os.path.isfile(item_path):
            if os.path.splitext(item_path)[1] != ".md": continue
            item_dest_path = os.path.splitext(item_dest_path)[0] + ".html"
            generate_page(item_path, template_path, item_dest_path)
        else:
            os.mkdir(item_dest_path)
            generate_pages_recursevely(item_path, template_path, item_dest_path)
            

if __name__ == "__main__":
    main()
