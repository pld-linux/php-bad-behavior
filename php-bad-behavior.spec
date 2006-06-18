Summary:	PHP-based software which blocks automated link spam
Name:		bad-behavior
Version:	1.2.4
Release:	0.7
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.homelandstupidity.us/download/%{name}-%{version}.zip
# Source0-md5:	2f7db82336542af415d59d7b0a52687f
URL:		http://www.homelandstupidity.us/software/bad-behavior/
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

%prep
%setup -qcT -n %{name}
%{__unzip} -qq -a %{SOURCE0} -d ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a *.php $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_appdir}
