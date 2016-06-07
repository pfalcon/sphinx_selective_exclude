Sphinx eager ".. only::" directive and other selective rendition extensions
===========================================================================

Project home page: https://github.com/pfalcon/sphinx_selective_exclude

The implementation of ".. only::" directive in Sphinx documentation
generation tool is known to violate principles of least user surprise
and user expectations in general. Instead of excluding content early
in the pipeline (pre-processor style), Sphinx defers exclusion until
output phase, and what's the worst, various stages processing ignore
"only" blocks and their exclusion status, so they may leak unexpected
information into ToC, indexes, etc.

There's multiple issues submitted upstream on this matter:

* https://github.com/sphinx-doc/sphinx/issues/2150
* https://github.com/sphinx-doc/sphinx/issues/1717
* https://github.com/sphinx-doc/sphinx/issues/1488
* etc.

They are largely ignored by Sphinx maintainers.

This projects tries to rectify situation on users' side. It actually
changes the way Sphinx processes "only" directive, but does this
without forking the project, and instead is made as a standard
Sphinx extension, which a user may add to their documentation config.
Unlike normal extensions, extensions provided in this package
monkey-patch Sphinx core to work in a way expected by users.

eager_only
----------

The core extension provided by the package is called `eager_only` and
is based on the idea by Andrea Cassioli (see bugreports above) to
process "only" directive as soon as possible during parsing phase.
This approach has some drawbacks, like producing warnings like
"WARNING: document isn't included in any toctree" if "only" is used
to shape up a toctree, or the fact that changing a documentation
builder (html/latex/etc.) may require complete rebuild of documentation
(if you use "only" conditional on a builder type). But these are minor
issues comparing to completely broken way "only" works in upstream
Sphinx.

Warning: `eager_only` works better with "html" output type. It may not
work well with "latexpdf" output, leading to skippage of various types
of content (this is likely issue with "latexpdf" builder, which can't
handle "only" directives in arbitrary places).

modindex_exclude
----------------

"only" directive allows for fine-grained conditional exclusion, but
sometimes you may want to exclude entire module(s) at once. Even if
you wrap an entire module description in "only" directive, like:

    .. only: option1
        .. module:: my_module
    
        ...

You will still have an HTML page generated, albeit empty. It may also
go into indexes, so will be discoverable by users, leading to less
than ideal experience. `modindex_exclude` extension is design to
resolve this issue, by making sure that any reference of a module
is excluded from Python module index ("modindex"), as well as
general cross-reference index ("genindex"). In the latter case,
any symbol belong to a module will be excluded. Unlike `eager_only`
extension which appear to have issued with "latexpdf" builder,
`modindex_exclude` is useful for PDF, and allows to get cleaner
index for PDF, just the same as for HTML.

Usage
-----

To use these extension, add https://github.com/pfalcon/sphinx_selective_exclude
as a git submodule to your project, in documentation folder (where
Sphinx conf.py is located). Alternatively, commit sphinx_selective_exclude
directory instead of making it a submodule (you will need to pick up
any project updates manually then).

Add following lines to "extensions" settings in your conf.py (you
likely already have some standard Sphinx extensions enabled):

    extensions = [
        ...
        'sphinx_selective_exclude.eager_only',
        'sphinx_selective_exclude.modindex_exclude',
    ]

You may enable both extensions, or one by one. As mentioned above, you
probably don't want to enable `eager_only` if you generate PDF.

These extensions are currently tested to work with Sphinx 1.2.2 and 1.4.2
(latexpdf builder is broken for me in 1.4.2 pristine - it generates PDF
with some sections skipped; enabling `eager_only` in 1.2.2 leads to a
similar behavior).