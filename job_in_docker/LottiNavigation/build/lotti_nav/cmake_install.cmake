# Install script for directory: /home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lotti_nav/srv" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lotti_nav/cmake" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/build/lotti_nav/catkin_generated/installspace/lotti_nav-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/include/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/share/roseus/ros/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/share/common-lisp/ros/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/share/gennodejs/ros/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/lib/python2.7/dist-packages/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/devel/lib/python2.7/dist-packages/lotti_nav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/build/lotti_nav/catkin_generated/installspace/lotti_nav.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lotti_nav/cmake" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/build/lotti_nav/catkin_generated/installspace/lotti_nav-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lotti_nav/cmake" TYPE FILE FILES
    "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/build/lotti_nav/catkin_generated/installspace/lotti_navConfig.cmake"
    "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/build/lotti_nav/catkin_generated/installspace/lotti_navConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lotti_nav" TYPE FILE FILES "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/package.xml")
endif()

