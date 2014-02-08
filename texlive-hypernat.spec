# revision 17358
# category Package
# catalog-ctan /macros/latex/contrib/hypernat
# catalog-date 2010-03-08 12:29:56 +0100
# catalog-license gpl
# catalog-version 1.0b
Name:		texlive-hypernat
Version:	1.0b
Release:	3
Summary:	Allow hyperref and natbib to work together
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypernat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows hyperref package and the natbib package with options
'numbers' and 'sort&compress' to work together. This means that
multiple sequential citations (e.g [3,2,1]) will be compressed
to [1-3], where the '1' and the '3' are (color-)linked to the
bibliography.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hypernat/hypernat.sty
%doc %{_texmfdistdir}/doc/latex/hypernat/hypernat.pdf
%doc %{_texmfdistdir}/doc/latex/hypernat/hypernat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-2
+ Revision: 752627
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-1
+ Revision: 718629
- texlive-hypernat
- texlive-hypernat
- texlive-hypernat
- texlive-hypernat

