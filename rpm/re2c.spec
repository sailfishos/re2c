#
# spec file for package re2c
#

Name:           re2c
Version:        1.0.3
Release:        0
Summary:        Tool for generating C-based recognizers from regular expressions
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Url:            http://re2c.org/
Source:         https://github.com/skvadrik/re2c/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         re2c-nogenerationdatedefault.patch
BuildRequires:  bison
BuildRequires:  gcc-c++

%description
re2c is a tool for writing fast and flexible lexers. Unlike other such
tools, it concentrates solely on generating efficient code for matching
regular expressions. This makes it suitable for a wide variety of
applications. The generated scanners approach hand-crafted ones in
terms of size and speed.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
cd re2c
%configure
make %{?_smp_mflags} V=1

%check
make check %{?_smp_mflags}

%install
%make_install

%files
%doc doc/*.ps doc/sample.bib
%doc README
%doc examples/
%{_bindir}/re2c
%{_mandir}/man1/re2c.1%{ext_man}

