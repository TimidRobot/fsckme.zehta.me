import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_strip_dir_date_prefix.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Timid Robot Zehta',
    author_email='timidrobot@zehta.me',
    description=description,
    keywords='Lektor plugin',
    license='Unlicense',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-strip-dir-date-prefix',
    packages=find_packages(),
    py_modules=['lektor_strip_dir_date_prefix'],
    # url='[link to your repository]',
    version='0.2',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'strip-dir-date-prefix = lektor_strip_dir_date_prefix:StripDirDatePrefixPlugin',
        ]
    }
)
