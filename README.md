# Website for OpenRazer

A single page website informing users of features, supported devices,
download instructions and project links.

Powered by [Jekyll], a static website generator. Hosted by [GitHub Pages].


## Static API

In addition, there are some static files that can be used by other projects
to get information about OpenRazer.

* [`api/devices.json`](https://openrazer.github.io/api/devices.json) - List of currently supported devices.
* [`api/latest_version.txt`](https://openrazer.github.io/api/latest_version.txt) - Latest version string for OpenRazer.


## Local Setup

1. Install [Ruby](https://jekyllrb.com/docs/installation/other-linux/).
2. Install `jekyll` and `bundler` via Ruby:

       gem install jekyll bundler

    (`sudo` may be required, depending on your distro)

3. Install dependencies:

       bundle install

4. To build and preview the website at http://localhost:4000:

       bundle exec jekyll serve --watch

    (This is also avaliable via `./scripts/watch.sh`)


## Editing

The main content for the page is stored in `index.md` so it's easy to update
without messing with HTML. This is formatted as YAML frontmatter, but
some keys use Markdown syntax (as indicated by `>-`)

Where Markdown is used, a double space is needed for a new line. Code should
be indented with 4 spaces, as backticks are not supported.


## Updating device list

The script at `./scripts/update-device-list.sh` is responsible for updating the
device list. This is intended to be run by a maintainer after a new release,
since the website only shows devices for stable releases.

The script will spawn `openrazer-daemon` against the fake driver, which requires
a clone of the `openrazer` repository next to this one, `openrazer.github.io`.


## License

CC-BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International)

[Jekyll]: https://jekyllrb.com/
[GitHub Pages]: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
