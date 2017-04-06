%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name conveyorcaaclient

Name:		conveyor-caaclient
Epoch:		1
Version:	XXX
Release:	XXX
Summary:	Python API and CLI for Conveyor-Caa

License:	ASL 2.0
URL:   		https://github.com/Hybrid-Cloud/conveyor-caaclient
Source0:	https://github.com/Hybrid-Cloud/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

%description
Client library (conveyorcaaclient python module) and command line utility
(conveyor Caa) for interacting with Conveyor API.

%package -n python-%{name}
Summary:          Python API and CLI for Conveyor Caa

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  python-d2to1

Requires:       python-babel
Requires:       python-pbr
Requires:       python-requests
Requires:       python-six >= 1.9.0


%description -n python-%{name}
Client library (conveyorcaaclient python module) and command line utility
(conveyor Caa) for interacting with Conveyor API.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Remove bundled egg-info
rm -rf python_conveyorcaaclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%{__python2} setup.py build

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Delete test
rm -fr %{buildroot}%{python-sitelib}/conveyorcaaclient/tests

%files -n python-%{name}
%{python2_sitelib}/conveyorcaaclient
%{python2_sitelib}/*.egg-info


%changelog
