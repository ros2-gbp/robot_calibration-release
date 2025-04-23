%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

%global __cmake_in_source_build 1

Name:           ros-kilted-robot-calibration
Version:        0.10.0
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
Requires:       ros-kilted-camera-calibration-parsers
Requires:       ros-kilted-control-msgs
Requires:       ros-kilted-cv-bridge
Requires:       ros-kilted-geometric-shapes
Requires:       ros-kilted-geometry-msgs
Requires:       ros-kilted-kdl-parser
Requires:       ros-kilted-moveit-msgs
Requires:       ros-kilted-nav-msgs
Requires:       ros-kilted-pluginlib
Requires:       ros-kilted-rclcpp
Requires:       ros-kilted-rclcpp-action
Requires:       ros-kilted-robot-calibration-msgs
Requires:       ros-kilted-rosbag2-cpp
Requires:       ros-kilted-sensor-msgs
Requires:       ros-kilted-std-msgs
Requires:       ros-kilted-tf2-geometry-msgs
Requires:       ros-kilted-tf2-ros
Requires:       ros-kilted-tinyxml2-vendor
Requires:       ros-kilted-visualization-msgs
Requires:       suitesparse-devel
Requires:       tinyxml2-devel
Requires:       yaml-cpp-devel
Requires:       ros-kilted-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gflags-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-kilted-ament-cmake
BuildRequires:  ros-kilted-camera-calibration-parsers
BuildRequires:  ros-kilted-control-msgs
BuildRequires:  ros-kilted-cv-bridge
BuildRequires:  ros-kilted-geometric-shapes
BuildRequires:  ros-kilted-geometry-msgs
BuildRequires:  ros-kilted-kdl-parser
BuildRequires:  ros-kilted-moveit-msgs
BuildRequires:  ros-kilted-nav-msgs
BuildRequires:  ros-kilted-pluginlib
BuildRequires:  ros-kilted-rclcpp
BuildRequires:  ros-kilted-rclcpp-action
BuildRequires:  ros-kilted-robot-calibration-msgs
BuildRequires:  ros-kilted-rosbag2-cpp
BuildRequires:  ros-kilted-sensor-msgs
BuildRequires:  ros-kilted-std-msgs
BuildRequires:  ros-kilted-tf2-geometry-msgs
BuildRequires:  ros-kilted-tf2-ros
BuildRequires:  ros-kilted-tinyxml2-vendor
BuildRequires:  ros-kilted-visualization-msgs
BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-kilted-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-kilted-ament-cmake-gtest
BuildRequires:  ros-kilted-launch
BuildRequires:  ros-kilted-launch-ros
BuildRequires:  ros-kilted-launch-testing
%endif

%description
Calibrate a Robot

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
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
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Tue Apr 22 2025 Michael Ferguson <mike@vanadiumlabs.com> - 0.10.0-2
- Autogenerated by Bloom

* Thu Dec 12 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.10.0-1
- Autogenerated by Bloom

* Tue Dec 03 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.9.3-1
- Autogenerated by Bloom

* Fri Nov 08 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.9.2-1
- Autogenerated by Bloom

* Thu Sep 26 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.9.1-1
- Autogenerated by Bloom

* Tue Apr 23 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.9.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Michael Ferguson <mike@vanadiumlabs.com> - 0.8.1-2
- Autogenerated by Bloom

