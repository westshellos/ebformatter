import os
from bs4 import BeautifulSoup

def links(company, input_content):
    # Links dictionary
    links_map = {"TSL" : "https://thesmartlocal.com/",
                 "Eatbook": "https://eatbook.sg/",
                 "MSN": "https://mustsharenews.com/",
                 "Zula" : "https://zula.sg/",
                 "Uchify" : "https://uchify.com/"}
    
    if company == '':
        raise Exception("No company selected")
    
    else:
        company_url = links_map[company]

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(input_content, 'html.parser')

        # Find all anchor tags in the HTML
        anchor_tags = soup.find_all('a')

        # Denotes company URL
        for anchor in anchor_tags:
            # Get the URL from the 'href' attribute of the anchor tag
            url = anchor.get('href', '')
            if url and not url.startswith(company_url):
                # Add target="_blank" to the anchor tag
                anchor['target'] = '_blank'

        # Get the processed HTML content
        processed_content = str(soup)

        return processed_content

def bold(input_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(input_content, 'html.parser')

    # Find all h3 headings in the HTML
    h3_headings = soup.find_all('h3')

    for h3 in h3_headings:
        # Wrap <b> tags around the h3 heading
        h3.wrap(soup.new_tag("b"))

    # Get the processed HTML content
    processed_content = str(soup)

    return processed_content

def hr3(input_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(input_content, 'html.parser')

    # Find all h3 headings in the HTML
    h3_headings = soup.find_all('h3')

    for h3 in h3_headings:
        # Wrap <hr> tags around the h3 heading
        h3.insert_before(soup.new_tag("hr"))
        h3.insert_after(soup.new_tag("hr"))

    # Get the processed HTML content
    processed_content = str(soup)

    return processed_content

def hr2(input_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(input_content, 'html.parser')

    # Find all h3 headings in the HTML
    h2_headings = soup.find_all('h2')

    for h2 in h2_headings:
        # Wrap <hr> tags around the h2 heading
        h2.insert_before(soup.new_tag("hr"))
        h2.insert_after(soup.new_tag("hr"))

    # Get the processed HTML content
    processed_content = str(soup)

    return processed_content

def edit(company, file_path, arg1, arg2, arg3, arg4):
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply modifications in the specified order 
    if arg1:
        content = links(company, content) 
    if arg2:
        content = bold(content)
    if arg3:
        content = hr3(content)
    if arg4:
        content = hr2(content)

    # Create a new output file with the appropriate suffix based on the functions applied
    output_file = os.path.splitext(file_path)[0]
    if arg1:
        output_file += '_links'
    if arg2:
        output_file += '_bold'
    if arg3:
        output_file += '_hr3'
    if arg4:
        output_file += '_hr2'
    output_file += '.txt'


    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Modifications successfully applied! Output saved to {output_file}")
