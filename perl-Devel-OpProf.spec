%include	/usr/lib/rpm/macros.perl
Summary:	Devel-OpProf perl module
Summary(pl):	Modu³ perla Devel-OpProf
Name:		perl-Devel-OpProf
Version:	0.2
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/DevelOpProf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-OpProf - Profile the internals of a Perl program.

%description -l pl
Modu³ perla Devel-OpProf.

%prep
%setup -q -n DevelOpProf-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Devel/OpProf.pm
%dir %{perl_sitearch}/auto/Devel/OpProf
%{perl_sitearch}/auto/Devel/OpProf/OpProf.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/OpProf/OpProf.so
%{_mandir}/man3/*
