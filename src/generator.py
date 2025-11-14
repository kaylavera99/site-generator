from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
from pathlib import Path
import os
import shutil


def copy_static_to_public(src, dest):
    if os.path.exists(src):
        print(f"Removing existing dir: {dest}")

    print(f"Creating new {dest} directory")
    all_files = os.listdir(src)

    for path in all_files:
        src_path = os.path.join(src, path)
        dest_path = os.path.join(dest, path)


        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            copy_static_to_public(src_path, dest_path)
            
        else: 
            print(f"Skipping unknown item: {src_path}")


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)    
        






def extract_title(markdown):
    split_mark = markdown.split('\n')
    title = ""

    for line in split_mark:
        # If it's an H1 with 1 # symbol
        if line.startswith("# "):
            title = line[2:].strip()
            #Return the title text
            return title
        else:
            raise ValueError("Not a valid heading")



def generate_page(from_path, template_path, dest_path):
    #Print message
    print(f"Generating page from {from_path} to {dest_path} using template.html")
    
    temp_file_content = ""
    from_file_content = ""

    # Reading template file and saving it to a str variable
    with open(template_path, "r") as file:
        temp_file_content = file.read()
    

    # Reading in the content from index.md and saving it 
    # to a str variable
    with open(from_path, 'r') as from_file:
        from_file_content = from_file.read()

        # Converting the content from the index.md markdown to HTML nodes
        html_file_content = markdown_to_html_node(from_file_content)
        #Extracting title from index.md markdown
        md_title = extract_title(from_file_content)

    # Parsing all of the, now, HTML nodes to an HTML string
    rendered = html_file_content.to_html()

    # Replacing the title
    replaced_title = temp_file_content.replace("{{ Title }}", md_title)
    #Replacing the content
    replaced_content = replaced_title.replace("{{ Content }}", rendered)

    # Name of the file we want to create
    #new_page_file = 'index.html'

    # Creating the new path. If it doesn't exist, make the path
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
        
    
    


    # Writing to our new index.html file
    with open(dest_path, 'w') as file:
        file.write(replaced_content)
        file.close()


# The content path, the template to use and the path where it does
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)



