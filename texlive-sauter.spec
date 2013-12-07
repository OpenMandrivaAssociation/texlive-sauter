# revision 13293
# category Package
# catalog-ctan /fonts/cm/sauter
# catalog-date 2008-12-30 21:17:11 +0100
# catalog-license gpl
# catalog-version 2.4
Name:		texlive-sauter
Version:	2.4
Release:	3
Summary:	Wide range of design sizes for CM fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cm/sauter
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauter.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extensions, originally to the CM fonts, providing a
parameterization scheme to build MetaFont fonts at true design
sizes, for a large range of sizes. The scheme has now been
extended to a range of other fonts, including the AMS fonts,
bbm, bbold, rsfs and wasy fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/sauter/b-cmb.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbxsl.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmbxti.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmcsc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmdunh.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmex.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmff.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmfi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmfib.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cminch.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmitt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmmi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmmib.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmr.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsl.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsltt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmss.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssdc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssq.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssqi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmssxi.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtcsc.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtex.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmti.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmu.mf
%{_texmfdistdir}/fonts/source/public/sauter/b-cmvtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-bmath.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmex.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmff.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmmi.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmr.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmss.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmssbx.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmssq.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmsy.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmti.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-cmtt.mf
%{_texmfdistdir}/fonts/source/public/sauter/c-sigma.mf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4-2
+ Revision: 755791
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-1
+ Revision: 719482
- texlive-sauter
- texlive-sauter
- texlive-sauter
- texlive-sauter

