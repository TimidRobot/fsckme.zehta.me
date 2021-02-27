# Standard library
import ast
import io
import re

# Third-party
from setuptools import find_packages, setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r"description\s+=\s+(?P<description>.*)")

with open("lektor_custom_filters.py", "rb") as f:
    description = str(
        ast.literal_eval(
            _description_re.search(f.read().decode("utf-8")).group(1)
        )
    )

setup(
    author="Timid Robot Zehta",
    author_email="timidrobot@zehta.me",
    description=description,
    keywords="Lektor plugin",
    license="Unlicense",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="lektor-custom-filters",
    packages=find_packages(),
    py_modules=["lektor_custom_filters"],
    # url='[link to your repository]',
    version="0.1",
    classifiers=[
        "Environment :: Plugins",
        "Framework :: Lektor",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "lektor.plugins": [
            "custom-filters = lektor_custom_filters:CustomFiltersPlugin",
        ]
    },
)
