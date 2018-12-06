#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-MIME-Encodings
Version  : 1.315
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MIME-Encodings-1.315.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MIME-Encodings-1.315.tar.gz
Summary  : 'A unified interface to MIME encoding and decoding'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-MIME-Encodings-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
This archive contains the distribution Email-MIME-Encodings,
version 1.315:
A unified interface to MIME encoding and decoding

%package dev
Summary: dev components for the perl-Email-MIME-Encodings package.
Group: Development
Provides: perl-Email-MIME-Encodings-devel = %{version}-%{release}

%description dev
dev components for the perl-Email-MIME-Encodings package.


%package license
Summary: license components for the perl-Email-MIME-Encodings package.
Group: Default

%description license
license components for the perl-Email-MIME-Encodings package.


%prep
%setup -q -n Email-MIME-Encodings-1.315

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-MIME-Encodings
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-MIME-Encodings/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Email/MIME/Encodings.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::MIME::Encodings.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-MIME-Encodings/LICENSE
