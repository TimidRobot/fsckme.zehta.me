#!/usr/bin/env python3
# Standard library
import os.path

# Third-party
import jinja2


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath="./"),
    autoescape=jinja2.select_autoescape(["html", "xml"]),
)
template = env.get_template("redirects/template.html")
assets = "source/assets"
with open("redirects/mapping.txt") as mapping_pointer:
    for line in mapping_pointer.readlines():
        source, target = line.split()
        source = source.lstrip("/")
        html_file = os.path.join(assets, source)
        header = "{}/{}".format("http://127.0.0.1:5000", source)
        print("#" * len(header))
        print(header)
        print("#" * len(header))
        print("   target:", target)
        print("html_file:", html_file)
        contents = template.render(TARGET=target)
        file_dir = os.path.dirname(html_file)
        os.makedirs(file_dir, exist_ok=True)
        with open(html_file, "w+") as html_file_pointer:
            html_file_pointer.write(contents)
        print()
