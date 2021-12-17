#!/usr/bin/env python3
# Standard library
import os.path
import sys
import traceback

# Third-party
import colorama
import jinja2


class ScriptError(Exception):
    def __init__(self, message, code=None):
        self.code = code if code else 1
        message = "({}) {}".format(self.code, message)
        super(ScriptError, self).__init__(message)


def print_pair(key, value, pad):
    style_key = f"{colorama.Style.BRIGHT}{colorama.Fore.GREEN}"
    style_sep = f"{colorama.Fore.GREEN}"
    style_reset = colorama.Style.RESET_ALL
    pad = " " * (pad - len(key))
    key = f"{style_key}{key}{style_reset}{style_sep}:{style_reset}"
    print(f"{pad}{key} {value}")


def main():
    colorama.init(autoreset=True)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="./"),
        autoescape=jinja2.select_autoescape(["html", "xml"]),
    )
    template = env.get_template("redirects/template.html")
    assets = "source/assets"
    style_count = f"{colorama.Back.MAGENTA}{colorama.Fore.BLACK}"
    style_file = (
        f"{colorama.Back.MAGENTA}{colorama.Style.BRIGHT}{colorama.Fore.WHITE}"
    )
    style_link = f"{colorama.Style.BRIGHT}{colorama.Fore.BLUE}"
    print()
    i = 1
    with open("redirects/mapping.txt") as mapping_pointer:
        for line in mapping_pointer.readlines():
            if line.startswith("#"):
                continue
            source, target = line.split()
            html_file = os.path.join(assets, source.lstrip("/"))
            print(f"{style_count}{i:>02}. {style_file}{html_file}")
            print_pair("source", source, 15)
            print_pair("target", target, 15)
            print_pair("test link", "", 15)
            print(f"{style_link}http://127.0.0.1:5000{source}")
            contents = template.render(TARGET=target)
            file_dir = os.path.dirname(html_file)
            os.makedirs(file_dir, exist_ok=True)
            with open(html_file, "w+") as html_file_pointer:
                html_file_pointer.write(contents)
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
