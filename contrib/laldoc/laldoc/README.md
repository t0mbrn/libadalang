# LALDoc modification to support AdaDocTests

This laldoc fork was modified to support [AdaDocTest](https://github.com/t0mbrn/adadoctest/) syntax.

## Dependencies:
- [AdaCore LibAdaLang](https://github.com/AdaCore/libadalang) esp.[LALdoc](https://github.com/t0mbrn/libadalang/tree/be141d8f03a46e7240decb6c86d6eed17acf9345/contrib/laldoc/laldoc)
- [Read the Docs Sphinx Theme](https://github.com/readthedocs/sphinx_rtd_theme)
- [AdaCore Sphinx AdaDomain](https://github.com/AdaCore/sphinxcontrib-adadomain/blob/master/sphinxcontrib/adadomain.py)
- For testing purposes: [AdaDocTest-Working](https://github.com/t0mbrn/adadoctest-working#readme)

## Usage
1. `sphinx-quickstart`:

    1.1 In your new Sphinx `conf.py` file:
    - Add `'adadomain'` to `extensions`.
    - Add `'libadalang'` to `exclude_patterns`.
    - Set `"sphinx_rtd_theme"` as `html_theme`.
    - Set:
    ```python
    html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
    ```

    1.2. Set your LD_LIBRARY_PATH and PYTHONPATH as follows:
    ```shell
        LD_LIBRARY_PATH=<GNAT Path>/lib:<GNAT Path>/lib/gcc/x86_64-pc-linux-gnu/10.3.1/rts-native/adalib/
        PYTHONPATH=<Path to your LibAdaLang-[...].whl file>
    ```

2. `generate_rst.py`:

    2.1. `-P`: Enter your projects GPR-file-path

    2.2. Enter **all file paths** you want RST documentation files generated for.

    2.2. `-O`: Specify an **Out-Path** for the RST generation

    ```shell
    $ python3 generate_rst.py -P <projectPath>/<projectName>.gpr <file1.ads> <file2.ads> ... -O ./out/<projectName>/rst/
    ```

3. Enter this **Out-Path** as Python `-P` parameter to `collectRSTs.py`
```shell
$ python3 collectRSTs.py -P ./out/<projectName>/rst/
```

4. Specify the **Out-Path** for the `sphinx-build` HTML generation:
```shell
$ sphinx-build -b html ./ ./out/<projectName>/html
```

> Try to run this tool in the same directory specified in `sphinx-quickstart` in order to avoid bugs.
>
> If **index.rst** cannot be found by `collectRSTs.py` try to follow this advice.

