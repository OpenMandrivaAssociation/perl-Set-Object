%define module	Set-Object
%define name	perl-%{module}
%define version 1.22
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary:	Set of objects and strings in Perl
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Set/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%_tmppath/%{name}-%{release}

%description
This module implements a set of objects, that is, an unordered collection of
objects without duplication.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Set
%{perl_vendorarch}/auto/Set
%{_mandir}/*/*

%clean
rm -rf %buildroot


