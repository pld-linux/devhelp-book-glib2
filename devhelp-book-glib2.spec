Summary:	DevHelp book: glib 2.0
Summary(pl):	Ksi±¿ka do DevHelpa o glibie 2.0
Name:		devhelp-book-glib2
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/glib-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about glib 2.0.

%description -l pl
Ksi±¿ka do DevHelpa o glibie 2.0.

%prep
%setup -q -c -n glib-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/glib-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/glib-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/glib-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
