## Project structure

<p align="justify">
This template is not intended to be a one-size-fits-all solution. It is designed to be a starting point for new dockerized python projects. It is up to you to decide which features you want to keep and which ones you want to remove. The goal is to provide a starting point that is easy to use and that can be easily adapted to your needs.
</p>

> Optional directory can be safely removed if you do not need them.

| Directory | Status | Description |
| --- | --- | --- |
| `.devcontainer` | Optional| Devcontainer is a VSCode feature that allows you to develop inside a Docker container while your code runs on the host. For more information, please refer to <a href="https://code.visualstudio.com/docs/remote/containers">VSCode documentation</a>. |
| `.github` | Optional| Github configuration, primary for actions is a feature that allows you to automate, customize, and execute your software development workflows right in your repository. For more information, please refer to <a href="https://docs.github.com/en/actions">Github documentation</a>. |
| `assets` | Optional| Assets are used to store additional files that are used within your project. </br> e.g. configuration files, images, etc. |
| `dockers` | Required | This template is designed with support for multi-containers applications. For this reason, the conventional root `dockerfile` is moved within a hierarichal structure. Such hierarchical pattern allow, the application to preserve consistency through docker composition paths. e.g. </br><code> dockers/dev/dockerfile</code></br><code>dockers/webapp/dockerfile</code>|
| `docs` | Optional| The docs directory contains everything related to the documentation of your project. It contains the documention styles, assets and pages which will be orchestrated by the `mkdocs.yml` configuration.|
| `lib` | Optional| Some projects require external library to be imported. While it is usually a bad practice, to directly include library sources in your project, some specific use cases require to directly embedes the library within the codebase. |
| `notebooks` | Optional| The notebooks directory contains all the Jupyter notebooks that are used to develop your project. |
| `scripts` | Optional| The scripts directory contains all the scripts that are used to develop your project. |
| `src` | Required | The src directory contains all the source code of your project. The source super structure, while note being mandatory, offers a clear separation between the source code and the rest of the project. |
| `tests` | Required | The tests directory contains all the tests of your project and should follow the same hierachical structure than the `src` directory. |
