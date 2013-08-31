I just received a question about how to use Dexy to document procedural (non-OOP) PHP code. Here are some ways of using dexy to document PHP. These examples assume you already have familiarity with the contents of the [Getting Started](http://dexy.it/guide/getting-started.html) part of the [guide](http://dexy.it/guide/).

<!-- more -->

## Displaying Complete Files

Let's take a simple example of an HTML file with embedded PHP:

<!-- @section "full-php-file" -->
{{ d["example.php|pyg"] }}
<!-- @end -->

We'll use this example file in the subsequent examples. In order to display it above we used the `pyg` filter to apply syntax highlighting. This was specified in the `dexy.yaml` file as follows:

{{ d['dexy.yaml|idio']['pyg'] }}

And included in this document like this:

{{ d['index.md|idio']['full-php-file'] }}

For more information, see the [documentation page for dexy's pyg filter](http://dexy.it/filters/pyg).

## Executing PHP

We can use dexy's `php` filter to run this file through a php interpreter and see the result:

<!-- @section "php-results-pre-tag" -->
<pre>
{{ d["example.php|php"] | e }}
</pre>
<!-- @end -->

That was the contents displayed using a pre tag:

{{ d['index.md|idio']['php-results-pre-tag'] }}

We can also display the results with syntax highlighting:

<!-- @section "php-results-pyg"-->
{{ d["example.php|php|pyg"] }}
<!-- @end -->

{{ d['index.md|idio']['php-results-pyg'] }}

Here is how these are specified in `dexy.yaml`:

{{ d['dexy.yaml|idio']['php'] }}

The contents of the resulting HTML file could also be displayed in HTML documentation using an iframe. This is done a lot in the [Getting Started](http://dexy.it/guide/getting-started.html) guide.

## Sections of Files

To document what is going on in a file, we really need to be able to isolate sections of a file to discuss what is happening in that small section. We can do this using the `idio` filter in dexy, and fortunately this filter has recently been redone to support HTML-style comments as well as comments used in most programming languages, so you can mix and match these within an embedded PHP file. (You probably noticed these comments in the PHP file above.)

In the `dexy.yaml` file, we apply the `idio` filter to our php example file:

{{ d["dexy.yaml|idio"]["idio"] }}

Then, we can talk about just the `head` section in the HTML:

<!-- @section "ex-head" -->
{{ d["example.php|idio"]["head"] }}
<!-- @end -->

Or the `assign-variables` section:

<!-- @section "ex-assign-variables" -->
{{ d["example.php|idio"]["assign-variables"] }}
<!-- @end -->

And then the section where we compare the variables:

<!-- @section "ex-compare" -->
{{ d["example.php|idio"]["compare"] }}
<!-- @end -->

Here is the source of how these items were included in this document:

{{ d['index.md|idio']['ex-head'] }}
{{ d['index.md|idio']['ex-assign-variables'] }}
{{ d['index.md|idio']['ex-compare'] }}

HTML-style comments will be preserved as your php passes through the php filter (just be careful to leave a blank line after each closing `?>`), so that you can also apply the `idio` filter to the output from the php filter:

{{ d["dexy.yaml|idio"]["php-idio"] }}

In this way we can show the php:

<!-- @section "src-idio" -->
{{ d["example.php|idio"]["display-variables"] }}
<!-- @end -->

And the resulting HTML:

<!-- @section "output-idio" -->
{{ d["example.php|php|idio"]["display-variables"] }}
<!-- @end -->

Here's how we included each of these in this document:

{{ d['index.md|idio']['src-idio'] }}
{{ d['index.md|idio']['output-idio'] }}

## Syntax Highlighting Sections

You might have noticed that the syntax highlighting wasn't applied to the HTML content in the previous section, and we had to pass some custom arguments to the lexer to make things work for the PHP content. The PHP syntax highlighter in pygments is stateful and keeps track of whether it is in a HTML or PHP region of the source code file. However, because we pass our source code in in sections, the lexer isn't able to keep track of the state.

This should be a solvable problem and you can track progress on it [here](https://github.com/ananelson/dexy/issues/67), but for now you'll have to tweak the settings if you want syntax highlighting, and please feel free to [get in touch](mailto:info@dexy.it) if you need help getting the output you want.

## Deployment, Screenshots and Integration Testing

An additional approach which you can take to documenting PHP projects is to start a server locally (or on a virtual machine either locally or in the cloud) and run a headless web browser against that server to take screenshots and make assertions about the displayed content.

This approach is applicable to any web application, regardless of the underlying technology. It also allows you to document JavaScript components of your application. (You can also use the same `pyg` and `idio` filters to document JavaScript source files.)

The [quickstart](http://www.dexy.it/guide/quickstart.html#django-polls-app) section of the Dexy Guide contains an example of bash scripts which start a local server, [casper.js](http://www.casperjs.org/) scripts which interact with the application running on that server, and then take screenshots and make assertions about the state of the application, as well as documentation which incorporates all these elements.

For example, here is a fully automated full-page screenshot of the polls app from the [Django tutorial](https://docs.djangoproject.com/en/1.5/intro/tutorial01/):

![automated screenshot from Django tutorial polls app](http://www.dexy.it/guide/code/quickstart/example/output-site/logged-in-admin.png)

