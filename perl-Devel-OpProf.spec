%include	/usr/lib/rpm/macros.perl
Summary:	Devel-OpProf perl module
Summary(pl):	Modu³ perla Devel-OpProf
Name:		perl-Devel-OpProf
Version:	0.2
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/DevelOpProf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-OpProf - Profile the internals of a Perl program.

%description -l pl
Modu³ perla Devel-OpProf.

%prep
%setup -q -n DevelOpProf-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Devel/OpProf/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/OpProf
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Devel/OpProf.pm

%dir %{perl_sitearch}/auto/Devel/OpProf
%{perl_sitearch}/auto/Devel/OpProf/.packlist
%{perl_sitearch}/auto/Devel/OpProf/OpProf.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/OpProf/OpProf.so

%{_mandir}/man3/*
