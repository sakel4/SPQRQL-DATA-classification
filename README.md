# ClassificationApp

> ## Prerequisites:

-   Python:
    -   Python: 3.9.9
-   SPARQLWrapper:
    ```bash
    pip install sparqlwrapper
    ```
-   Flask:
    ```bash
    install: pip install Flask
    ```

> ## Create Environment:

-   Linux/Mac OS:
    ```bash
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv
    ```
-   Windows:
    ```bash
    $ mkdir myproject
    $ cd myproject
    $ py -3 -m venv venv
    ```

> ## Activate Environment:

-   Linux/Mac OS:
    ```bash
    $ . venv/bin/activate
    ```
-   Windows:
    ```bash
    $ venv\Scripts\activate
    ```

> ## Initialize Server:

-   Linux/Mac OS:
    ```bash
    $ export FLASK_RUN_PORT=5000
    $ export FLASK_APP=__filename__ (only the first time)
    $ flask run
    ```
-   Windows(CMD):
    ```bash
    $ set FLASK_RUN_PORT=5000
    $ set FLASK_APP=__filename__ (only the first time)
    $ flask run
    ```
