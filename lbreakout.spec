Summary:	Breakout-style aracade game using SDL
Summary(pl):	Gra w stylu Breakout u¿ywaj±ca SDL
Name:		lbreakout
Version:	001104
Release:	3
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-highscore_dir.patch
URL:		http://lgames.sourceforge.net
BuildRequires:	SDL-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_localstatedir	/var

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl
LBreakout to gra breakout z przyjemn± grafik±, efektami i d¼wiêkiem.
Mo¿na graæ mysz± lub klawiatur± oraz tworzyæ w³asne poziomy.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_localstatedir}/games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lbreakout/manual 
%attr(2755,root,games) %{_bindir}/lbreakout
%{_datadir}/games/lbreakout 
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) %{_localstatedir}/games/lbreakout*
%{_applnkdir}/Games/*
