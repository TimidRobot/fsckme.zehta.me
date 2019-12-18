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
    - [nixjdm/lektor-atom][atom]: Lektor Atom plugin.
    - [lektor/lektor-markdown-header-anchors][md-header]: Adds support for
      anchors and table of contents to Markdown.
    - [pietroalbini/lektor-minify][minify]: Minify build artifacts in a Lektor
      project
    - [Andrew-Shay/lektor-read-full-post][read-full]: Allows blog listing posts
      to be shortened with a link to the full post.
  - [Pipenv Documentatio][pipenv]: Python Dev Workflow for Humans
  - [Skeleton][skeleton]: Responsive CSS Boilerplate
- Guides
  - [Building a static blog with Lektor | Animesh Bulusu][building]

[atom]: https://github.com/nixjdm/lektor-atom
[md-header]: https://github.com/lektor/lektor-markdown-header-anchors
[minify]: https://github.com/pietroalbini/lektor-minify
[read-full]: https://github.com/Andrew-Shay/lektor-read-full-post
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


### Font Awesome

Font Awesome Free is free, open source, and GPL friendly. You can use it for 
commercial projects, open source projects, or really almost whatever you want.
Full Font Awesome Free license: https://fontawesome.com/license/free.

**Icons:** CC BY 4.0 License (https://creativecommons.org/licenses/by/4.0/)
In the Font Awesome Free download, the CC BY 4.0 license applies to all icons
packaged as SVG and JS file types.

**Fonts:** SIL OFL 1.1 License (https://scripts.sil.org/OFL)
In the Font Awesome Free download, the SIL OFL license applies to all icons
packaged as web and desktop font files.

**Brand Icons:**
All brand icons are trademarks of their respective owners. The use of these
trademarks does not indicate endorsement of the trademark holder by Font
Awesome, nor vice versa. **Please do not use brand logos for any purpose except
to represent the company, product, or service to which they refer.**


### Skeleton

*All parts of [Skeleton][skeleton-gh] are free to use and abuse under the
[open-source MIT license][mit].*

[skeleton-gh]: https://github.com/dhg/Skeleton
[mit]: https://github.com/dhg/Skeleton/blob/master/LICENSE.md
