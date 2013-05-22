Let's check out the new [Stargazer](http://bit.ly/1a5jCVA) library for making beautiful PDF tables and see how to make it work with dexy. To use the R package we first load the library:

{{ d['tables.R|idio|rint|pyg']['import-library'] }}

Here's the basic demo:

{{ d['tables.R|idio|rint|pyg']['basic-demo'] }}

This prints the LaTeX markup in our R session. The Stargazer docs say:

     ‘stargazer’ uses ‘cat()’ to output LaTeX code for the table. To
     allow for further processing of this output, ‘stargazer’ also
     returns the same output invisibly as a character string vector.
     You can include the produced tables in your paper by inserting
     ‘stargazer’ output into your publication's TeX source.

So, according to this there's no built-in way to get stargazer to write its output directly to a file. One option would be to use R's sink() to divert the output from stargazer:

{{ d['tables.R|idio|rint|pyg']['basic-demo-with-sink'] }}

This gives us a file named `output-from-sink.tex` which we can include in documents.

That works fine, we can create as many separate files as we need. However, it might be nice to create a single file with multiple LaTeX snippets in it, referenced by name.

To do this we create a list and add named elements to the list containing output from running stargazer:

{{ d['tables.R|idio|rint|pyg']['create-object'] }}

We'll also generate the regression output example from [Tal Galili's blog post](http://bit.ly/10TgaJp) and save this to the list:

{{ d['tables.R|idio|rint|pyg']['save-ols-models'] }}

Then we export this list to a JSON file using the rjson library:

{{ d['tables.R|idio|rint|pyg']['save-objects'] }}

Now let's create a LaTeX document and make use of the snippets we have generated. Here's the full source of the LaTeX document:

{{ d['example.tex|idio'] }}

Here is how we configure the latex document to include the output from `tables.R` (you don't need the 'botoup' filter unless you want to upload your PDF to Amazon S3):

{{ d['dexy.yaml|idio']['example.tex'] }}

Here's part of the LaTeX document showing how we include the contents of the standalone file we created using `sink()`:

{{ d['example.tex|idio']['output-from-sink'] }}

To load our named list, we call the `from_json()` method to convert the JSON to a (python) dictionary:

{{ d['example.tex|idio']['snippets'] }}

Then we can access the elements in this list as follows:

{{ d['example.tex|idio']['use-snippets'] }}

We can use a dot to access the elements because of [jinja](http://jinja.pocoo.org/docs/templates/#variables). You can download the generated PDF to see what it looks like [here]({{ d['example.tex|jinja|latex|botoup'] }}).

That was two different ways to get Stargazer's output into a file (for use with dexy).
