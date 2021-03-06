# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))

import pyretem


# -- Project information -----------------------------------------------------

project = "pyretem"
copyright = "2021, CoopTeam-CERFACS"
author = "CoopTeam-CERFACS"

# The full version, including alpha/beta/rc tags
release = pyretem.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc",
              "sphinx.ext.viewcode", "sphinx.ext.autosummary",
              "sphinx.ext.intersphinx",
              "sphinx_copybutton", "sphinx_autodoc_typehints",
              "myst_parser", "nbsphinx",
              ]

source_suffix = [".rst", ".md", ".ipynb"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# general sphinx config
add_module_names = False


# intersphinx options
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}


# napoleon options
napoleon_use_admonition_for_notes = True
napoleon_preprocess_types = True
napoleon_type_aliases = {
    "np.array": "numpy.ndarray"
}

# mathjax config within myst_parser
suppress_warnings = ["myst.mathjax"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/lpereira95/python-repo-template",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
