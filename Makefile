# trying to remove the change of `/etc/nix/nix.conf`.
env:
	nix develop --impure --extra-experimental-features nix-command --extra-experimental-features flakes
clean-env:
	rm -rf .venv .devenv

.PHONY: clean-env env
