#specfile originally created for Fedora, modified for Moblin Linux
Name:           perl-Devel-Symdump
Version:        2.08
Release:        5
Summary:        A Perl module for inspecting Perl's symbol table

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Devel-Symdump/
Source0:        %{name}-%{version}.tar.gz
Source1001: packaging/perl-Devel-Symdump.manifest 

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchy within a running program.


%prep
%setup -q

%build
cp %{SOURCE1001} .
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%manifest perl-Devel-Symdump.manifest
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/Devel/*
%ifarch %{arm}
%{_mandir}/man3/*.3pm*
%endif
