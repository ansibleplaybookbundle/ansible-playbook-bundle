%if 0%{?fedora}
%global use_python3 1
%global use_python2 0
%global pythonbin %{__python3}
%global python_sitelib %{python3_sitelib}
%else
%global use_python3 0
%global use_python2 1
%if 0%{?__python2:1}
%global pythonbin %{__python2}
%global python_sitelib %{python2_sitelib}
%else
%global pythonbin %{__python}
%global python_sitelib %{python_sitelib}
%endif
%endif
%{!?python_sitelib: %define python_sitelib %(%{pythonbin} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: ansibleapp
Version: 0.1.0
Release: 1%{?dist}
Summary: A lightweight application definition (meta-containers)

Group: Development/Tools
License: GPLv2
URL: https://github.com/fusor/ansible-service-broker
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
%if %{use_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
Requires: python3-PyYAML
%else
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-pip
Requires: PyYAML
%endif


%description
AnsibleApp is a lightweight application definition (meta-containers). AnsibleApp
has the following features:

%prep
%setup -q -n %{name}-%{version}

%build
%{pythonbin} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{pythonbin} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/ansibleapp
%dir %{python_sitelib}/ansibleapp
%{python_sitelib}/ansibleapp/*
%{python_sitelib}/ansibleapp-*.egg-info


%changelog
