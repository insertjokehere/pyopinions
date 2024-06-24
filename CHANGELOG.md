# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### [Fixed]
* For Poetry projects, replace "default" sources with "primary" ones

### [Added]
* Install [poetry-dynamic-versioning](https://pypi.org/project/poetry-dynamic-versioning/) to automatically set package versions based on VCS state
* Install [poethepoet](https://pypi.org/project/poethepoet/) and configure with a job to run [build](https://pypi.org/project/build/) to build source and binary distributions