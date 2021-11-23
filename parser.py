from marko.ext.gfm import gfm
from bs4 import BeautifulSoup
import sys


def parse_apps_list(heading):
    """
    Verifies that apps list is in following format:
    <h2>Catalog</h2>
    <h3>{category name}</h3>
    <p>{category description}</p>
    <ul>
    <li><a href="{app link}">{app name}</a>{app description}</li>
    ...
    </ul>
    ...
    :param heading: Heading beginning the list
    :return: True if structure is valid, else False
    """
    if not heading:
        return False

    curr_elem = heading.find_next_sibling()
    prev_elem_name = 'ul'

    while curr_elem.name != 'h2':
        if curr_elem.name == 'h3':
            if prev_elem_name != 'ul' or not curr_elem.text:
                return False
        elif curr_elem.name == 'p':
            if (prev_elem_name != 'h3' and curr_elem.name != 'p') or not curr_elem.text:
                return False
        elif curr_elem.name == 'ul':
            if prev_elem_name != 'p' or not parse_apps_list_per_category(curr_elem):
                return False
        else:
            return False

        prev_elem_name = curr_elem.name
        curr_elem = curr_elem.find_next_sibling()

    if prev_elem_name != 'ul':
        return False

    return True


def parse_apps_list_per_category(ul_elem):
    """
    Verifies that apps list for a category is in following format:
    <ul>
    <li><a href="{app link}">{app name}</a>{app description}</li>
    ...
    </ul>
    :param ul_elem: list of apps in a category
    :return: True if structure is valid, else False
    """
    for child in ul_elem.childGenerator():
        if child.name:
            next_elem = child.find_next()
            if next_elem.name != 'a':
                return False
            app_name = next_elem.text
            if not app_name:
                return False
            app_description = child.text.replace(app_name, '').replace(' ','')
            if not app_description:
                return False
    return True

example_format = """
    ## Catalog
    ### Category name - 1
    _Category description_
    - [contribution-1-name](contribution-1-link) - contribution-1 description
    - [contribution-2-name](contribution-2-link) - contribution-2 description
    ### Category name - 2
    _Category description_
    - [contribution-1-name](contribution-1-link) - contribution-1 description
    - [contribution-2-name](contribution-2-link) - contribution-2 description
    """
if __name__ == "__main__":
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.read()

    html = gfm(read_me)
    soup = BeautifulSoup(html, 'html.parser')
    gg_catalog_heading = soup.find('h2', string='Catalog')

    if not parse_apps_list(gg_catalog_heading):
        sys.exit('README Structure is invalid. Please update the README to match the following format.\n{}'.format(example_format))
