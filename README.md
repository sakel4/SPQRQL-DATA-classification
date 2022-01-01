# ClassificationApp

Prerequisites:

-   Python:
    -   Python: 3.9.9
-   SPARQLWrapper:
    -   install: pip install sparqlwrapper
-   Flask:
    -   install: pip install Flask

Create Enviroment:

-   Linux/Mac OS:
    -   $ mkdir myproject
    -   $ cd myproject
    -   $ python3 -m venv venv
-   Windows:
    -   $ mkdir myproject
    -   $ cd myproject
    -   $ py -3 -m venv venv

Activate Enviroment:

-   Linux/Mac OS:
    -   $ . venv/bin/activate
-   Windows:
    -   $ venv\Scripts\activate

Initialize Server:

-   Linux/Mac OS:
    -   $ export FLASK_RUN_PORT=5000
    -   $ export FLASK_APP=**filename** (only the first time)
    -   $ flask run
-   Windows(CMD):
    -   $ set FLASK_RUN_PORT=5000
    -   $ set FLASK_APP=**filename** (only the first time)
    -   $ flask run
