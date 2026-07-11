%global tl_name onlyamsmath
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.20
Release:	%{tl_revision}.1
Summary:	Inhibit use of non-amsmath mathematics markup when using amsmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/onlyamsmath
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package inhibits the usage of plain TeX and (on demand) of standard
LaTeX mathematics environments. This is useful for class writers who
want to encourage their users to use the environments provided by the
amsmath package.

