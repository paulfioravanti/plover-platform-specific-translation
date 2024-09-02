# Plover Platform Specific Translation

[![Build Status][Build Status image]][Build Status url] [![PyPI - Version][PyPI version image]][PyPI url] [![PyPI - Downloads][PyPI downloads image]][PyPI url] [![linting: pylint][linting image]][linting url]

This [Plover][] [extension][] [plugin][] contains a [meta][] that allows you to
specify different outline translation values depending on what operating system
(platform) you are using.

This can be helpful in times where if you use the same dictionaries with Plover
across, say, Windows and macOS, and want to have a single outline for "copy" to
translate as Control-C on Windows, but Command-C on macOS.

## Install

### Pre-Plover Plugin Registry inclusion (Current)

```console
git clone git@github.com:paulfioravanti/plover-platform-specific-translation.git
cd plover-platform-specific-translation
plover --script plover_plugins install --editable .
```

> Where `plover` in the command is a reference to your locally installed version
> of Plover. See the [Invoke Plover from the command line][] page for details on
> how to create that reference.

Then:

1. When it finishes installing, restart Plover
2. After re-opening Plover, open the Configuration screen (either click the
   Configuration icon, or from the main Plover application menu, select
   `Preferences...`)
3. Open the Plugins tab
4. Check the box next to `plover_platform_specific_translation` to activate the
   plugin

### Post-Plover Plugin Registry inclusion (Future)

1. In the Plover application, open the Plugins Manager (either click the Plugins
   Manager icon, or from the `Tools` menu, select `Plugins Manager`).
2. From the list of plugins, find `plover-platform-specific-translation`
3. Click "Install/Update"
4. When it finishes installing, restart Plover
5. After re-opening Plover, open the Configuration screen (either click the
   Configuration icon, or from the main Plover application menu, select
   `Preferences...`)
6. Open the Plugins tab
7. Check the box next to `plover_platform_specific_translation` to activate the
   plugin

## How To Use

Using the example of an outline for "copy", here are the different ways you can
create a platform-specific translation in your steno dictionaries.

Specify a translation for all possible (and unknown) platforms:

```json
"KP*EU": "{:PLATFORM:WINDOWS:#CONTROL(C):MAC:#SUPER(C):LINUX:#CONTROL(C):OTHER:#CONTROL(C)}"
```

Specify a translation for only some platforms, and provide a default fallback
translation for any other platform:

```json
"KP*EU": "{:PLATFORM:MAC:#SUPER(C):OTHER:#CONTROL(C)}"
```

Specify a translation for only some platforms, but without a fallback for other
platforms (will show an error if current platform is not found, but if you are
confident you know what platforms you work with, this should be fine):

```json
"KP*EU": "{:PLATFORM:WINDOWS:#CONTROL(C):MAC:#SUPER(C)}"
```

Specify only a default fallback for other platforms (pointless, but supported):

```json
"KP*EU": "{:PLATFORM:OTHER:#CONTROL(C)}"
```

Note that the translation values are not limited to keyboard shortcuts, and can
contain [commands][] to run:

```json
"TO*LG": "{:PLATFORM:WINDOWS:PLOVER:TOGGLE_DICT:+win_dict.py:MAC::COMMAND:TOGGLE_DICT:+mac_dict.py}"
```

> Both command prefixes of `{PLOVER:<command>}` and `{:COMMAND:<command>}` are
> supported.

Naturally, plain text output is also supported:

```json
"H-L": "{:PLATFORM:WINDOWS:Hello:MAC:Hi:LINUX:Good day:OTHER:Whassup}"
```

## Configuration

When a platform-specific translation is successfully determined from an outline,
the result is stored in the local [Plover configuration directory][] on your
machine in a file called `platform_specific_translation.json`. This is done in
order to prevent determination actions from being done multiple times for the
same outline, and hence speed up lookups for already known translations.

You should not need to manually add any entries to the configuration, but if you
find any obsolete entries, feel free to delete them.

## Technical Details

The heart of this plugin is essentially [Python][]'s [`platform.system()`][]
function, which will tell you what operating system you are running Plover on.
It will return one of the following values:

- `"Windows"`
- `"Darwin"` (macOS)
- `"Linux"`
- `"Java"` (this looks like a value for [potentially deprecated][] [Jython][]
  environments, in which Plover will very likely never run in, so it is not
  supported in this plugin)
- `""` (unknown platform)

When the extension starts, the value returned from `platform.system()` gets
cached to avoid checking it every time an outline is stroked.

All the platform-specific translations also get cached, so subsequent stroking
of outlines that contain them should feel snappier than the first time they are
used.

Pressing the "Disconnect and reconnect the machine" button on the Plover UI
resets the translation cache. If you make any changes to a specific
platform-specific translation in an outline, make sure to press it so it can
be re-read in again properly.

## Development

Clone from GitHub with [git][]:

```console
git clone git@github.com:paulfioravanti/plover-platform-specific-translation.git
cd plover-platform-specific-translation
python -m pip install --editable ".[test]"
```

If you are a [Tmuxinator][] user, you may find my
[plover_platform_specific_translation project file][] of reference.

### Python Version

Plover's Python environment currently uses version 3.9 (see Plover's
[`workflow_context.yml`][] to confirm the current version).

So, in order to avoid unexpected issues, use your runtime version manager to
make sure your local development environment also uses Python 3.9.x.

### Testing

- [Pytest][] is used for testing in this plugin.
- [Coverage.py][] and [pytest-cov][] are used for test coverage, and to run
  coverage within Pytest
- [Pylint][] is used for code quality
- [Mypy][] is used for static type checking

Currently, the only parts able to be tested are ones that do not rely directly
on Plover.

Run tests, coverage, and linting with the following commands:

```console
pytest --cov --cov-report=term-missing
pylint plover_local_env_var
mypy plover_local_env_var
```

To get a HTML test coverage report:

```console
coverage run --module pytest
coverage html
open htmlcov/index.html
```

If you are a [`just`][] user, you may find the [`justfile`][] useful during
development in running multiple test commands. You can run the following command
from the project root directory:

```console
just --working-directory . --justfile test/justfile
```

### Deploying Changes

After making any code changes, deploy the plugin into Plover with the following
command:

```console
plover --script plover_plugins install --editable .
```

> Where `plover` in the command is a reference to your locally installed version
> of Plover. See the [Invoke Plover from the command line][] page for details on
> how to create that reference.

When necessary, the plugin can be uninstalled via the command line with the
following command:

```console
plover --script plover_plugins uninstall plover-platform-specific-translation
```

[Build Status image]: https://github.com/paulfioravanti/plover-platform-specific-translation/actions/workflows/ci.yml/badge.svg
[Build Status url]: https://github.com/paulfioravanti/plover-platform-specific-translation/actions/workflows/ci.yml
[commands]: https://plover.readthedocs.io/en/latest/plugin-dev/commands.html
[Coverage.py]: https://github.com/nedbat/coveragepy
[extension]: https://plover.readthedocs.io/en/latest/plugin-dev/extensions.html
[git]: https://git-scm.com/
[Invoke Plover from the command line]: https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line
[`just`]: https://github.com/casey/just
[`justfile`]: ./test/justfile
[Jython]: https://www.jython.org/
[linting image]: https://img.shields.io/badge/linting-pylint-yellowgreen
[linting url]: https://github.com/pylint-dev/pylint
[meta]: https://plover.readthedocs.io/en/latest/plugin-dev/metas.html
[my steno dictionaries]: https://github.com/paulfioravanti/steno-dictionaries
[Mypy]: https://github.com/python/mypy
[`platform.system()`]: https://docs.python.org/3/library/platform.html#platform.system
[Plover]: https://www.openstenoproject.org/
[Plover configuration directory]: https://plover.readthedocs.io/en/latest/api/oslayer_config.html#plover.oslayer.config.CONFIG_DIR
[plover_platform_specific_translation project file]: https://github.com/paulfioravanti/dotfiles/blob/master/tmuxinator/plover_platform_specific_translation.yml
[plugin]: https://plover.readthedocs.io/en/latest/plugins.html#types-of-plugins
[potentially deprecated]: https://discuss.python.org/t/lets-deprecate-platform-system-java/48026/4
[Pylint]: https://github.com/pylint-dev/pylint
[PyPI downloads image]:https://img.shields.io/pypi/dm/plover-platform-specific-translation
[PyPI version image]: https://img.shields.io/pypi/v/plover-platform-specific-translation
[PyPI url]: https://pypi.org/project/plover-platform-specific-translation/
[Pytest]: https://pytest.org/
[pytest-cov]: https://github.com/pytest-dev/pytest-cov/
[Python]: https://www.python.org/
[Tmuxinator]: https://github.com/tmuxinator/tmuxinator
[`workflow_context.yml`]: https://github.com/openstenoproject/plover/blob/master/.github/workflows/ci/workflow_context.yml
