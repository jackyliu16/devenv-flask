###################
# Nix Instruction #
###################

SHELL := /bin/bash

# Install Single-User Nix into your system
install-nix:
	if ! command -v nix >/dev/null 2>&1; then \
		echo "Installing Nix...";\
		sh <(curl -L https://nixos.org/nix/install) --no-daemon;\
	else \
		echo "You have already installed Nix.";\
	fi
	
	# ref:
	# https://nixos.org/download.html
	# https://www.reddit.com/r/NixOS/comments/wyw7pa/multi_user_vs_single_user_installation/

# Uninstall Single-User Nix 
uninstall-nix:
	@echo "will removing nix single user installing in 5 seconds... <using Ctrl + C to stop it>";
	@sleep 1 && echo "will removing nix single user installing in 4 seconds... <using Ctrl + C to stop it>";
	@sleep 1 && echo "will removing nix single user installing in 3 seconds... <using Ctrl + C to stop it>";
	@sleep 1 && echo "will removing nix single user installing in 2 seconds... <using Ctrl + C to stop it>";
	@sleep 1 && echo "will removing nix single user installing in 1 seconds... <using Ctrl + C to stop it>";
	@for dir in /nix ~/.nix-defexpr ~/.nix-profile ~/.nix-channels; do \
		if [ -d "$$dir" ]; then \
			echo "removing $$dir..."; \
			sudo rm -rf "$$dir"; \
		fi; \
	done
	# ref:
	# https://nixos.org/download.html#nix-install-linux
	# https://github.com/NixOS/nix/pull/8334
monitor:
	 inotifywait --event=create --event=modify --event=moved_to --exclude='/(dev|nix|proc|run|sys|tmp|var)/.*' --monitor --no-dereference --quiet --recursive /

#######################
# general instruction #
#######################

# Running development environment
env:
	nix develop --impure --extra-experimental-features nix-command --extra-experimental-features flakes
	
# (untest) Run background services like mysql
bg:
	ifeq ($(IN_NIX_SHELL),nix-shell)
		@devenv up
	else
		@echo "you should run make env first to make you inside the nix shell environment
	endif
	
# rebuild all environment
clean-env:
	rm -rf .venv .devenv

.PHONY: clean-env env
