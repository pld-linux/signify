Summary:	Random signature generator
Summary(pl):	Generator losowych syngaturek
Name:		signify
Version:	1.05
Release:	1
Copyright:	public domain
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/text/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Signify is a neat little Perl program that allows a random
signature to be generated from a set of rules.  Each section
can be one of an unlimited number of possibilities, each with
its own weighting so those really cool quotes can appear more
often than others.  Sections can also be placed next to each
other vertically to create columns.  Each section can be
formatted independently as left/right/center and
top/bottom/vcenter.

%description -l pl
Signify jest malym programem w Perlu, który pozwala na generowanie
sygnatur za pomoc± ustalonych regu³. Ka¿da sekcja mo¿e zowieraæ
nieograniczon± liczbê kombinacji, mo¿na ustawiæ priorytet, które
cytaty maj± byæ czê¶ciej wy¶wietlane od innych. Sekcje mog± byæ
byæ formatowane w kolumnach, jak równie¿ tekst mo¿e byæ wyrównywany
do lewej/prawej/¶rodka, pionowo do góry/na ¶rodku/na dole.

%prep
%setup -q -n %{name}
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install signify.pl $RPM_BUILD_ROOT/%{_bindir}/signify
install signify.1 $RPM_BUILD_ROOT/%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man1/* \
	examples/* README COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.gz README.gz
%doc examples

%attr(755,root,root) %{_bindir}/signify
%{_mandir}/man1/*
