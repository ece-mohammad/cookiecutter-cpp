# Tests for CoarseTimer
file(GLOB SOURCES *.cpp)

add_executable(${PROJECT_NAME}_test ${SOURCES})
target_link_libraries(${PROJECT_NAME}_test ${PROJECT_NAME} libgtest)

# Register the tests
add_test(
  NAME 
  ${PROJECT_NAME}_test
  COMMAND ${PROJECT_NAME}_test
)

