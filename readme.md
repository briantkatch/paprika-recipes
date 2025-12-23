# `paprika-recipes` Python Module

This Python module allows you to interact with recipes from the
[Paprika](https://www.paprikaapp.com/) electronic recipe book app.

It's a fork of
[Adam Coddington's module](https://github.com/coddingtonbear/paprika-recipes) updated
for Python 3.13. It also adds support for setting the User-Agent to the Python library.

This codebase is the building block for
[`paprika-mcp`](https://github.com/briantkatch/paprika-mcp).

## User-Agent

The Paprika API requires a known User-Agent string to work properly.

On a Mac, the module will try to build a User-Agent string using the metadata from the
copy of Paprika you downloaded from the Mac App Store. On other platforms, or if there
are major changes in the future, you may need to manually pass a User-Agent via the API.
This also means the CLI will only work on macOS since there is no support added to
override the User-Agent otherwise.