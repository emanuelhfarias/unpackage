from common import run


class Git():
    name = 'git'


class XClip():
    name = 'xclip'


class NVim():
    name = 'neovim'


class Zsh():
    name     = 'zsh'
    dotfiles = [
        {"file": ".zshrc", "destination": "~/"},
    ]

    def after(self):
        self.change_user_shell()

    def change_user_shell(self):
        run('chsh -s `which zsh` `whoami`')


class Prezto():
    git = 'https://github.com/emanuelhfarias/prezto.git'
    branch = 'manolos-prezto'


class Tmux():
    name     = 'tmux'
    dotfiles = [
        {"file": ".zshrc", "destination": "~/"}
    ]

