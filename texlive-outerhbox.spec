%global tl_name outerhbox
%global tl_revision 54254

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Collect horizontal material for contributing to a paragraph
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/outerhbox.sty
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outerhbox.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the \outerhbox command, which is similar to \hbox,
except that material is set in outer horizontal mode. This prevents TeX
from optimising away maths penalties and the like, that are needed when
the material is \unhbox'ed.

