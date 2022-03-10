#!/usr/bin/env python3
# Standard library
import os.path
import sys
import traceback

# Third-party
import jinja2
from colorama import Back, Fore, Style, init


class ScriptError(Exception):
    def __init__(self, message, code=None):
        self.code = code if code else 1
        message = "({}) {}".format(self.code, message)
        super(ScriptError, self).__init__(message)


def print_pair(key, value):
    pad = " " * (19 - len(key))
    key = (
        f"{Style.BRIGHT}{Fore.GREEN}{key}{Style.RESET_ALL}"
        f"{Style.DIM}:{Style.RESET_ALL}"
    )
    print(f"{pad}{key} {value}")


def main():
    init(autoreset=True)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="./"),
        autoescape=jinja2.select_autoescape(["html", "xml"]),
    )
    template = env.get_template("redirects/template.html")
    assets = os.path.join("source", "assets")
    print()
    i = 1
    with open("redirects/mapping.txt") as mapping_pointer:
        for line in mapping_pointer.readlines():
            if line.startswith("#"):
                continue
            source, target = line.split()
            source_file = os.path.join(assets, source.lstrip("/"))
            if source_file.endswith("/"):
                source_file = f"{source_file}index.html"
            docs_file = os.path.join("docs", source.lstrip("/"))
            pad = " " * (79 - 8 - len(source_file))
            print(
                f"{Back.MAGENTA}{Fore.BLACK}{i:>02}.{'':>5}"
                f"{Back.MAGENTA}{Style.BRIGHT}{Fore.WHITE}{source_file}{pad}"
            )
            print(f"{'':>17}{Fore.MAGENTA}{docs_file}")
            print_pair("URL path source", source)
            print_pair("URL path target", target)
            print_pair("URL test link", "")
            print(f"{Style.BRIGHT}{Fore.BLUE}http://127.0.0.1:5000{source}")
            # Note that this writes a manually formatted HTML file to the
            # source directory. On build, it will be minified by Lektor.
            contents = template.render(TARGET=target)
            contents.strip()
            contents = f"{contents}\n"
            file_dir = os.path.dirname(source_file)
            os.makedirs(file_dir, exist_ok=True)
            with open(source_file, "w+") as source_file_pointer:
                source_file_pointer.write(contents)
            print()
            i += 1


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        sys.exit(e.code)
    except KeyboardInterrupt:
        print("INFO (130) Halted via KeyboardInterrupt.", file=sys.stderr)
        sys.exit(130)
    except ScriptError:
        error_type, error_value, error_traceback = sys.exc_info()
        print("ERROR {}".format(error_value), file=sys.stderr)
        sys.exit(error_value.code)
    except Exception:
        print("ERROR (1) Unhandled exception:", file=sys.stderr)
        print(traceback.print_exc(), file=sys.stderr)
        sys.exit(1)
