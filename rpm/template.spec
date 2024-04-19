%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-robot-calibration
Version:        0.8.1
Release:        3%{?dist}%{?release_suffix}
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
Requires:       ros-jazzy-camera-calibration-parsers
Requires:       ros-jazzy-control-msgs
Requires:       ros-jazzy-cv-bridge
Requires:       ros-jazzy-geometric-shapes
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-kdl-parser
Requires:       ros-jazzy-moveit-msgs
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-action
Requires:       ros-jazzy-robot-calibration-msgs
Requires:       ros-jazzy-rosbag2-cpp
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-tf2-ros
Requires:       ros-jazzy-tinyxml2-vendor
Requires:       ros-jazzy-visualization-msgs
Requires:       suitesparse-devel
Requires:       tinyxml2-devel
Requires:       yaml-cpp-devel
Requires:       ros-jazzy-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gflags-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-camera-calibration-parsers
BuildRequires:  ros-jazzy-control-msgs
BuildRequires:  ros-jazzy-cv-bridge
BuildRequires:  ros-jazzy-geometric-shapes
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-kdl-parser
BuildRequires:  ros-jazzy-moveit-msgs
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-action
BuildRequires:  ros-jazzy-robot-calibration-msgs
BuildRequires:  ros-jazzy-rosbag2-cpp
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  ros-jazzy-tinyxml2-vendor
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-launch
BuildRequires:  ros-jazzy-launch-ros
BuildRequires:  ros-jazzy-launch-testing
%endif

%description
Calibrate a Robot

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Fri Apr 19 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.1-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.1-2
- Autogenerated by Bloom

