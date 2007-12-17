%define realname Catalyst-Plugin-JSONRPC
%define name	perl-%{realname}

%define version	0.01

%define	rel	2
%define release	%mkrel %rel

Summary:	Dispatch JSON-RPC methods with Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl(Catalyst) >= 5.6
BuildRequires:	perl(JSON) >= 1
BuildRequires:	perl(Test::More) >= 0.32
BuildArch:	noarch

%description
Catalyst::Plugin::JSONRPC is a Catalyst plugin to add JSON-RPC methods
in your controller class. It uses the same mechanism that XMLRPC plugin
does and actually plays really nicely.


%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

%clean
rm -rf $RPM_BUILD_ROOT

