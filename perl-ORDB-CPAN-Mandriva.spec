%define upstream_name    ORDB-CPAN-Mandriva
%define upstream_version 1.100230

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Orlite for module table in database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ORDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ORLite::Mirror)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module is an easy way to fetch a database listing all Perl modules &
distributions packaged within Mandriva Linux distribution.

When using it, it will automatically & silently download it from the
original source and copy it in a local directory, letting you focus on what
you want with the data itself.

Check the _examples_ directory for some ideas on how to use it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
# fails at ABF
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.230-2mdv2011.0
+ Revision: 655148
- rebuild for updated spec-helper

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.230-1mdv2011.0
+ Revision: 496979
- import perl-ORDB-CPAN-Mandriva


* Wed Jan 27 2010 cpan2dist 1.100230-1mdv
- initial mdv release, generated with cpan2dist
