%define upstream_name    ORDB-CPAN-Mandriva
%define upstream_version 1.100230

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Orlite for module table in database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ORDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(ORLite::Mirror)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


