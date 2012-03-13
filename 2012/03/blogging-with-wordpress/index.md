In this tutorial we'll walk through creating and then modifying a WordPress blog post. All the features mentioned in this blog post are available in Dexy 0.5.7. In order to post content to WordPress we will use its XMLRPC API, so before you try this yourself make sure you have enabled this option; it is disabled by default.

We'll start in an empty directory. We need to configure our directory to know where our WordPress installation is, and to provide our username and password. Fortunately Dexy's new filter commands make this really easy. The `create_keyfile` command from the WordPress filter will create the configuration file we need to store our credentials:

{{ d['script.sh|fn|idio|shtmp']['wp-fcmd-help']['transcript-html'] }}

We could also call the `create_keyfile` filter command on the ApiFilter classs (the parent class of WordPressFilter), and this would create a keyfile in the user's home directory that we could use to store all our API credentials:

{{ d['script.sh|fn|idio|shtmp']['apis-fcmd-help']['transcript-html'] }}

The user-wide approach is usually more convenient, since you can run your dexy scripts from anywhere and only need to have your credentials in one place. On the other hand, per-project config is useful if you need to override the defaults to post to a different blog, if you prefer to keep the credentials closer to where you will be using them, or if you are just getting started and want the simplest option.

{{ d['script.sh|fn|idio|shtmp']['call-wp-fcmd']['transcript-html'] }}

{% set configfile = ".dexyapis" -%}
This has created a JSON file named {{ configfile }} which looks like this:

<pre>
{{ d['script.sh|fn|idio|shtmp']['call-wp-fcmd']['files'][configfile] }}
</pre>

You should replace the TODO items with the values appropriate for your website. The url required is the base url for your blog. Here is the config file that I used to create this example:

<pre>
{{ d['ex1-dexyapis|dexy'] }}
</pre>

You'll notice that I didn't actually type my username and password into the .dexyapis file. You can type your actual username and password, or if you have environment variables set up to store your useranme and password then you can put references to environment variables by starting with a $, and the ApiFilter will fetch these for you. The advantage of using environment variables is that you can commit your `.dexyapis` file to your project repository without committing sensitive information.

Let's test this out to make sure it's working before we actually start writing our blog post. Let's get a list of all the filter commands that are provided by the WordPressFilter:

{{ d['script.sh|fn|idio|shtmp']['fcmds']['transcript-html'] }}

The `list_categories` filter command will print out the categories that are defined in your blog. It has to authenticate and visit the correct URL to do this, so it's a good test (especially if you have custom categories set up):

{{ d['script.sh|fn|idio|shtmp']['list-categories']['transcript-html'] }}

Ok, now that we have that working let's move on to an actual blog post. To start with, let's just try to post a simple static HTML file like this:

{{ d['ex1-index.html|pyg'] }}

{% set configfile = "wordpress.json" -%}
We also need to create a configuration file named `{{ configfile }}` to hold some simple metadata about our blog post.

<pre>
{{ d['script.sh|fn|idio|shtmp']['list-categories']['files'][configfile] }}
</pre>

Here is the `.dexy` configuration file we need:

{{ d['ex1-dexy|ppjson|pyg'] }}

The WordPress filter alias is just `wp` (you can see the filter reference [here](http://dexy.it/docs/filters/wp)). We specify `wordpress.json` as an input so that if there are any changes to that file, Dexy will upload our blog post to wordpress again. You could omit this and just `touch` your blog post file to trigger an upload.

And that's all we need to do to create our first blog post! Because this is a new dexy project, we need to run dexy setup:

{{ d['script.sh|fn|idio|shtmp']['dexy-setup']['transcript-html'] }}

And then we can run dexy:

{{ d['script.sh|fn|idio|shtmp']['dexy']['transcript-html'] }}

If this has completed successfully, then our `{{ configfile }}` has changed. It now looks like this:

<pre>
{{ d['script.sh|fn|idio|shtmp']['dexy']['files'][configfile] }}
</pre>

The `postid` has been filled in. This is very important since next time we run this filter, we don't want to create another blog post, we want to update this same blog post. You can fill in the postid yourself if you already have created a draft post via your WordPress admin interface. Also notice that there is a key called `publish` with a value of false. By default, we create draft blog posts, so they aren't visible to the public yet. But, you can get a preview if you are logged in. Here's our preview:

![screenshot of draft blog post]({{ d['screencap1.png|boto'] }})

Let's go ahead and publish this before we move on to creating a more interesting example. To make this visible, just change the value of `publish` from `false` to `true`, and run dexy again.

![screenshot of published blog post]({{ d['screencap2.png|boto'] }})

Now this is published and anyone can read it.

Where things really get interesting is when we start making use of Dexy to create blog post content that includes code examples and results, so let's do an example of that next.

One thing I'm not going to cover in this post, but will cover in detail very soon, is how to include dexy-generated images in your blog post. The [WordPress filter](http://dexy.it/docs/filters/wp/) will actually already upload images for you to WordPress, but there is a snag. The `overwrite` option in the WordPress API is broken, so each time Dexy thinks your image has changed, another copy will be uploaded to WordPress. This clutters up your Media Library very quickly. (See [this bug report](http://core.trac.wordpress.org/ticket/17604) for more information.) My approach is to use Amazon S3 for image hosting, and there is a `boto` filter in Dexy which will upload images to S3 and return the URL, which I can then use to reference the image. That's how I am displaying the dexy-generated screenshots in this blog post. I'm also working on adding filters for other image and hosting services. There will be a comprehensive blog post on this topic soon, so watch this space (and if you are in a position to do anything to help that WordPress bug get fixed, please do).

When we include code snippets and examples, we probably want to include syntax highlighting. The approach I find easiest is to use pygments within Dexy to apply syntax highlighting, and then to have a pygments stylesheet as part of my blog CSS. If you can't modify the CSS for your blog, then you can still use pygments with the `"noclasses" : true` option, and this will embed the styles directly.

If you would like to use a different syntax highlighting system, and are having trouble getting it to work, then please [open a support ticket](http://dexy.tenderapp.com).

For this example, we will tell pygments to use inline styles rather than classes, so no modification to the CSS is required (which is good since I'm doing this demo using a free wordpress.com blog, so I can't modify the CSS).

We'll use markdown rather than HTML, so we don't have to type as much markup. Here is the source for our blog post:

{{ d['ex2-index.md|pyg'] }}

We'll apply the jinja and markdown filters first, then post to wordpress. We also have several inputs, including a python script and a JavaScript example. Here is the `.dexy` config:

{{ d['ex2-dexy|ppjson|pyg'] }}

We will also tweak our {{ configfile }} to change the title of our blog post, and assign it to a category:

<pre>
{{ d['script.sh|fn|idio|shtmp']['change-title']['files'][configfile] }}
</pre>

And, here's the screenshot of our updated blog post:

![screenshot of blog post with code examples]({{ d['screencap3.png|boto'] }})

If you are new to Dexy, then reviewing tutorials [0](/docs/tutorials/0-hello-world) and [1](/docs/tutorials/1-python) will help you understand how the HTML for that blog post was created. There is a [dexy template](/docs/templates/wordpress-blogpost) containing a similar setup to that described here which you can also download to get started.

That's all for this tutorial! You can check out the source code of this blog post at [github](https://github.com/ananelson/dexy-blog/). If you have any questions please leave a comment, or if you need help getting this to work please open a [support ticket](http://dexy.tenderapp.com).
