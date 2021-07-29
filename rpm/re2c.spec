Name:           re2c
Summary:        Tool for generating C, C++ recognizers from regular expressions
Version:        2.0.3
Release:        1
License:        Public Domain
Url:            http://re2c.org/
Source:         %{name}-%{version}.tar.bz2
Patch0:         re2c-nogenerationdatedefault.patch
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel

%description
re2c is a tool for writing very fast and very flexible scanners. Unlike any
other such tool, re2c focuses on generating high efficient code for regular
expression matching. As a result this allows a much broader range of use than
any traditional lexer offers. And Last but not least re2c generates warning
free code that is equal to hand-written code in terms of size, speed and
quality.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-docs --disable-libs --disable-golang
%make_build

%check
make check %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/re2c
%{_datadir}/re2c/
%{_mandir}/man1/re2c.1*
