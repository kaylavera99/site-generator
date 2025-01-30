from textnode import TextNode, TextType
import os
import shutil
from generator import generate_page, extract_title, generate_pages_recursive, copy_static_to_public



    




def main():
    
   #copy_static_to_public("./static", "./public")


    generate_pages_recursive('./content', './template.html', './public')

if __name__ == "__main__":
    main()