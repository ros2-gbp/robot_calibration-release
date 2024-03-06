%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-robot-calibration
Version:        0.8.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS robot_calibration package

License:        Apache2
URL:            http://ros.org/wiki/robot_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ceres-solver-devel
Requires:       flexiblas-devel
Requires:       gflags-devel
Requires:       orocos-kdl-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       ros-rolling-camera-calibration-parsers
Requires:       ros-rolling-control-msgs
Requires:       ros-rolling-cv-bridge
Requires:       ros-rolling-geometric-shapes
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-kdl-parser
Requires:       ros-rolling-moveit-msgs
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-pluginlib
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-action
Requires:       ros-rolling-robot-calibration-msgs
Requires:       ros-rolling-rosbag2-cpp
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-tf2-geometry-msgs
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-tinyxml2-vendor
Requires:       ros-rolling-visualization-msgs
Requires:       suitesparse-devel
Requires:       tinyxml2-devel
Requires:       yaml-cpp-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gflags-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-camera-calibration-parsers
BuildRequires:  ros-rolling-control-msgs
BuildRequires:  ros-rolling-cv-bridge
BuildRequires:  ros-rolling-geometric-shapes
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-kdl-parser
BuildRequires:  ros-rolling-moveit-msgs
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-pluginlib
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-action
BuildRequires:  ros-rolling-robot-calibration-msgs
BuildRequires:  ros-rolling-rosbag2-cpp
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-tf2-geometry-msgs
BuildRequires:  ros-rolling-tf2-ros
BuildRequires:  ros-rolling-tinyxml2-vendor
BuildRequires:  ros-rolling-visualization-msgs
BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-launch-testing
%endif

%description
Calibrate a Robot

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Mar 06 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.1-2
- Autogenerated by Bloom

