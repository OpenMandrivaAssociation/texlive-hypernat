# revision 17358
# category Package
# catalog-ctan /macros/latex/contrib/hypernat
# catalog-date 2010-03-08 12:29:56 +0100
# catalog-license gpl
# catalog-version 1.0b
Name:		texlive-hypernat
Version:	1.0b
Release:	1
Summary:	Allow hyperref and natbib to work together
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypernat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Allows hyperref package and the natbib package with options
'numbers' and 'sort&compress' to work together. This means that
multiple sequential citations (e.g [3,2,1]) will be compressed
to [1-3], where the '1' and the '3' are (color-)linked to the
bibliography.

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
%{_texmfdistdir}/tex/latex/hypernat/hypernat.sty
%doc %{_texmfdistdir}/doc/latex/hypernat/hypernat.pdf
%doc %{_texmfdistdir}/doc/latex/hypernat/hypernat.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
