# Install script for directory: /home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/src/nav2

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/build/nav2/catkin_generated/installspace/nav2.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav2/cmake" TYPE FILE FILES
    "/home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/build/nav2/catkin_generated/installspace/nav2Config.cmake"
    "/home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/build/nav2/catkin_generated/installspace/nav2Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav2" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_lone/Isaac-Sim-Warehouse/TurtleBotNavigation/lotto_map_ws/src/nav2/package.xml")
endif()

