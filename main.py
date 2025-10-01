#!/usr/bin/env python3 
file_path = "books/frankenstein.txt"

def main():



    def get_book_text(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    book_text = get_book_text(file_path)
    
    from stats import get_num_words
    
    print(f"Found {get_num_words(book_text)} total words")  
main()