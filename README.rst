Turnstile-Codevalidator
=======================

Check
-----

The `codevalidator` check runs [codevalidator](https://github.com/hjacobs/codevalidator) on added and modified files.

By default this check uses your general codevalidator configuration, but you can also provide a custom codevalidatorc by
adding it as `.codevalidatorc` to your repository root.


Command
-------
To check if staged files follow the codevalidator rules do:

    $ turnstile codevalidator

If you want codevalidator to try to fix the code style do:

    $ turnstile codevalidator --fix

Please note that any change will be left unstaged and need to be added with `git add` and any **unstaged change to
staged files will be overwritten**.
