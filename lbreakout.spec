Summary:	Breakout-style aracade game using SDL
Name:		lbreakout
Version:	001014
Release:	1
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	http://download.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://lgames.sourceforge.net
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_localstatedir	/var

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%prep
%setup -q

%patch0 -p1

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

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
%dir %attr(750,root,games) %{_localstatedir}/games/lbreakout
%attr(664,root,games) %config(noreplace) %verify(not mtime md5 size) %{_localstatedir}/games/lbreakout/highscore
%{_applnkdir}/Games/*
