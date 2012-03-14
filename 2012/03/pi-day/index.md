It was pretty late last night when I finished my post about blogging with WordPress and Dexy, so I didn't even notice it had turned into [&pi; day](http://en.wikipedia.org/wiki/Pi_Day). This morning of course twitter reminded me, and in particular this caught my eye:

<blockquote class="twitter-tweet"><p>Can anyone draw me a plot of &radic;[6(1 + 1/2^2 + 1/3^2 + 1/4^2...)] &rarr;&pi;? Excel is not only ok, it's recommended. Should bounce around and close in.</p>&mdash; Matt Parker (@standupmaths) <a href="https://twitter.com/standupmaths/status/179934335120572416" data-datetime="2012-03-14T14:17:43+00:00">March 14, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<!--more-->

Lots of people have done cool graphs using spreadsheets. Here's a google spreadsheets version:

<blockquote class="twitter-tweet"><p>Here's a nice spreadsheet simulating &radic;[6(1 + 1/2^2 + 1/3^2 + 1/4^2...)] &rarr;&pi; <a href="https://twitter.com/search/%2523piday">#piday</a> RT @<a href="https://twitter.com/si_kelly">si_kelly</a>: @<a href="https://twitter.com/standupmaths">standupmaths</a> <a href="https://t.co/dsMoS679" title="https://docs.google.com/spreadsheet/ccc?key=0AhTWpGoiXjKQdGJVd3E5WXNZVTI4U1Z3a0F6ZWNoREE#gid=0">docs.google.com/spreadsheet/cc...</a></p>&mdash; Matt Parker (@standupmaths) <a href="https://twitter.com/standupmaths/status/179973838233272320" data-datetime="2012-03-14T16:54:41+00:00">March 14, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

As Matt says, Excel is recommended here because it's very easy to set up the formulas and graph them. It makes it very intuitive. But, I'm going to try this out using Python just because I feel like playing with some math today and spreadsheets are pretty awkward on my little netbook.

Here's the formula, made a little easier to read thanks to LaTeX and MathJax:

<div id="converges-to-pi">$$\sqrt{6\left(1+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{4^2}\dots\right)}$$</div>

Here's my first implementation:

{{ d['code.py|fn|idio|pycon|pyg']['calcs'] }}

We've stored the first 20 values in an array, so let's graph them:

{{ d['code.py|fn|idio|pycon|pyg']['graph'] }}

![graph of approximation of pi using sum of inverse squares]({{ d['pi.png|boto'] }})

Not bad, but we'll want to go a little farther out. Also, a fun addition to this was also posted:

<blockquote class="twitter-tweet" data-in-reply-to="179934335120572416"><p>@<a href="https://twitter.com/standupmaths">standupmaths</a> A guess: did you want the alternating odd inverses summing to 4/&pi;? In case you did: <a href="http://t.co/9dbG0KYK" title="http://twitter.com/outofthenorm2/status/179942642627522560/photo/1">twitter.com/outofthenorm2/...</a></p>&mdash; out of the norm (@outofthenorm2) <a href="https://twitter.com/outofthenorm2/status/179942642627522560" data-datetime="2012-03-14T14:50:44+00:00">March 14, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

So, let's try this again defining some functions:

{{ d['code.py|fn|idio|pycon|pyg']['calcs-2'] }}

Now we can graph it:

{{ d['code.py|fn|idio|pycon|pyg']['graph-2'] }}

![graph of approximation of pi using sum of inverse squares and Gregory-Leibniz series]({{ d['pi2.png|boto'] }})

There's more information about approximating pi on [this wikipedia page](http://en.wikipedia.org/wiki/Approximations_of_%CF%80). You can get the source code for this blog post and play around with it [on github](https://github.com/ananelson/dexy-blog/tree/master/2012/03/pi-day).
