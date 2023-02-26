<p align="center">
   <img src="assets/template/python_poetry_template.png" width=100% height=100%>
</p>

<p align="center">
<a href="https://pvanberg.github.io/python-poetry-template/">Documentation</a> | <a href="https://github.com/pvanberg/python-poetry-template/actions"> Github Actions </a>
</p>

## Introduction

<p align="justify">
This template is designed to be used as a starting point for new python projects with support for dockerized development and deployment. This template focuses on standardization (static analysis, code quality) and automation (workflows).
</p>

#### Getting started

- <code>Use this template > Create a new repository</code> : First, you can clone this template from the UI by clicking on the upper left repository button.
- <code>Use this template > Open in codespace</code> : Second, you can directly try it out in Github codespace (build time <= 1.30min). Codespace is a Github feature that allows you to develop directly in the cloud using VSCode devcontainer. For more information, please refer to <a href="https://docs.github.com/en/codespaces">Github Codespace</a>.
- <code>git clone https://github.com/pvanberg/python-poetry-template.git</code> : Third, you can clone this template from the command line. 

#### Installation

Once the project cloned or the codespace ready, you can install the project dependencies. For development, you can use the `dev` extra to install the development dependencies.

```bash
poetry install --with=dev
```
or using pip:
```bash
pip install -e .[dev]
```

#### Features

This template includes the following features:

 - <code>[Poetry](https://python-poetry.org/)</code> - Python dependency management and packaging made easy.
 - <code>[Pre-commit](https://pre-commit.com/)</code> - A framework for managing and maintaining multi-language pre-commit hooks. Supports black, pylint, flake8, isort, mypy and more.
 - <code>[Containers](https://www.docker.com/)</code> - Build, ship, and run any application, anywhere.
 - <code>[Devcontainer](https://code.visualstudio.com/docs/remote/containers)</code> - Develop inside a Docker container while your code runs on the host.
 - <code>[MKDocs](https://www.mkdocs.org/)</code> - Fast, simple and beautiful documentation with Markdown.
 - <code>[Github Pages]()</code> - Publish your project documentation directly from your repository.
 - <code>[Github Actions]()</code> - Automate, customize, and execute your software development workflows right in your repository.

## Configuration

Prior to developement, you should update the following values according to your project. Do not forget to update the `LICENSE.md` file.

<table border="0">

   <tr>
      <th colspan="4">Configuration</th>
   </tr> 
   <tr>
      <th rowspan="2">Parameter</th>
      <th rowspan="2">Value</th>   
      <th colspan="2">References</th>
   </tr> 
   <tr>
      <td><b>Path</b></td>
      <td><b>Variable</b></td>
   </tr>

   <tr>
      <td rowspan="2"><code>AUTHOR_NAME</code></td>
      <td rowspan="2"><i>author</i></td>
      <td>pyproject.toml</td>
      <td>tool.poetry.authors</td>
   </tr>
   <tr>
      <td>mkdocs.yml</td>
      <td>site_author</td>
   </tr>

   <tr>
      <td rowspan="5"><code>PACKAGE_NAME</code></td>
      <td rowspan="5"><i>pypoetry_template</i></td>
      <td>src</td>
      <td>pypoetry_template</td>
   </tr>
   <tr>
      <td>pyproject.toml</td>
      <td>tool.poetry.name</td>
   </tr>
   <tr>
      <td>pyproject.toml</td>
      <td>tool.poetry.package.include</td>
   </tr>
   <tr>
      <td>mkdocs.yml</td>
      <td>repo_name</td>
   </tr>
   <tr>
      <td>mkdocs.yml</td>
      <td>plugins.mkdocstrings.watch</td>
   </tr>

</table>
