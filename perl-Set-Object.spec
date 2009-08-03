%define upstream_name	 Set-Object
%define upstream_version 1.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Set of objects and strings in Perl
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
Buildroot:	%_tmppath/%{name}-%{version}-%{release}

%description
This module implements a set of objects, that is, an unordered collection of
objects without duplication.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# should not have been included
# http://rt.cpan.org/Ticket/Display.html?id=37799
rm -f t/misc/threads.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Set
%{perl_vendorarch}/auto/Set
%{_mandir}/*/*
