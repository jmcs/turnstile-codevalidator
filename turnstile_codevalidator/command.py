# -*- coding: utf-8 -*-

"""
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""

from __future__ import print_function

import subprocess

import click
import pathlib
import turnstile.common.git as git
import turnstile.models.staging as staging

import turnstile_codevalidator.check as check


def copy(src, dst):
    """
    Use cp to copy files and directories from src to destination
    """
    args = ['cp', '-r', str(src), str(dst)]
    subprocess.check_call(args)


def verify_staging_area(repository, codevalidator_rc, fix):
    staging_area = staging.StagingArea(repository)
    with staging_area:
        if staging_area.files:
            output = check.codevalidator(staging_area.files, temporary_dir=staging_area.temporary_directory,
                                         custom_config=codevalidator_rc, fix=fix)
            print(output)
            if output and fix:  # if some files were fixed
                # Copy files to repository
                for file_path in staging_area.temporary_directory.iterdir():
                    copy(file_path, repository.working_dir)
                click.echo("Fixed files copied to the repository.")
                click.secho("The files were not added to the staging area. ", bold=True, nl=False)
                click.echo("Please check the files manually with 'git add'.")
        else:
            click.secho("There are no files in the staging area. ", bold=True, nl=False)
            click.echo("Please check in your files with 'git add'.")


@click.command('codevalidator')
@click.option('--fix', '-f', is_flag=True)
@click.argument('files', nargs=-1, required=False, default=None)
def cmd(fix, files):
    """
    Executes the codevalidator check in the staging area files and optionally tries to fix the files.

    If specific files are provided the version on the working copy will be checked
    """
    repository = git.get_repository()
    codevalidator_rc = pathlib.Path('{}/.codevalidatorrc'.format(repository.working_dir))
    if files:
        output = check.codevalidator(files, custom_config=codevalidator_rc, fix=fix)
        print(output)
    else:
        verify_staging_area(repository, codevalidator_rc, fix)
