%include	/usr/lib/rpm/macros.perl
Summary:	Devel::OpProf perl module
Summary(pl):	Modu³ perla Devel::OpProf
Name:		perl-Devel-OpProf
Version:	0.2
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/DevelOpProf-%{version}.tar.gz
# Source0-md5:	c53887871b7a73ad824b7b4cc1db4211
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::OpProf - Profile the internals of a Perl program.

%description -l pl
Modu³ perla Devel::OpProf.

%prep
%setup -q -n DevelOpProf-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Devel/OpProf.pm
%dir %{perl_vendorarch}/auto/Devel/OpProf
%{perl_vendorarch}/auto/Devel/OpProf/OpProf.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/OpProf/OpProf.so
%{_mandir}/man3/*
