# revision 25006
# category Package
# catalog-ctan /macros/latex/contrib/onlyamsmath
# catalog-date 2012-01-02 14:24:13 +0100
# catalog-license lppl
# catalog-version 0.10
Name:		texlive-onlyamsmath
Version:	0.10
Release:	4
Summary:	Inhibit use of non-amsmath mathematics markup when using amsmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/onlyamsmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onlyamsmath.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.10-1
+ Revision: 758992
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.04-2
+ Revision: 754549
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.04-1
+ Revision: 719162
- texlive-onlyamsmath
- texlive-onlyamsmath
- texlive-onlyamsmath
- texlive-onlyamsmath

