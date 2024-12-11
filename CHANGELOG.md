# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### [Changed]
* Bump ruff (0.1.14 -> 0.8.2), pytest-ruff (0.2.1 -> 0.4.1), mypy (1.8.0 -> 1.13.0), pytest 7.4.(4 -> 8.3.4). The ruff upgrade changes some rules, and may cause linter failures unless they are corrected.

## [v1.0.0]

### [Fixed]
* For Poetry projects, replace "default" sources with "primary" ones

### [Added]
* Install [poetry-dynamic-versioning](https://pypi.org/project/poetry-dynamic-versioning/) to automatically set package versions based on VCS state
* Install [poethepoet](https://pypi.org/project/poethepoet/) and configure with a job to run [build](https://pypi.org/project/build/) to build source and binary distributions