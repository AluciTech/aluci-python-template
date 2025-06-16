# Aluci's Python Project Template

## Overview

This repository provides a reusable template for creating python projects that follow Aluci's engineering and documentation standards. It is intended for internal teams and developers who want to quickly set up a new project with a consistent structure and best practices.

## Setup

> [!NOTE]
> To streamline your Python project setup, we've provided a `setup.sh` script that automatically creates a virtual environment and installs all required dependencies. The script supports several command-line options, allowing you to tailor the setup to your specific needs. You can also customize the script itself as needed.
>
> To explore available options, run:
> `./setup.sh --help`
>
> This script has been developed and thoroughly tested on **Ubuntu 22.04 LTS**, **Ubuntu 24.04 LTS**, and **Debian 12.x LTS**. While it may work on other Linux distributions, compatibility is not guaranteed.

### Recommended Setup (using Miniconda)

```bash
./setup.sh --env-name ProjectEnv --python-version 3.10
```

### Venv

```bash
./setup.sh --env-name ProjectEnv --python-version 3.10 --venv
```

## README Template

You can use the following as a starting point for your project's README file. Make sure to fill in the placeholders with relevant information about your project.

````markdown
# Name of the project

In case of early development, please include a warning:

> [!WARNING]
> This project is in early development and is not yet ready for production use.

## Overview

This project is a [brief description of the project]. It aims to [describe the main goal or functionality of the project].

## Setup

### Requirements

If there are any requirements, please list them here.

### Recommended Setup (using Miniconda)

```bash
./setup.sh --env-name MyEnv --python-version 3.10
```

### Venv

```bash
./setup.sh --env-name MyEnv --python-version 3.10 --venv
```

## Usage

Always include a usage section, even if it's just a single command.

## License

This project is licensed under the Apache License (Version 2.0).

See the [LICENSE](LICENSE) file for details.
````

## License

This project is licensed under the Apache License (Version 2.0).

See the [LICENSE](LICENSE) file for details.
