%include	/usr/lib/rpm/macros.perl
Summary:	The stupid content tracker
Summary(pl):	Prymitywne narz�dzie do �ledzenia tre�ci
Name:		git-core
Version:	1.4.3.4
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
# Source0-md5:	5114c6b58329f3574697a595774df7d0
URL:		http://git.or.cz/
BuildRequires:	asciidoc
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-Error
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	rpm-perlprov >= 4.1-13
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

%package -n perl-Git
Summary:	Perl interface to the Git version control system
Summary(pl):	Perlowy interfejs do systemu kontroli wersji Git
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-git-core

%description -n perl-Git
This module provides Perl scripts easy way to interface the Git
version control system. The modules have an easy and well-tested way
to call arbitrary Git commands; in the future, the interface will also
provide specialized methods for doing easily operations which are not
totally trivial to do over the generic command interface.

%description -n perl-Git -l pl
Ten modu� umo�liwia skryptom Perla wsp�prac� z systemem kontroli
wersji Git. W �atwy i dobrze przetestowany spos�b pozwala wywo�ywa�
dowolne polecenia Gita; w przysz�o�ci interfejs udost�pni tak�e
specjalne metody do �atwego wykonywania operacji nietrywialnych do
wykonania przy u�yciu og�lnego interfejsu polece�.

%prep
%setup -q -n git-%{version}

%build
%{__make} \
	prefix=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

# once again to get perl paths stright
cd perl
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
cd ..

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

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Git/.packlist

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

%files -n perl-Git
%defattr(644,root,root,755)
%{perl_vendorlib}/Git.pm
%{_mandir}/man3/*
