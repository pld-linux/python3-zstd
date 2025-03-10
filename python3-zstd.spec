#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	zstd
Summary:	Simple python bindings to Yann Collet ZSTD compression library
Name:		python3-%{module}
Version:	1.5.1.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zstd/
Source0:	https://files.pythonhosted.org/packages/source/z/zstd/%{module}-%{version}.tar.gz
# Source0-md5:	fe5e894d6925ee1ff13b824eababf13b
Patch0:		unbundle-zstd.patch
URL:		https://pypi.org/project/zstd/
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	zstd-devel
# replace with other requires if defined in setup.py
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple python bindings to Yann Collet ZSTD compression library.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

# Remove bundled lib
%{__rm} -rf zstd

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py3_sitedir}/%{module}*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
