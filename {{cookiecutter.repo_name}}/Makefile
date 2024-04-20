BUILD_DIR=cmake_build

LIB_DIR=lib

# Build all targets
all: test

test: build
	@cmake --build $(BUILD_DIR) --target test

# Build the documentation (Doxygen)
doc: configure
	@cmake --build $(BUILD_DIR) --target doc

# Build all targets and run the test suite

build: configure
	@cmake --build $(BUILD_DIR) --target all

install: build
	@cmake --build $(BUILD_DIR) --target install

# Configure the targets (CMake)
configure: $(BUILD_DIR) $(LIB_DIR)
	@cmake -S . -B $(BUILD_DIR) -G Ninja -DCMAKE_INSTALL_PREFIX=$(LIB_DIR) -DCMAKE_CXX_COMPILER_LAUNCHER=ccache --fresh

$(BUILD_DIR):
	mkdir -p $@

$(LIB_DIR):
	mkdir -p $@

# Clean the build directory
clean:
	@rm -rf $(BUILD_DIR)

# Format all h,hpp,c,cpp,cxx files under version control inplace
format:
	@ { git diff --name-only --diff-filter=ACMRT; \
	    git diff --name-only --diff-filter=ACRMT --cached; } | \
	  grep -E "\.(c|h|cpp|hpp|cxx)$$" | \
	  xargs -n1 clang-format -i

# Check for formatting violations without fixing
check-format:
	@ ! { git diff --name-only --diff-filter=ACMRT; \
	      git diff --name-only --diff-filter=ACMRT --cached; } | \
	    grep -E "\.(c|h|cpp|hpp|cxx)$$" | \
	    xargs -n1 clang-format -output-replacements-xml | \
	    grep "<replacement " > /dev/null

