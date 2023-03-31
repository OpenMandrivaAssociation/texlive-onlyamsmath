Name:		texlive-onlyamsmath
Version:	42927
Release:	2
Summary:	Inhibit use of non-amsmath mathematics markup when using amsmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/onlyamsmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package inhibits the usage of plain TeX and (on demand) of
standard LaTeX mathematics environments. This is useful for
class writers who want to encourage their users to use the
environments provided by the amsmath package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/onlyamsmath/onlyamsmath.sty
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/ChangeLog
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/Makefile
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/README
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmath-v.tex
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmath.pdf
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmathtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/onlyamsmath/onlyamsmath.dtx
%doc %{_texmfdistdir}/source/latex/onlyamsmath/onlyamsmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
