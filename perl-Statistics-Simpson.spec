#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	Simpson
Summary:	Statistics::Simpson - Simpson index
Summary(pl):	Statistics::Simpson - wska¼nik Simpsona
Name:		perl-Statistics-Simpson
Version:	0.01
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Statistics-Frequency >= 0.03
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Statistics::Simpson module can be used to compute the Simpson
index of data, which measures the variability of data.

%description -l pl
Modu³ Statistics::Simpson mo¿e byæ u¿ywany do liczenia wska¼nika
Simpsona danych, który jest miar± zmienno¶ci danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
