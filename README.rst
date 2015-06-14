.. image:: https://img.shields.io/pypi/v/turnstile-codevalidator.svg
   :target: https://pypi.python.org/pypi/turnstile-codevalidator/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/l/turnstile-codevalidator.svg
   :target: https://github.com/zalando/turnstile-codevalidator/blob/master/LICENSE
   :alt: License


Turnstile-Codevalidator
=======================

Codevalidator extensions for `turnstile <https://github.com/zalando/turnstile>`_

Check
-----

The `codevalidator` check runs `codevalidator <https://github.com/hjacobs/codevalidator>`_ on added and modified files.

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


License
-------
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
