# NOTE
# - the md5 is different in various wp backends, so invoke packages/fetchsrc_request
#   several times until distfiles catches the same one you downloaded.
Summary:	PHP-based software which blocks automated link spam
Summary(pl.UTF-8):	Oparte na PHP oprogramowanie blokujące spam z automatycznych odnośników
Name:		php-bad-behavior
Version:	2.0.36
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/bad-behavior.%{version}.zip
# Source0-md5:	c6602c5d9107dd17ee0b60cf31f35f9b
URL:		http://www.bad-behavior.ioerror.us/
BuildRequires:	unzip
Requires:	php-common
Obsoletes:	bad-behavior
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/bad-behavior

%description
Bad Behavior is a set of PHP scripts which prevents spambots from
accessing your site by analyzing their actual HTTP requests and
comparing them to profiles from known spambots. It goes far beyond
User-Agent and Referer, however. Bad Behavior is available for several
PHP-based software packages, and also can be integrated in seconds
into any PHP script.

%description -l pl.UTF-8
Bad Behavior to zbiór skryptów PHP zapobiegający dostępowi spambotów
do strony poprzez analizę ich żądań HTTP i porównywanie z profilami
znanych spambotów. Wykracza znacząco poza User-Agent i Referer. Bad
Behavior jest dostępny dla kilku opartych na PHP pakietów, może być
także zintegrowany w krótkim czasie z dowolnym skryptem PHP.

%prep
# unpack in ascii mode
%define __unzip /usr/bin/unzip -a
%setup -qc
mv {,.}bad-behavior
mv .bad-behavior/* .
rm index.html bad-behavior/index.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a bad-behavior* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{php_data_dir}/bad-behavior
%{php_data_dir}/bad-behavior-generic.php
%{php_data_dir}/bad-behavior-lifetype.php
%{php_data_dir}/bad-behavior-mediawiki.php
%{php_data_dir}/bad-behavior-wordpress-admin.php
%{php_data_dir}/bad-behavior-wordpress.php
