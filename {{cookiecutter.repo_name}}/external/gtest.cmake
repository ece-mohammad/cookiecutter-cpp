# GoogleTest (gtest)
# A unit testing library for C/C++
# Creates a libgtest target packaged with the required include driectories
find_package(Threads REQUIRED)

# Fetch GoogleTest remotely
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/GTest)
add_library(libgtest ALIAS gtest)
add_library(libgmock ALIAS gmock)

