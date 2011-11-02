Name:		texlive-onlyamsmath
Version:	0.04
Release:	1
Summary:	Inhibit use of non-amsmath mathematics markup when using amsmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/onlyamsmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package inhibits the usage of plain TeX and (on demand) of
standard LaTeX mathematics environments. This is useful for
class writers who want to encourage their users to use the
environments provided by the amsmath package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/onlyamsmath/onlyamsmath.sty
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/README
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmath.pdf
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmath.xml
%doc %{_texmfdistdir}/doc/latex/onlyamsmath/onlyamsmathtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/onlyamsmath/Makefile
%doc %{_texmfdistdir}/source/latex/onlyamsmath/onlyamsmath.dtx
%doc %{_texmfdistdir}/source/latex/onlyamsmath/onlyamsmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
