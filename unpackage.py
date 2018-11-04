import inspect
import sys

import packages as pkg
import package_manager
from common import run, get_current_dir


class Unpackage():

    def install_package(self, name):
        pkg_manager = self._identify_package_manager()
        if pkg_manager:
            command = pkg_manager.install(name)
            output, error = run(command)
        else:
            print("Missing Package Manager!")

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
                output, error = run("which {}".format(pkg_manager.prefix))
                if output:
                    return pkg_manager

Unpackage().all()

