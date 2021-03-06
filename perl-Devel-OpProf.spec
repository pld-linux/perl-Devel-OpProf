Summary:	Devel::OpProf - profile the internals of a Perl program
Summary(pl.UTF-8):	Devel::OpProf - dostrojenie wewnętrznych parametrów programu w Perlu
Name:		perl-Devel-OpProf
Version:	0.2
Release:	8
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/DevelOpProf-%{version}.tar.gz
# Source0-md5:	c53887871b7a73ad824b7b4cc1db4211
URL:		http://search.cpan.org/dist/DevelOpProf/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::OpProf module lets perl keep a count of each internal
operation in a program so that you can profile your Perl code.

%description -l pl.UTF-8
Moduł Devel::OpProf umożliwia perlowi zliczanie wszystkich
wewnętrznych operacji w programie w celu dostrojenia kodu w Perlu.

%prep
%setup -q -n DevelOpProf-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Devel/OpProf.pm
%dir %{perl_vendorarch}/auto/Devel/OpProf
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/OpProf/OpProf.so
%{_mandir}/man3/*
