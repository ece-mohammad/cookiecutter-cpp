# Target:   {{ cookiecutter.project_name }}_lib
# Type:     Library
file(GLOB SOURCE *.cpp)
add_library({{cookiecutter.project_name}} STATIC ${SOURCE})
target_include_directories({{cookiecutter.project_name}} 
    PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)
install(TARGETS {{cookiecutter.project_name}} EXPORT {{ cookiecutter.project_name }} DESTINATION ${CMAKE_SOURCE_DIR}/lib)
