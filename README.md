# fsckme.zehta.me

Source for [fsckme.zehta.me][fsckme].

[fsckme]: https://fsckme.zehta.me/


# Overview

The source is located in `fsckme/`.

The build/content is located in `docs/`.


# Development

1. Install [Pipenv][pipenv]
    ```shell
    brew install pipenv
    ```
2. Install [Lektor][lektor] on Python 3 via Pipenv
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
