#specfile originally created for Fedora, modified for Moblin Linux
Name:           perl-Devel-Symdump
Version:        2.08
Release:        5
Summary:        A Perl module for inspecting Perl's symbol table

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Devel-Symdump/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/Devel-Symdump-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchy within a running program.


%prep
%setup -q -n Devel-Symdump-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/Devel/*
%doc %{_mandir}/man3/*.3pm*


