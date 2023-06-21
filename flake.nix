{
  description = "Description for the project";

  nixConfig.extra-substituters = "https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/ https://devenv.cachix.org";
  nixConfig.trusted-substituters = "https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/ https://devenv.cachix.org";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    devenv.url = "github:jackyliu16/devenv/stupid";
    nix2container.url = "github:nlewo/nix2container";
    nix2container.inputs.nixpkgs.follows = "nixpkgs";
    mk-shell-bin.url = "github:rrbutani/nix-mk-shell-bin";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.devenv.flakeModule
      ];
      systems = [ "x86_64-linux" "i686-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];

      perSystem = { config, self', inputs', pkgs, system, ... }: {
        # Per-system attributes can be defined here. The self' and inputs'
        # module parameters provide easy access to attributes of the same
        # system.

        # Equivalent to  inputs'.nixpkgs.legacyPackages.hello;
        packages.default = pkgs.hello;

        devenv.shells.default = {
          name = "my-project";

          # https://devenv.sh/reference/options/
          packages = [
            config.packages.default
          ] ++ (with pkgs; [
            stdenv.cc.cc.lib
            bat
            fzf
            ripgrep
          ]);

          pre-commit = {
            hooks = {
              # Automatic Formatter when commit
              markdownlint.enable = true; # markdown
              nixpkgs-fmt.enable = true; # nix
              black.enable = true; # python
            };
            settings = {
              markdownlint.config = pkgs.lib.importJSON ./.markdownlint.json;
            };
          };

          languages.python = {
            enable = true;
            poetry = {
              enable = true;
              install.enable = true; # enable poetry install during devenv initialisation
              activate.enable = true; # activate the poetry virtual environment automatically.
            };
          };

          services.mysql = {
            enable = true;
            package = pkgs.mysql80;
            initialDatabases = [
              { name = "travel"; schema = ./SQL/travel.sql; }
            ];
            settings = {
              mysqld = {
                port = "5001";
              };
            };
          };

          processes = {
            app.exec = ''
              flask --app ./__init__.py run --debug --port 5002
            '';
          };

          env.LD_LIBRARY_PATH = pkgs.lib.mkForce "";
          enterShell = ''
            LD_PRELOAD=${pkgs.stdenv.cc.cc.lib}/lib/
            # LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib/
            FLASK_APP=$(pwd)/__init__.py
            FLASK_DEBUG=1
            # alias helpper
            alias  gc='git commit --verbose'
            alias 'gc!'='git commit --verbose --amend'
            alias  ga='git add'
            alias  gp='git push'
            alias  gpf='git push --force'
            alias  gst="git status"
            alias  gaa='git add --all'
            alias  grh='git reset'
            alias  grhh='git reset --hard'
          '';
        };

      };
      flake = {
        # The usual flake attributes can be defined here, including system-
        # agnostic ones like nixosModule and system-enumerating ones, although
        # those are more easily expressed in perSystem.

      };
    };
}
