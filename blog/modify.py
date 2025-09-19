from bs4 import BeautifulSoup
import sys

def modify_html(input_html):
    """Modify the input HTML (obtained from htlatex) and return the modified HTML."""

    # Parse the input HTML with BeautifulSoup
    soup = BeautifulSoup(input_html, 'html.parser')
    
    # Add the required meta and link tags to the head
    head = soup.head
    new_link = soup.new_tag("link", rel="stylesheet", type="text/css", href="../../../style/styles.css")
    head.append(new_link)
    new_meta_charset = soup.new_tag("meta", attrs={"charset": "UTF-8"})
    head.append(new_meta_charset)

    new_meta_viewport = soup.new_tag("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0, maximum-scale=1.0"})
    head.append(new_meta_viewport)

    # Add the required div tags to the beginning of the body
    body = soup.body

    # Create page-container div
    page_container = soup.new_tag("div", **{"class": "page-container"})
    menu_div = soup.new_tag("div", **{"class": "menu"})
    header = soup.new_tag("header")
    header_link = soup.new_tag("a", href="../../../index.html")
    header_link.string = "Aditya Kane"
    header.append(header_link)
    menu_div.append(header)

    # Create navigation
    nav = soup.new_tag("nav")
    ul = soup.new_tag("ul")

    # ABOUT link
    li1 = soup.new_tag("li")
    li1_a = soup.new_tag("a", href="../../../index.html", **{"class": "current"})
    li1_a.string = "ABOUT"
    li1.append(li1_a)
    ul.append(li1)

    # BLOG link
    li2 = soup.new_tag("li")
    li2_a = soup.new_tag("a", href="../../index.html")
    li2_a.string = "BLOG"
    li2.append(li2_a)
    ul.append(li2)

    # MISC link
    li3 = soup.new_tag("li")
    li3_a = soup.new_tag("a", href="../../../miscellany.html")
    li3_a.string = "MISC."
    li3.append(li3_a)
    ul.append(li3)

    nav.append(ul)
    menu_div.append(nav)
    page_container.append(menu_div)

    # Create page and blog-article divs
    page_div = soup.new_tag("div", **{"class": "page"})
    blog_article_div = soup.new_tag("div", **{"class": "blog-article"})

    # Move specific body contents inside blog-article div
    for tag in body.contents[1:]:  # Skip the first tag which is page_container
        blog_article_div.append(tag.extract())

    # Structure the divs accordingly
    page_div.append(blog_article_div)
    page_container.append(page_div)
    
    # Insert page_container at the beginning of the body
    body.insert(0, page_container)

    # Add closing div tags at the end of the body
    body.append(soup.new_tag("div"))
    body.append(soup.new_tag("div"))

    return str(soup)

# The rest of the script remains the same as your original code.
if __name__ == "__main__":    
    # Read the command line arguments
    input_file_path = input("Enter the path to the input HTML file:")
    output_file_path = input("Enter the path to the output HTML file:")


    # Read the input HTML content
    with open(input_file_path, "r", encoding="utf-8") as f:
        input_html = f.read()

    # Modify the input HTML
    modified_html = modify_html(input_html)

    # Write the modified HTML to the output file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(modified_html)

    print(f"Modified HTML has been written to '{output_file_path}'")
