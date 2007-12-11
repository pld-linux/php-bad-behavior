Summary:	PHP-based software which blocks automated link spam
Summary(pl.UTF-8):	Oparte na PHP oprogramowanie blokujące spam z automatycznych odnośników
Name:		bad-behavior
Version:	2.0.11
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.bad-behavior.ioerror.us/download/%{name}-%{version}.zip
# Source0-md5:	8e8578c4e437c9d6e8167c2b43e90776
URL:		http://www.bad-behavior.ioerror.us/
BuildRequires:	unzip
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
%setup -qcT
%{__unzip} -qq -a %{SOURCE0}
cd Bad-Behavior
rm index.html bad-behavior/index.html

%install
rm -rf $RPM_BUILD_ROOT
cd Bad-Behavior
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a bad-behavior* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Bad-Behavior/README.txt
%{_appdir}
