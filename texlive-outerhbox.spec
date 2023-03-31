Name:		texlive-outerhbox
Version:	54254
Release:	2
Summary:	Collect horizontal material for contributing to a paragraph
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outerhbox
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outerhbox.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the \outerhbox command, which is similar
to \hbox, except that material is set in outer horizontal mode.
This prevents TeX from optimising away maths penalties and the
like, that are needed when the material is \unhbox'ed.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/outerhbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
