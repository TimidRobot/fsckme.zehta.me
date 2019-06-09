# zehta.me

Source for [zehta.me][site].

[site]: https://zehta.me/


## Overview

The source is located in [`site/`](site/).

The built content is located in [`docs/`](docs/).


## Development

1. Install [Pipenv][pipenv]
    ```shell
    brew install pipenv
    ```
2. Install [Lektor][lektor] for Python 3 via Pipenv
    ```shell
    pipenv install --three Lektor
    ```
3. Run Lektor development server (with custom output path)
    ```shell
    ./run.sh
    ```
   - access development site at http://127.0.0.1:5000/

[pipenv]: https://docs.pipenv.org/en/latest/
[lektor]: https://www.getlektor.com/docs/


## Resources

- Software
  - [Lektor Documentation][lektor]: Static Content Management System
  - [Pipenv Documentatio][pipenv]: Python Dev Workflow for Humans
  - [Skeleton][skeleton]: Responsive CSS Boilerplate
- Guides
  - [Building a static blog with Lektor | Animesh Bulusu][building]

[skeleton]: http://getskeleton.com/
[building]: https://animesh.blog/building-a-static-blog-with-lektor/


## License


### Code

All the code within this repository is licensed under a [Unlicense][unlicense]
unless otherwise specified. (Much of the code used in this respository is
standard boilerplate or otherwise *should* be too simple and obvious to
copyright.)

[unlicense]:https://unlicense.org/ "Unlicense.org » Unlicense Yourself: Set Your Code Free"


### Content

All the content within this repository is licensed under a [Creative Commons 
Attribution-ShareAlike 4.0 International License][cc-by-sa] unless otherwise
specified.

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/ "Creative Commons — Attribution-ShareAlike 4.0 International — CC BY-SA 4.0"


### Skeleton

All parts of [Skeleton][skeleton-gh] are free to use and abuse under the
[open-source MIT license][mit].

[skeleton-gh]: https://github.com/dhg/Skeleton
[mit]: https://github.com/dhg/Skeleton/blob/master/LICENSE.md
