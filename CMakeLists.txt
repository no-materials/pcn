cmake_minimum_required(VERSION 3.0)
project(pcn_root)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

#set(PROJECT_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)

#include_directories("${PROJECT_INCLUDE_DIR}")
#include_directories("${PROJECT_SOURCE_DIR}")

add_subdirectory(sample)
add_subdirectory(vis)