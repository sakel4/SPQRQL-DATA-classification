# ClassificationApp
> ## API Endpoints:

- /triplets?dataset=BNF
    - **parameters**
        - dataset (possible values: BNF,DB_PEDIA,CONFERENCE,HIST_MUNIC)
    - **return value**
        - all dataset triplets
- /types?dataset=BNF
    - **parameters**
        - dataset (possible values: BNF,DB_PEDIA,CONFERENCE,HIST_MUNIC)
    - **return value**
        - all dataset distinct types
- /predicates?dataset=BNF
    - **parameters**
        - dataset (possible values: BNF,DB_PEDIA,CONFERENCE,HIST_MUNIC)
    - **return value**
        - all dataset distinct predicates
- /subjects?dataset=BNF
    - **parameters**
        - dataset (possible values: BNF,DB_PEDIA,CONFERENCE,HIST_MUNIC)
    - **return value**
        - all dataset distinct subject
- /classification?dataset=BNF&statistics=true
    - **parameters**
        - dataset (possible values: BNF,DB_PEDIA,CONFERENCE,HIST_MUNIC)
        - statistics (possible values: true or false)
    - **return value**
        - ***if statistics equal false:*** all subjects triplets and types
        - ***if statistics equal true:*** statistics object (structure available in sampleResponse.json)
> ## Prerequisites:

-   Python:
    -   Python: 3.9.9
-   SPARQLWrapper:
    ```bash
    pip install sparqlwrapper
    ```
-   Flask:
    ```bash
    pip install Flask
    ```
-   Scikit-learn:
    ```bash
    pip install scikit-learn
    ```
-   Pandas:

    ```bash
    pip install pandas
    ```

    > ## Create Environment:

-   Linux/Mac OS:(on linux works without the creation of the virtual environment)
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

> ## Activate Environment (requires the environment creation):

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
    $ export FLASK_APP=__filename__
    $ export FLASK_ENV=development
    $ flask run
    ```
-   Windows(CMD):
    ```bash
    $ set FLASK_RUN_PORT=5000
    $ set FLASK_APP=__filename__
    $ set FLASK_ENV=development
    $ flask run
    ```
