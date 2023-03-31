Name:		texlive-hypernat
Version:	17358
Release:	2
Summary:	Allow hyperref and natbib to work together
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypernat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypernat.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
