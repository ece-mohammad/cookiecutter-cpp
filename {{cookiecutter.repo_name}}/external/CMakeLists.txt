# add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/GTest)
# add_library(libgtest IMPORTED STATIC GLOBAL)
# add_dependencies(libgtest gtest)
# set_property(TARGET libgtest PROPERTY IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/GTest/build/libgtest.a)
include(gtest.cmake)

