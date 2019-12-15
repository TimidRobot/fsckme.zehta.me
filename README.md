# zehta.me

Source for [zehta.me][zehta-me].

[zehta-me]: https://zehta.me/


## Overview

The source is located in [`source/`](source/).

The built content is located in [`docs/`](docs/).


## Development

1. Install [Pipenv][pipenv]
    ```shell
    brew install pipenv
    ```
2. Install [Lektor][lektor] for Python 3 via Pipenv
    ```shell
    pipenv install
    ```
3. Run Lektor development server (with custom output path)
    ```shell
    ./run.sh
    ```
   - access development site at http://127.0.0.1:5000/

[pipenv]: https://docs.pipenv.org/en/latest/
[lektor]: https://www.getlektor.com/docs/


## Theme

See [New Website - Timid Robot](https://zehta.me/2019/12/new-website/).


## Resources

- Software
  - [Lektor Documentation][lektor]: Static Content Management System
    - [lektor/lektor-markdown-header-anchors][md-header]: Adds support for
      anchors and table of contents to Markdown.
    - [Andrew-Shay/lektor-read-full-post][read-full]: Allows blog listing posts
      to be shortened with a link to the full post.
    - [nixjdm/lektor-atom][atom]: Lektor Atom plugin.
  - [Pipenv Documentatio][pipenv]: Python Dev Workflow for Humans
  - [Skeleton][skeleton]: Responsive CSS Boilerplate
- Guides
  - [Building a static blog with Lektor | Animesh Bulusu][building]

[md-header]: https://github.com/lektor/lektor-markdown-header-anchors
[read-full]: https://github.com/Andrew-Shay/lektor-read-full-post
[atom]: https://github.com/nixjdm/lektor-atom
[skeleton]: http://getskeleton.com/
[building]: https://animesh.blog/building-a-static-blog-with-lektor/


## Licenses


### Code

All the code within this repository is licensed under a [Unlicense][unlicense]
unless otherwise specified. (Much of the code used in this respository is
standard boilerplate or otherwise *should* be too simple and obvious to
copyright.)

[unlicense]:https://unlicense.org/ "Unlicense.org » Unlicense Yourself: Set Your Code Free"


### Content

![CC BY-SA 4.0 license button][cc-by-sa-png]

All the content within this repository is licensed under a [Creative Commons 
Attribution-ShareAlike 4.0 International License][cc-by-sa] unless otherwise
specified.

[cc-by-sa-png]: https://licensebuttons.net/l/by-sa/4.0/88x31.png "CC BY-SA 4.0 license button"
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/ "Creative Commons — Attribution-ShareAlike 4.0 International — CC BY-SA 4.0"


### Skeleton

*All parts of [Skeleton][skeleton-gh] are free to use and abuse under the
[open-source MIT license][mit].*

[skeleton-gh]: https://github.com/dhg/Skeleton
[mit]: https://github.com/dhg/Skeleton/blob/master/LICENSE.md
