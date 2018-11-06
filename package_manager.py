"""
    Implement specific installation commands for popular Package Managers
    For custom install commands implement install method
"""

class BasePackageManager():
    prefix            = None
    install_command   = None
    uninstall_command = None

    def install(self, package):
        return "{} {} {}".format(self.prefix, self.install_command, package)

    def uninstall(self, package):
        return "{} {} {}".format(self.prefix, self.uninstall_command, package)


class Apt(BasePackageManager):
    prefix            = 'apt-get'
    install_command   = 'install'
    uninstall_command = 'remove'


class Yum(BasePackageManager):
    prefix            = 'yum'
    install_command   = 'install -y'
    uninstall_command = 'erase'


class Dnf(Yum):
    prefix            = 'dnf'


class Pacman(BasePackageManager):
    prefix            = 'pacman'
    install_command   = '-S'
    uninstall_command = '-Rs'


class Homebrew(BasePackageManager):
    prefix            = 'brew'
    install_command   = 'install'
    uninstall_command = 'uninstall'

# TODO
# Implement Snap, Flatpak


