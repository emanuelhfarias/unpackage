Provision your DEV Environment (packages and dotfiles) easily

Add your favorite tools in `packages.py`

```
class Zsh:
    name = 'zsh'

class Tmux:
    name = 'tmux'
```

It will automatically identify your default package manager and install it.
Just run unpackage from the same directory from `packages.py`

Need to install it from a git repository?

```
class Prezto:
    git = 'github.com/sorin-ionescu/prezto'
```

Don't have git installed? Install it first

```
class Git:
    name = 'git'
```

Install your favorite text editor and copy the dotfiles

```
class NVim:
    name = 'neovim'
    dotfiles = [
        {
            "file": "configs/init.vim",
            "destination": "~/.config/nvim/init.vim"
        }
    ]
```

Want a drink? Install it first, then drink
```
class Brew:
    name = 'homebrew'


class Irssi:
    brew = 'irssi'
```


See my `packages.py` as example.


## TODO
* test it with homebrew

