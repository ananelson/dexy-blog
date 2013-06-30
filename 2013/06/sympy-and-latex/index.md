[SymPy](http://sympy.org/) is a [computer algebra system](http://en.wikipedia.org/wiki/Computer_algebra_system) for Python. This blog post will talk about how to use SymPy with Dexy to get automated mathematical LaTeX in your documents.

<!--more-->

{% macro show_derivatives() -%}
<!-- section "derivatives" -->
{% for deriv_latex in d['derivatives.json'].from_json() %}
$${{ deriv_latex }}$$
{% endfor %}
<!-- section "end" -->
{% endmacro -%}

{% macro show_integrals() -%}
<!-- section "integrals" -->
{% for integral_latex in d['integrals.json'].from_json() %}
$${{ integral_latex }}$$
{% endfor %}
<!-- section "end" -->
{% endmacro -%}

With SymPy you can calculate things like this derivative table:

{{ show_derivatives() }}

or this integral table:

{{ show_integrals() }}

To generate these tables, we modify [this example from the Sympy wiki](https://github.com/sympy/sympy/wiki/Generating-tables-of-derivatives-and-integrals).

Here's the imports for this script:

{{ d['table.py|idio|pycon|pyg']['imports'] }}

We start by defining functions which return [equality](http://docs.sympy.org/dev/modules/core.html#eq) objects relating the derivative or integral to its calculated expression:

{{ d['table.py|idio|pycon|pyg']['define-functions'] }}

Here's a simple example of what this function returns:

{{ d['table.py|idio|pycon|pyg']['example-deriv'] }}

Here's another:

{{ d['table.py|idio|pycon|pyg']['example-integral'] }}

Then, we define functions which return the LaTeX representation of that equality:

{{ d['table.py|idio|pycon|pyg']['define-latex-functions'] }}

Here's what these functions return:

{{ d['table.py|idio|pycon|pyg']['example-deriv-latex'] }}
{{ d['table.py|idio|pycon|pyg']['example-integral-latex'] }}

So, it's very simple to generate the LaTeX we want, now we just need a way of displaying that LaTeX in a dexy document. A recommended way of sharing content between dexy documents is to use JSON. JSON is widely available and is human readable for debugging. JSON objects map nicely to Python dictionaries, and dexy defines a `from_json()` method which you can use to easily parse JSON into their corresponding Python objects (dictionaries, lists, or whatever the JSON happens to map to).

So, in our Python script, let's define a simple dict which contains the latex we want, referenced by a memorable name, and save this to a JSON file:

{{ d['table.py|idio|pycon|pyg']['save-examples-latex'] }}

Then in a Markdown-formatted document, we can do something like this:

<pre>
{{ d['index.md|htmlsections']['examples'] }}
</pre>

And the result looks like this:

<!-- section "examples" -->
{% set example_latex = d['example-latex.json'].from_json() -%}
Here is the derivative example:
$${{ example_latex.derivative }}$$

And here is the integral example:
$${{ example_latex.integral }}$$
<!-- section "end" -->

Now, we want to see how to generate the derivative and integral tables we started with. Instead of a dictionary letting us pick out individual examples, we'll generate a list and store this list in JSON, then iterate over and display each element in the list in order.

We use two list comprehensions, the first generates a list of functions, the second returns the LaTeX for the expressions:

{{ d['table.py|idio|pycon|pyg']['derivatives'] }}

And here is how we load the JSON saved to `derivatives.json` and iterate over each entry, to generate the table:

<pre>
{{ d['index.md|htmlsections']['derivatives'] }}
</pre>

Here's the table again:

{{ show_derivatives() }}

We do much the same for the integrals table, here's the Python which generates the JSON:

{{ d['table.py|idio|pycon|pyg']['integrals'] }}

And here is how we load the JSON and generate the table:

<pre>
{{ d['index.md|htmlsections']['integrals'] }}
</pre>

Here's the table again:

{{ show_integrals() }}

That's how you can use SymPy, JSON and Dexy to get automated math into your documents. We've been displaying the LaTeX within a HTML document and using [MathJax](mathjax.org) to render it, but of course you can just insert the LaTeX content into a .tex file and render it to a PDF.

Another option, besides using JSON, is to print the LaTeX content to STDOUT within your python scripts and then use dexy to insert the output into a document directly. For example:

{{ d['example.py|pyg'] }}

Here is how we could insert this into a document:

<pre>
{{ d['index.md|htmlsections']['use-stdout'] }}
</pre>

And here's what it looks like:

<!-- section "use-stdout" -->
$${{ d['example.py|py'] }}$$
<!-- section "end" -->

This is simpler, although using JSON is more flexible and robust.
