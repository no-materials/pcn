cmake_minimum_required(VERSION 3.0)

project(mesh_sampling)
find_package(BOOST)

include_directories(${Boost_INCLUDE_DIRS})
#set(Eigen3_USE_STATIC_LIBS ON)
#set(Eigen3_USE_STATIC ON)
#set(Eigen_DIR /usr/local/Cellar/eigen/3.3.7/share/eigen3/cmake)
#find_package(Eigen REQUIRED PATHS /usr/local/Cellar/eigen/3.3.7/share/cmake/Modules/FindEigen3.cmake)



find_package(PCL REQUIRED PATHS /usr/local/Cellar/pcl/1.9.1_4)
#find_package(PCL REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

#find_package(VTK 7.1.1 EXACT REQUIRED PATHS /Users/nomaterials/Documents/Code_Libraries/VTK-7.1.1/VTKBuild)
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})
#include_directories(/usr/local/Cellar/vtk/8.2.0_3/include)
#link_directories(/Users/nomaterials/Documents/Code_Libraries/VTK-7.1.1/VTKBuild/lib)
#${PCL_VTK_COMPONENTS}

add_executable (mesh_sampling mesh_sampling.cpp)
target_link_libraries (mesh_sampling ${PCL_LIBRARIES} ${VTK_LIBRARIES} ${Boost_LIBRARIES})
