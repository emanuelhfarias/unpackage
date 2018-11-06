from __future__ import print_function
import inspect
import sys

import packages as pkg
import package_manager
from common import run, get_current_dir


class Unpackage():
    CRED = '\033[91m'
    CSUC = '\033[92m'
    CEND = '\033[0m'

    def __init__(self):
        self.pkg_manager = self._identify_package_manager()

    def install_package(self, name):
        print("Installing {} ...".format(name), end="\r")
        command = self.pkg_manager.install(name)
        output, error = run(command)
        if output and error == '':
            print("{}{} installed successfully{}".format(self.CSUC, name, self.CEND))
        else:
            print("{}Error installing {}".format(self.CRED, name))
            print("\t{}".format(output))
            print("\t{}{}".format(error, self.CEND))
            exit(1)

    def git_clone(self, package):
        destination = "{}/repos/{}".format(
            get_current_dir(), package.__class__.__name__.lower()
        )
        run('mkdir -p ' + destination)
        if 'branch' in dir(package):
            run("git clone {url} --branch {branch} --single-branch {dest}".format(
                url=package.git,
                branch=package.branch,
                dest=destination
            ))
        else:
            run("git clone {url} {dest}".format(package.git, destination))


    def all(self):
        if self.pkg_manager is None:
            print("Missing Package Manager!")
            return

        packages = self._get_packages()
        for package in packages:
            if self._is_packaged_installed(package):
                self._show_already_installed_message(package)
            else:
                if 'name' in dir(package):
                    self.install_package(package.name)
                elif 'git' in dir(package):
                    self.git_clone(package)

            if 'after' in dir(package):
                package.after()

    def _is_packaged_installed(self, package):
        if 'name' in dir(package):
            command = "which {}".format(package.name)
            output, error = run(command)
            return len(output) > 0
        elif package.git:
            return False
        return False

    def _show_already_installed_message(self, package):
        name = package.__class__.__name__
        print("{} already installed.".format(name))

    def _get_packages(self):
        packages = []
        for name, obj in inspect.getmembers(pkg):
            if inspect.isclass(obj):
                packages.append(obj())
        return packages

    def _identify_package_manager(self):
        for name, obj in inspect.getmembers(package_manager):
            if inspect.isclass(obj):
                pkg_manager = obj()
                if pkg_manager.prefix:
                    output, error = run(pkg_manager.prefix)
                    if output:
                        self._install_which(pkg_manager)
                        return pkg_manager

    def _install_which(self, pkg_manager):
        run(pkg_manager.install('which'))

Unpackage().all()

