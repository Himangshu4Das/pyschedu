# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath('..'))
master_doc = 'index'
# -- Project information -----------------------------------------------------
project = 'pyschedu'
author = 'Himangshu Das'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
html_theme_options = {
    'description': 'Python package for scheduling events',
    'github_user': 'your_username',
    'github_repo': 'pyschedu',
    'github_banner': True,
    'github_button': True,
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyschedudoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'pyschedu.tex', 'pyschedu Documentation',
     'Himangshu Das', 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'pyschedu', 'pyschedu Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'pyschedu', 'pyschedu Documentation',
     author, 'pyschedu', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
