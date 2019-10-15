cmake_minimum_required(VERSION 3.0)

project(pcd_vis)
find_package(BOOST)

include_directories(${Boost_INCLUDE_DIRS})

find_package(PCL REQUIRED PATHS /usr/local/Cellar/pcl/1.9.1_4)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

find_package(VTK REQUIRED)
include(${VTK_USE_FILE})

add_executable(pcd_vis pcd_vis.cpp)
target_link_libraries(pcd_vis ${PCL_LIBRARIES} ${VTK_LIBRARIES} ${Boost_LIBRARIES})
