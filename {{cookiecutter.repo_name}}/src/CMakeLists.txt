# Target:   {{ cookiecutter.project_name }}_lib
# Type:     Library
file(GLOB SOURCE *.cpp)
add_library({{ cookiecutter.project_name }}_lib STATIC ${SOURCE})
target_include_directories({{ cookiecutter.project_name }}_lib 
    PUBLIC 
    ${CMAKE_SOURCE_DIR}/include
)
install(TARGETS {{ cookiecutter.project_name }}_lib EXPORT {{ cookiecutter.project_name }} DESTINATION ${CMAKE_SOURCE_DIR}/lib)
export(TARGETS {{ cookiecutter.project_name }}_lib FILE ${CMAKE_BINARY_DIR}/{{ cookiecutter.project_name }}-config.cmake)
