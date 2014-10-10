%define upstream_name	 Set-Object
%define upstream_version 1.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Set of objects and strings in Perl
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Set/Set-Object-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

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
%makeinstall_std

%clean

%files
%doc README
%{perl_vendorarch}/Set
%{perl_vendorarch}/auto/Set
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.280.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2011.0
+ Revision: 561041
- update to 1.28

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-2mdv2011.0
+ Revision: 556142
- rebuild for perl 5.12

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 408045
- rebuild using %%perl_convert_version

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2009.1
+ Revision: 330194
- update to new version 1.27

* Sat Oct 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.1
+ Revision: 294833
- update to new version 1.26

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2009.0
+ Revision: 242115
- update to new version 1.25

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 238946
- update to new version 1.24
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.22-2mdv2008.1
+ Revision: 151348
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 97563
- update to new version 1.22


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.21-1mdv2007.0
+ Revision: 131707
- 1.21

* Thu Jan 04 2007 Olivier Thauvin <nanardon@mandriva.org> 1.18-1mdv2007.1
+ Revision: 103940
- 1.18
- 1.17
- Import perl-Set-Object

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2007.0
- New version 1.15
- spec cleanup
- fix directory ownership

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.14-1mdk
- Initial MDV RPM



