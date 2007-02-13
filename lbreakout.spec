Summary:	Breakout-style aracade game using SDL
Summary(pl.UTF-8):	Gra w stylu Breakout używająca SDL
Name:		lbreakout
Version:	010315
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	0597b94c2c954aa820aa03324a5aaab4
Source1:	%{name}.desktop
Patch0:		%{name}-highscore_dir.patch
Patch1:		%{name}-segv.patch
Patch2:		%{name}-security.patch
URL:		http://lgames.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var

%description
LBreakout is a breakout game with nice graphics, effects and sound.
You can play it either with mouse or keyboard and you can create your
own levels.

%description -l pl.UTF-8
LBreakout to gra breakout z przyjemną grafiką, efektami i dźwiękiem.
Można grać myszą lub klawiaturą oraz tworzyć własne poziomy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_localstatedir}/games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README lbreakout/manual
%attr(2755,root,games) %{_bindir}/lbreakout
%{_datadir}/games/lbreakout
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/games/lbreakout*
%{_desktopdir}/*.desktop
