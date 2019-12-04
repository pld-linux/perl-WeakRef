#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WeakRef
Summary:	WeakRef - an API to the Perl weak references
Summary(pl.UTF-8):	WeakRef - API do perlowych słabych referencji
Name:		perl-WeakRef
Version:	0.01
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/L/LU/LUKKA/%{pdir}-%{version}.tar.gz
# Source0-md5:	3162df7a6eda0dfb44676dd9ebfa3c4c
URL:		http://search.cpan.org/dist/WeakRef/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WeakRef - an API to the Perl weak references.

%description -l pl.UTF-8
WeakRef - API do perlowych słabych referencji.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/WeakRef/
%attr(755,root,root) %{perl_vendorarch}/auto/WeakRef/*.so
%{_mandir}/man3/*
