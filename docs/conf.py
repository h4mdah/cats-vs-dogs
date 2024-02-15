# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "cats-vs-dogs"
copyright = "2024, Hamdah"
author = "Hamdah"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "notfound.extension",  # for 404 page
    "recommonmark",  # for markdown
    "sphinx_copybutton",  # for copy button
    "sphinx-prompt",  # for prompt
    "sphinx.ext.viewcode",  # for source code
    "sphinx.ext.githubpages",  # for github pages
    "nbsphinx",  # for jupyter notebook
]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# sphinx-notfound-page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>Try using the search box or go to the homepage.</p>
""",
}
notfound_urls_prefix = "/cats-vs-dogs/"

# The master toctree document.
master_doc = "index"
language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# syntax highlighting
pygments_style = "sphinx"
highlight_language = "python3"

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "cats-vs-dogs-doc"
