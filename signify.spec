Summary:	Random signature generator
Summary(pl):	Generator losowych sygnaturek
Name:		signify
Version:	1.07
Release:	2
License:	Public Domain
Group:		Applications/Mail
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/text/%{name}-%{version}.tar.gz
Patch0:		%{name}-home_etc.patch
BuildArch:	noarch
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Signify is a neat little Perl program that allows a random signature
to be generated from a set of rules. Each section can be one of an
unlimited number of possibilities, each with its own weighting so
those really cool quotes can appear more often than others. Sections
can also be placed next to each other vertically to create columns.
Each section can be formatted independently as left/right/center and
top/bottom/vcenter.

%description -l pl
Signify jest malym programem w Perlu, który pozwala na generowanie
sygnatur za pomoc± ustalonych regu³. Ka¿da sekcja mo¿e zowieraæ
nieograniczon± liczbê kombinacji, mo¿na ustawiæ priorytet, które
cytaty maj± byæ czê¶ciej wy¶wietlane od innych. Sekcje mog± byæ byæ
formatowane w kolumnach, jak równie¿ tekst mo¿e byæ wyrównywany do
lewej/prawej/¶rodka, pionowo do góry/na ¶rodku/na dole.

%prep
%setup -q -n %{name}
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install signify.pl $RPM_BUILD_ROOT/%{_bindir}/signify
install signify.1 $RPM_BUILD_ROOT/%{_mandir}/man1

gzip -9nf examples/* README COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.gz README.gz
%doc examples

%attr(755,root,root) %{_bindir}/signify
%{_mandir}/man1/*
