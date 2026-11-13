# GitHub Pages source

1. Publishing source: **Deploy from a branch**.
2. Branch: **master**. Folder: **/docs**.
3. Edit `docs/index.md` for page text, `docs/_layouts/default.html` for layout and `docs/assets/style.css` for styling. The initial page text comes from the current README.
4. GitHub runs Jekyll directly on `docs/`. Commit Markdown, Liquid templates, configuration, styles and selected images. Jekyll output and caches are ignored by Git.

Local build with an existing Jekyll installation:

```sh
jekyll build --source docs --destination _site
```
