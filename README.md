# scene_app
Scene API

# Prerequisites
```
- pyenv (install with homebrew)
- poetry (install with homebrew)
- python 3.11.1 (install with pyenv)
```

# Setup
during pyenv installation it should tell you to do this, but add the following to your .zshrc file
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

# Running the app
```
make install
make init-db
make migrate
make run
```
