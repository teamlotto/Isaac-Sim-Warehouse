# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "lotti_nav: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(lotti_nav_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_custom_target(_lotti_nav_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lotti_nav" "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(lotti_nav
  "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lotti_nav
)

### Generating Module File
_generate_module_cpp(lotti_nav
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lotti_nav
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(lotti_nav_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(lotti_nav_generate_messages lotti_nav_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_dependencies(lotti_nav_generate_messages_cpp _lotti_nav_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lotti_nav_gencpp)
add_dependencies(lotti_nav_gencpp lotti_nav_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lotti_nav_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(lotti_nav
  "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lotti_nav
)

### Generating Module File
_generate_module_eus(lotti_nav
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lotti_nav
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(lotti_nav_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(lotti_nav_generate_messages lotti_nav_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_dependencies(lotti_nav_generate_messages_eus _lotti_nav_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lotti_nav_geneus)
add_dependencies(lotti_nav_geneus lotti_nav_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lotti_nav_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(lotti_nav
  "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lotti_nav
)

### Generating Module File
_generate_module_lisp(lotti_nav
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lotti_nav
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(lotti_nav_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(lotti_nav_generate_messages lotti_nav_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_dependencies(lotti_nav_generate_messages_lisp _lotti_nav_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lotti_nav_genlisp)
add_dependencies(lotti_nav_genlisp lotti_nav_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lotti_nav_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(lotti_nav
  "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lotti_nav
)

### Generating Module File
_generate_module_nodejs(lotti_nav
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lotti_nav
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(lotti_nav_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(lotti_nav_generate_messages lotti_nav_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_dependencies(lotti_nav_generate_messages_nodejs _lotti_nav_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lotti_nav_gennodejs)
add_dependencies(lotti_nav_gennodejs lotti_nav_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lotti_nav_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(lotti_nav
  "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lotti_nav
)

### Generating Module File
_generate_module_py(lotti_nav
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lotti_nav
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(lotti_nav_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(lotti_nav_generate_messages lotti_nav_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/LottiNavigation/src/lotti_nav/srv/WhereIgo.srv" NAME_WE)
add_dependencies(lotti_nav_generate_messages_py _lotti_nav_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lotti_nav_genpy)
add_dependencies(lotti_nav_genpy lotti_nav_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lotti_nav_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lotti_nav)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lotti_nav
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(lotti_nav_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lotti_nav)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lotti_nav
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(lotti_nav_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lotti_nav)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lotti_nav
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(lotti_nav_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lotti_nav)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lotti_nav
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(lotti_nav_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lotti_nav)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lotti_nav\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lotti_nav
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(lotti_nav_generate_messages_py std_msgs_generate_messages_py)
endif()
