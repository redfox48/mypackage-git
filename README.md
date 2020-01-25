# Example Python Package

This is an example package for teaching purposes. Run using `python -m mypackage`

# Pro Tips

## `__init__` and `__main__`

`init()` is guaranteed to run before `main()` is called (if main is there).

**`__init__.py` marks the directory as a Python package**

* *Runs when you import a package* into a running Python program. For example, `import mymodule` runs `mymodule/__init__.py`

* Lets you set variables on a package wide level.

**`__main__.py` is typically used for running compressed files; allows you to execute packages**

* *Runs as `__main__` when you run a package as the main program.* 

```python
# For example
$ python mypkg_dir
$ python mypkg.zip
# Or, if the program is accessible as a module
$ python -m mypkg
```

These examples at command line run `mypkg/__main__.py`

*Note that a `__main__` module usually doesn't come from a `__main__.py` file. It can, but it usually doesn't. When you run a script like python my_program.py, the script will run as the `__main__` module instead of the my_program module. This also happens for modules run as python -m my_module, or in several other ways.*

## What to include in `__init__.py`?

**3 Options**

1) **Leave `__init__.py` blank.** This enforces explicit imports and thus clear namespaces. The cons are, the user of the package has to import seperate modules and call them with the dot notation.

2) **Import all modules in __init__.py.** The user doesn't have to do multiple imports. The cons are explicit vs implicit, and also as Martelli puts it (paraphrased), "if that's how your package works, maybe it should all go in a single module anyway".

3) **Import key functions from various modules directly into the package namespace.** If you restructure modules, you still have the option to keep the same API for end users. Cons, it dirties the namespace, and very implicit / hacky.


## `if __name__ == "__main__":`

Every module in Python has a special attribute called `__name__`. The value of `__name__` is set to '__main__'  when module run as main program. Otherwise, the value of `__name__` is set to contain the name of the module.

## `Makefile`

Optionally include a `Makefile` and use it as an easy way of managing generic tasks. For example

```
init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
```