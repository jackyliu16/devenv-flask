# Tourism Website

## INSTALL ENVIRONMENT INTO YOUR COMPUTER

Because the concurrent development need of development the project, there is necessary to ensure consistent development environment.
Base on the need of it, our choice to using nix flakes, Devenv and poetry to make sure we could provide consistent development environment.

### Explain for Component

- Nix :Nix is a package manager and operating system configuration tool known for its functional and reproducible approach to software deployment. It uses a declarative language, allowing users to specify dependencies and system configurations precisely. Nix's content-addressable store ensures that different package versions can coexist without conflicts, and it supports atomic upgrades and rollbacks.

- Nix flakes: Nix Flakes is an extension to the Nix package manager that provides a more efficient and reliable way to manage dependencies and configurations. It introduces a new concept called "flakes," which are self-contained and reproducible units of software or system configurations. **Flakes enable declarative and version-controlled management of packages, making it easier to reproduce and share development environments. With Nix Flakes**, we can define your projects and their dependencies in a single file, simplifying the setup process and improving compatibility across [different systems](https://nixos.org/manual/nix/stable/installation/supported-platforms.html), which is need by my team (macOS(intel, m1), linux, WSL).

- Devenv: Devenv.sh provides a convenient and user-friendly platform for creating and managing development environments. It offers a range of tools and configurations tailored to specific programming languages and frameworks. With devenv.sh, developers can easily set up their development environment with just a few clicks, saving them time and effort. The platform also allows for customization and collaboration, enabling developers to share their configurations or collaborate on projects with others. Overall, devenv.sh simplifies the process of setting up and maintaining development environments, making it easier for developers to focus on their code.

- Poetry: a dependency management and packaging tool. It is used for managing project dependencies, creating virtual environments, and generating distribution packages. Poetry simplifies the process of managing project dependencies by automatically resolving package versions and handling their installations. With Poetry, developers can easily manage their project dependencies, ensuring consistent and reproducible environments for their Python projects. It provides a user-friendly command-line interface and integrates well with other popular Python tools and frameworks.

### STEP BY STEP INSTALL AND RUN ENVIRONMENT

1. First, install Nix by [nix-installer](https://github.com/DeterminateSystems/nix-installer) but not the official one, which haven't provided an easy ways to uninstall nix. (if you are using macOS or Pure linux, you just need to use `make install-nix`)

*If you're using WSL and you couldn't install nix correctly (maybe case by systemd wasn't supported or others), you can try to use the installation script in [history version](https://github.com/jackyliu16/devenv-flask/commit/7fbf044a58bb55a299771d0c947268bed7c84303), which is removed because macOS wasn't support single user installation.*
2. Second, restart your terminal, or just run the command it displays.
3. Third, run `make env` to open nix development environment, the fist time you run this command may take 5 or more times, this is depended on your network, it will install about 2G data into `/nix` file.
3. Forty, run `make bg`, it will open two kinds of background services, MYSQL and FLASK.
4. You should be able to using `127.0.0.1:5002` to open the website.

*Note: if you were facing a problem from databases, you can use `make clean` to clean the file generate.*
