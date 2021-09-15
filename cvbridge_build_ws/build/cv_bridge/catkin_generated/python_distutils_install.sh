#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/root/cvbridge_build_ws/src/vision_opencv/cv_bridge"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/root/cvbridge_build_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/root/cvbridge_build_ws/install/lib/python3/dist-packages:/root/cvbridge_build_ws/build/cv_bridge/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/root/cvbridge_build_ws/build/cv_bridge" \
    "/usr/bin/python3" \
    "/root/cvbridge_build_ws/src/vision_opencv/cv_bridge/setup.py" \
    egg_info --egg-base /root/cvbridge_build_ws/build/cv_bridge \
    build --build-base "/root/cvbridge_build_ws/build/cv_bridge" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/root/cvbridge_build_ws/install" --install-scripts="/root/cvbridge_build_ws/install/bin"
