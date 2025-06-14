# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Manage Your Home Depot Credit Card'
copyright = '2025, The Home Depot'
author = 'The Home Depot'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Title shown in the browser tab and at the top of HTML pages
html_title = "Homedepot.com/mycard – Access & Manage Your Home Depot Credit Card"

# Short title used in places like the navigation bar
html_short_title = "Home Depot Card Portal"

# Favicon (optional – must be in root or _static directory)
html_favicon = 'favicon.ico'

# Use the default theme or specify one
# html_theme = 'sphinx_rtd_theme'

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Hide "View page source" link
html_show_sourcelink = False

# Theme-specific options (customize depending on theme)
html_theme_options = {
    'show_powered_by': False,
}

# Add any paths that contain custom static files (e.g., style sheets) here
# html_static_path = ['_static']  # Uncomment and add files if needed
