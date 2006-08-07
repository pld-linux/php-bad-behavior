Summary:	PHP-based software which blocks automated link spam
Summary(pl):	Oparte na PHP oprogramowanie blokuj±ce spam z automatycznych odno¶ników
Name:		bad-behavior
Version:	2.0.5
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.homelandstupidity.us/download/%{name}-%{version}.zip
# Source0-md5:	55caff35123e8612ae17988d4c14f791
URL:		http://error.wordpress.com/
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

%description -l pl
Bad Behavior to zbiór skryptów PHP zapobiegaj±cy dostêpowi spambotów
do strony poprzez analizê ich ¿±dañ HTTP i porównywanie z profilami
znanych spambotów. Wykracza znacz±co poza User-Agent i Referer. Bad
Behavior jest dostêpny dla kilku opartych na PHP pakietów, mo¿e byæ
tak¿e zintegrowany w krótkim czasie z dowolnym skryptem PHP.

%prep
%setup -qcT -n Bad-Behavior
%{__unzip} -qq -a %{SOURCE0} -d ..
rm -f index.html bad-behavior/index.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a bad-behavior* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_appdir}
