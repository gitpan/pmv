%define modname pmv
%define modversion 0.03

Name: %modname
Version: %modversion
Release: 1
Source: http://www.cpan.org/authors/id/JV/%{name}-%{version}.tar.gz
BuildArch: noarch
Provides: %modname = %version
URL: http://www.squirrel.nl/people/jvromans/
BuildRoot: %{_tmppath}/rpm-buildroot-%{name}-%{version}-%{release}
Prefix: %{_prefix}

Summary: Rename files using Perl power
License: Artistic
Group: Applications/Productivity

%description
With pmv you can rename files using the power of Perl expressions.

%prep
%setup -q

%build
perl Makefile.PL
make all test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f ${RPM_BUILD_ROOT}%{_libdir}/perl*/*/*/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README

%{_bindir}/pmv
%{_libdir}/perl5/site_perl/*/*/auto/pmv
%{_libdir}/perl5/site_perl/*/File/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2005 Johan Vromans <jvromans@squirrel.nl>
- Initial version.
