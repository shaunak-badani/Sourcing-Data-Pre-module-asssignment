# Word generator

Generates a list of paragraphs. Each paragraph is a list of random words, which may or may not make sense grammatically.

### How to run:

- Setup the virtual env:

    ```
    python3 -m venv pre-module-pckgs
    source pre-module-pckgs/bin/activate
    pip3 install -r requirements.txt
    ```

- Different methods of running the program

    ```
    python3 wordgen.py -n 2
    python3 wordgen.py -n 5 --min 20
    python3 wordgen.py -n 8 --max 5
    python3 wordgen.py -n 9 --min 76 --max 79
    ```

### Running the tests:
```
pytest
```