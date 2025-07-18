Summary:	Random signature generator
Summary(pl.UTF-8):	Generator losowych sygnaturek
Name:		signify
Version:	1.07
Release:	3
License:	Public Domain
Group:		Applications/Mail
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/text/%{name}-%{version}.tar.gz
# Source0-md5:	bd80df849f2df0f2ccecbcc171e5f3a3
Patch0:		%{name}-home_etc.patch
BuildArch:	noarch
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Signify is a neat little Perl program that allows a random signature
to be generated from a set of rules. Each section can be one of an
unlimited number of possibilities, each with its own weighting so
those really cool quotes can appear more often than others. Sections
can also be placed next to each other vertically to create columns.
Each section can be formatted independently as left/right/center and
top/bottom/vcenter.

%description -l pl.UTF-8
Signify jest malym programem w Perlu, który pozwala na generowanie
sygnatur za pomocą ustalonych reguł. Każda sekcja może zawierać
nieograniczoną liczbę kombinacji, można ustawić priorytet, które
cytaty mają być częściej wyświetlane od innych. Sekcje mogą być być
formatowane w kolumnach, jak również tekst może być wyrównywany do
lewej/prawej/środka, pionowo do góry/na środku/na dole.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install signify.pl $RPM_BUILD_ROOT%{_bindir}/signify
install signify.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README examples
%attr(755,root,root) %{_bindir}/signify
%{_mandir}/man1/*
