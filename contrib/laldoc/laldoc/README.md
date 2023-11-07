# LALDoc modification to support AdaDocTests

This laldoc fork was modified to support [AdaDocTest](https://github.com/t0mbrn/adadoctest/) syntax.

## Usage
(After using `sphinx-quickstart` once)
1. Enter **all desired file paths** (seperated by '\\') as Python parameters in the RST generation section for `./libadalang/contrib/laldoc/laldoc/generate_rst.py`.
2. Specify an **Out-Path** for the RST generation (`-O ./out/<projectName>/rst`).

3. Enter this **Out-Path** as Python `-P` parameter to `collectRSTs.py` (`python3 collectRSTs.py -P ./out/<projectName>/rst/`).

4. Specify an **Out-Path** for the `sphinx-build` HTML generation:
```
sphinx-build -b html ./ ./out/<projectName>/html
```

> Try to have the Makefile in the same directory specified in `sphinx-quickstart` in order to avoid bugs.
> In **index.rst** cannot be found by `collectRSTs.py` try to follow this advice.

Finally use `make` to execute the documentation toolchain.