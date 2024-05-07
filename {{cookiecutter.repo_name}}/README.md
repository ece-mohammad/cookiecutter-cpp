# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}


## Usage


## Build

### Build all targets and run tests

```
make all
```

### Build and run tests

```
make test
```

### Install library

> installed into local subdirectory `./lib`

```
make install
```

### Clean build direcotry

```
make clean
```

## Link into your project

### 1. As a submodule

1. Add as a submodule

```
git submodule add {{cookiecutter.repo_name}} \[path to submodule\]
```

2. In your CMakeLists.txt:

```
add_subdirectory(path to submodule)
```

### 2. As a static library

1. Install libraries into `lib`
2. Either copy files under `lib` directory or point your compiler/linker to the directory

### 3. As source/header files

1. Copy files from `src` and `include` and add them to your project.
2. Build and link your project.

