# CSS Dig

**Note: There is now a [CSS Dig Chrome Extension](https://chrome.google.com/webstore/detail/css-dig/lpnhmlhomomelfkcjnkcacofhmggjmco) that duplicates most of this functionality and is much easier to use.**

Inspired by Nicolle Sullivan’s advice to “grep your styles”, CSS Dig is is a Python script that runs locally to  unearth properties and values from almost any website — from both linked CSS files as well as any styles found in the head — to help you analyze, refactor, standardize and maintain your CSS.

See [CSS Dig: It’s Time to Refactor](http://www.atomeye.com/css-dig.html) for more context.

Some sample reports:

<ul>
  <li><a href="http://www.atomeye.com/dig-reports/nytimes.html">Report for http://nytimes.com</a></li>
  <li><a href="http://www.atomeye.com/dig-reports/nytimes-world.html">Report for http://nytimes.com/pages/world/index.html</a></li>
  <li><a href="http://www.atomeye.com/dig-reports/msn.html">Report for http://msn.com</a></li>
  <li><a href="http://www.atomeye.com/dig-reports/aol.html">Report for http://aol.com</a></li>
  <li><a href="http://www.atomeye.com/dig-reports/apple.html">Report for http://apple.com</a></li>
</ul>


## What it Does

1. CSS Dig will look for `<link>` tags with `rel="stylesheet"` at the URL you provide as well as any `<style>` blocks on the page.
2. It reads in and combines that CSS and then finds all unique properties, using those to find all the declarations.
3. From that it creates the counts and groups them for viewing and inspecting.

## Requirements


You'll need at least Python 2.7. Run:

    python -V

in the command line if you're unsure. You should see something like:

    Python 2.7.2

Python modules you’ll likely need to install.

- [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

If you've never used Python before probably the easiest way to get modules installed is to use Easy Install:

- [Easy Install](https://pypi.python.org/pypi/setuptools/0.7.2#installation-instructions)

After that completes you can run:

    easy_install beautifulsoup4

or

    sudo easy_install beautifulsoup4


## Installation and Usage

Clone or download this repository to your computer. Open a terminal window and navigate to this folder. Run the following:

    python cssdig.py http://atomeye.com

...replacing http://atomeye.com with any URL you'd like to run a report on.

If it runs successfully you should see the following:

    Attempting to reach URL...
    Finding CSS at URL...
    Building report...
    Report complete.

You'll find your report inside a 'report' folder that will be created in the same directory. That 'report' directory is self-contained so you copy it, archive it, etc.

If you get errors about 'No module found...' please install any missing modules.

## Limitations

- It currently only works with http:// URLs that return HTML. It won't yet work against files on your computer or individual CSS files (like http://domain.com/style.css).
- There are a number of regular expressions that work with the Combined CSS in the third panel. This was done so that it would be readable but would leave any original errors in place. It's not perfect but seems to work well enough. If you see any strangeness let me know.
- In the script I've excluded some URLs from font providers so it won't be mixed in with the data. You can edit this list as needed.

## Please Contribute

I am neither a Python programmer nor a regex master so there are likely improvements to be made. I'd also love to see this built into a proper web app so it would be dead simple to use.
