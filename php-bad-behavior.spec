# NOTE
# - the md5 is different in various wp backends, so invoke this to find the most used one and fetchsrc_request several times until distfiles catches the same one:
#   while sleep 1; do rm *.zip; ./md5 bad-behavior.spec; done
Summary:	PHP-based software which blocks automated link spam
Summary(pl.UTF-8):	Oparte na PHP oprogramowanie blokujące spam z automatycznych odnośników
Name:		bad-behavior
Version:	2.0.33
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/%{name}.%{version}.zip
# Source0-md5:	9e084a49f2ddc7d6cd15b497702cec7a
URL:		http://www.bad-behavior.ioerror.us/
BuildRequires:	unzip
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/php/%{name}

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
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a bad-behavior* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{_appdir}
%{_appdir}/bad-behavior
%{_appdir}/bad-behavior-generic.php
%{_appdir}/bad-behavior-lifetype.php
%{_appdir}/bad-behavior-mediawiki.php
%{_appdir}/bad-behavior-wordpress-admin.php
%{_appdir}/bad-behavior-wordpress.php
