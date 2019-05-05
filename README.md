# fsckme.zehta.me

Source for [fsckme.zehta.me][fsckme].

[fsckme]: https://fsckme.zehta.me/


## Overview

The source is located in [`fsckme/`](fsckme/).

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
- Guides
  - [Building a static blog with Lektor | Animesh Bulusu][building]

[building]: https://animesh.blog/building-a-static-blog-with-lektor/


## License


### Code

The code is licensed under a Expat/[MIT][mit] License.

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"


### Content

The content is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/ "Creative Commons — Attribution-ShareAlike 4.0 International — CC BY-SA 4.0"
