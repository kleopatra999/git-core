Summary:	The stupid content tracker
Summary(pl):	Prymitywne narz�dzie do �ledzenia tre�ci
Name:		git-core
Version:	1.4.2.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
# Source0-md5:	9c8577e2e43fa08d68590928a4112547
URL:		http://git.or.cz/
BuildRequires:	asciidoc
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	xmlto
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"git" can mean anything, depending on your mood.

 - random three-letter combination that is pronounceable, and not
   actually used by any common UNIX command. The fact that it is a
   mispronunciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room.
 - "goddamn idiotic truckload of sh*t": when it breaks

This is a stupid (but extremely fast) directory content manager. It
doesn't do a whole lot, but what it 'does' do is track directory
contents efficiently.

%description -l pl
"git" mo�e oznacza� cokolwiek, w zale�no�ci od nastroju.

- losow� kombinacj� trzech liter, kt�ra jest wymawialna i w�a�ciwie
  nie u�ywana przez �adne popularne polecenie uniksowe. Fakt, �e jest to
  b��dna pisownia s�owa "get" mo�e mie� lub nie mie� znaczenia.
- g�upi, pogardliwy, prosty. Mo�na wybra� ze s�ownika slangu.
- "global information tracker" (narz�dzie do globalnego �ledzenia
  informacji) - je�li jeste�my w dobrym nastroju i git akurat dzia�a.
  Anio�y �piewaj�, a �wiat�o niespodziewanie wype�nia pok�j.
- "goddamn idiotic truckload of sh*t" (przekl�ty idiotyczny �adunek
  g*) - kiedy si� zepsuje.

Jest to prymitywny (ale bardzo szybki) zarz�dca tre�ci s�ownikowej.
Nie robi wiele, ale to, co "robi", to wydajne �ledzenie zawarto�ci
katalogu.

%package devel
Summary:	Header files for git-core
Summary(pl):	Pliki nag��wkowe dla git-core
Group:		Development/Libraries

%description devel
Header files for git-core.

%description devel
Pliki nag��wkowe dla git-core.

%prep
%setup -q -n git-%{version}

%build
%{__make} \
	prefix=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C Documentation

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff

%{__make} install \
	prefix=%{_prefix} \
	CFLAGS="%{rpmcflags}" \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Documentation install \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install xdiff/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Documentation/*.html Documentation/howto Documentation/technical
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
