#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	Simpson
Summary:	Statistics::Simpson - Simpson index
Summary(pl):	Statistics::Simpson - wska�nik Simpsona
Name:		perl-Statistics-Simpson
Version:	0.01
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a60893a4efc2023d35eece27b1ab6aa8
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
BuildRequires:	perl-Statistics-Frequency >= 0.03
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Statistics::Simpson module can be used to compute the Simpson
index of data, which measures the variability of data.

%description -l pl
Modu� Statistics::Simpson mo�e by� u�ywany do liczenia wska�nika
Simpsona danych, kt�ry jest miar� zmienno�ci danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
