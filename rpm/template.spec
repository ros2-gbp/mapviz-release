%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-mapviz-plugins
Version:        2.4.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mapviz_plugins package

License:        BSD
URL:            https://github.com/swri-robotics/mapviz
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtbase
Requires:       ros-jazzy-ament-index-cpp
Requires:       ros-jazzy-cv-bridge
Requires:       ros-jazzy-gps-msgs
Requires:       ros-jazzy-image-transport
Requires:       ros-jazzy-map-msgs
Requires:       ros-jazzy-mapviz
Requires:       ros-jazzy-marti-common-msgs
Requires:       ros-jazzy-marti-nav-msgs
Requires:       ros-jazzy-marti-sensor-msgs
Requires:       ros-jazzy-marti-visualization-msgs
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-action
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-stereo-msgs
Requires:       ros-jazzy-swri-image-util
Requires:       ros-jazzy-swri-math-util
Requires:       ros-jazzy-swri-route-util
Requires:       ros-jazzy-swri-transform-util
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-index-cpp
BuildRequires:  ros-jazzy-cv-bridge
BuildRequires:  ros-jazzy-gps-msgs
BuildRequires:  ros-jazzy-image-transport
BuildRequires:  ros-jazzy-map-msgs
BuildRequires:  ros-jazzy-mapviz
BuildRequires:  ros-jazzy-marti-common-msgs
BuildRequires:  ros-jazzy-marti-nav-msgs
BuildRequires:  ros-jazzy-marti-sensor-msgs
BuildRequires:  ros-jazzy-marti-visualization-msgs
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-action
BuildRequires:  ros-jazzy-ros-environment
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-stereo-msgs
BuildRequires:  ros-jazzy-swri-image-util
BuildRequires:  ros-jazzy-swri-math-util
BuildRequires:  ros-jazzy-swri-route-util
BuildRequires:  ros-jazzy-swri-transform-util
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Common plugins for the Mapviz visualization tool

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
* Fri Aug 09 2024 Southwest Research Institute <swri-robotics@swri.org> - 2.4.1-1
- Autogenerated by Bloom

* Fri Aug 09 2024 Southwest Research Institute <swri-robotics@swri.org> - 2.4.0-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Southwest Research Institute <swri-robotics@swri.org> - 2.3.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Southwest Research Institute <swri-robotics@swri.org> - 2.3.0-2
- Autogenerated by Bloom

