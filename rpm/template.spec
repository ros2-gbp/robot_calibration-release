%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-robot-calibration
Version:        0.9.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS robot_calibration package

License:        Apache2
URL:            http://ros.org/wiki/robot_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ceres-solver-devel
Requires:       gflags-devel
Requires:       orocos-kdl-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       ros-humble-camera-calibration-parsers
Requires:       ros-humble-control-msgs
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-geometric-shapes
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-kdl-parser
Requires:       ros-humble-moveit-msgs
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-action
Requires:       ros-humble-robot-calibration-msgs
Requires:       ros-humble-rosbag2-cpp
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-tinyxml2-vendor
Requires:       ros-humble-visualization-msgs
Requires:       suitesparse-devel
Requires:       tinyxml2-devel
Requires:       yaml-cpp-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  gflags-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-camera-calibration-parsers
BuildRequires:  ros-humble-control-msgs
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-geometric-shapes
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-kdl-parser
BuildRequires:  ros-humble-moveit-msgs
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-action
BuildRequires:  ros-humble-robot-calibration-msgs
BuildRequires:  ros-humble-rosbag2-cpp
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-tinyxml2-vendor
BuildRequires:  ros-humble-visualization-msgs
BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-launch
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-launch-testing
%endif

%description
Calibrate a Robot

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Fri Nov 08 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.9.2-1
- Autogenerated by Bloom

* Sat Nov 25 2023 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.1-1
- Autogenerated by Bloom

* Sat Jun 25 2022 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.0-1
- Autogenerated by Bloom

