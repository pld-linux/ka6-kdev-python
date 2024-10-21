#
# Conditional build:
%bcond_with	tests		# build with tests

%define		kdeappsver	24.08.2
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdev-python

Summary:	KDE Integrated Development Environment - python
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE - python
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1baa45c856430c8e92c9ae611eb039ca
URL:		http://www.kdevelop.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	ka6-kdevelop-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= 5.78.0
BuildRequires:	kf6-kauth-devel >= 5.105.0
BuildRequires:	kf6-kcodecs-devel >= 5.105.0
BuildRequires:	kf6-kcompletion-devel >= 5.105.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf6-ki18n-devel >= 5.105.0
BuildRequires:	kf6-kitemviews-devel >= 5.105.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.105.0
BuildRequires:	kf6-kparts-devel >= 5.105.0
BuildRequires:	kf6-kservice-devel >= 5.105.0
BuildRequires:	kf6-ktexteditor-devel >= 5.91.0
BuildRequires:	kf6-ktextwidgets-devel >= 5.105.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf6-kxmlgui-devel >= 5.105.0
BuildRequires:	kf6-solid-devel >= 5.105.0
BuildRequires:	kf6-sonnet-devel >= 5.105.0
BuildRequires:	kf6-syntax-highlighting-devel >= 5.105.0
BuildRequires:	kf6-threadweaver-devel >= 5.91.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 3.10
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	ka6-kdevelop
Obsoletes:	ka5-%{kaname} < %{version}
ExcludeArch:	x32 i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Integrated Development Environment - python.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DFORCE_BASH_COMPLETION_INSTALLATION=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdevpythoncompletion.so
%attr(755,root,root) %{_libdir}/libkdevpythonduchain.so
%attr(755,root,root) %{_libdir}/libkdevpythonparser.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevpdb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevpythonlanguagesupport.so
%{_datadir}/kdevappwizard/templates/django_project.tar.bz2
%{_datadir}/kdevappwizard/templates/qtdesigner_app.tar.bz2
%{_datadir}/kdevappwizard/templates/simple_pythonapp.tar.bz2
%{_datadir}/kdevpythonsupport
%{_datadir}/metainfo/org.kde.kdev-python.metainfo.xml
%{_datadir}/qlogging-categories6/kdevpythonsupport.categories
