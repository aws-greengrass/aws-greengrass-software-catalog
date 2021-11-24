import json

import requests


def validate_templates(file_path):
    with open(file_path, "r") as templates_file:
        templates = json.loads(templates_file.read())
        for name, url in templates.items():
            if not url_exists(url):
                exit(f"Template '{name}' does not exist at the URL - {url}")


def validate_repositories(file_path):
    with open(file_path, "r") as repositories_file:
        repositories = json.loads(repositories_file.read())
        for name, url in repositories.items():
            if not url_exists(url):
                exit(f"Repository '{name}' does not exist at the URL - {url}")


def url_exists(url):
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return True


if __name__ == "__main__":
    validate_templates("cli-components/templates.json")
    validate_repositories("cli-components/community-components.json")
