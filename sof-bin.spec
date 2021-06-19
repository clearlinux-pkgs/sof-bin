#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sof-bin
Version  : 1.7
Release  : 5
URL      : https://github.com/thesofproject/sof-bin/archive/v1.7/sof-bin-1.7.tar.gz
Source0  : https://github.com/thesofproject/sof-bin/archive/v1.7/sof-bin-1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sof-bin-license = %{version}-%{release}
Patch1: 0001-Add-makefile-for-easier-packaging.patch

%description
# SOF Firmware and Topology Binaries
This is the living area and distribution channel for SOF firmware and topology
binaries. It's still very much WiP and may churn a little until things
settle down.

%package license
Summary: license components for the sof-bin package.
Group: Default

%description license
license components for the sof-bin package.


%prep
%setup -q -n sof-bin-1.7
cd %{_builddir}/sof-bin-1.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624128071
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  SOF_VERSION=%{version}


%install
export SOURCE_DATE_EPOCH=1624128071
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sof-bin
cp %{_builddir}/sof-bin-1.7/LICENCE.Intel %{buildroot}/usr/share/package-licenses/sof-bin/b052da06a67e96a1d3ca22f4630bf7956ea88d5a
cp %{_builddir}/sof-bin-1.7/LICENCE.NXP %{buildroot}/usr/share/package-licenses/sof-bin/b428069e1aa2a6a89fc188a63dc40e861236a2e2
%make_install SOF_VERSION=%{version}

%files
%defattr(-,root,root,-)
/usr/lib/firmware/intel/sof-tplg/sof-apl-asrc-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-asrc-wm8804.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-da7219.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-demux-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-a2ch-b2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-a2ch-b4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-a4ch-b2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-dmic-a96k-b16k.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-eq-dmic.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-eq-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-keyword-detect.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-pcm512x-master-44100.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-pcm512x-master.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-pcm512x-nohdmi.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-pcm512x-tdfb_28mm-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-rt298.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-src-50khz-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-src-dmic.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-src-pcm512x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-tdf8532.tplg
/usr/lib/firmware/intel/sof-tplg/sof-apl-wm8804.tplg
/usr/lib/firmware/intel/sof-tplg/sof-bdw-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-bdw-rt286.tplg
/usr/lib/firmware/intel/sof-tplg/sof-bdw-rt5640.tplg
/usr/lib/firmware/intel/sof-tplg/sof-bdw-rt5677.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-cx2072x-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-cx2072x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-da7213-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-da7213.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-es8316-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-es8316.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5640-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5640.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5645-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5645.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5651-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5651.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5670-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5670.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5682-ssp0.tplg
/usr/lib/firmware/intel/sof-tplg/sof-byt-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-cx2072x.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-da7213.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-es8316.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-max98090.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-nau8824.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-rt5640.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-rt5645.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-rt5651.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-rt5670.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cht-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-da7219-max98357a.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-demux-rt5682-max98357a.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-demux-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-eq-fir-loud-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-eq-fir-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-eq-iir-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-eq-rt1011-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt1011-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt5682-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt5682-max98357a.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt700-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt700-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt700.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt711-rt1308-mono-rt715.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-rt711-rt1308-rt715.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cml-src-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cnl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cnl-rt274.tplg
/usr/lib/firmware/intel/sof-tplg/sof-cnl-rt5682-sdw2.tplg
/usr/lib/firmware/intel/sof-tplg/sof-ehl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-ehl-rt5660-nohdmi.tplg
/usr/lib/firmware/intel/sof-tplg/sof-ehl-rt5660.tplg
/usr/lib/firmware/intel/sof-tplg/sof-glk-da7219-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-glk-da7219.tplg
/usr/lib/firmware/intel/sof-tplg/sof-glk-eq-da7219.tplg
/usr/lib/firmware/intel/sof-tplg/sof-glk-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-asrc-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-1ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-2ch-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-3ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-4ch-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-eq-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-eq-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-eq.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-idisp-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-idisp-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-idisp.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic-tdfb_50mm-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-hda-generic.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-dmic-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt5682-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt700-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt700-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt700.tplg
/usr/lib/firmware/intel/sof-tplg/sof-icl-rt711-rt1308-rt715.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8-cs42888-mixer.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8-wm8960-mixer.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8mp-wm8960-mixer.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8mp-wm8960.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8qxp-cs42888.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8qxp-nocodec-sai.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8qxp-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-imx8qxp-wm8960.tplg
/usr/lib/firmware/intel/sof-tplg/sof-jsl-da7219-mx98360a.tplg
/usr/lib/firmware/intel/sof-tplg/sof-jsl-da7219.tplg
/usr/lib/firmware/intel/sof-tplg/sof-jsl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-jsl-rt5682-mx98360a.tplg
/usr/lib/firmware/intel/sof-tplg/sof-jsl-rt5682-rt1015.tplg
/usr/lib/firmware/intel/sof-tplg/sof-smart-amplifier-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-max98357a-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-max98373-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-nocodec.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt1011-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt5682-ssp0-max98373-ssp2.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-i2s-rt1308-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-i2s-rt1308-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-rt1308-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-rt1308-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-rt1308-mono-rt715.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-rt1308-rt715.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt711-rt1316-rt714.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-rt715-rt711-rt1308-mono.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-sdw-max98373-rt5682-2ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-tgl-sdw-max98373-rt5682-4ch.tplg
/usr/lib/firmware/intel/sof-tplg/sof-whl-demux-rt5682.tplg
/usr/lib/firmware/intel/sof-tplg/sof-whl-rt5682-kwd.tplg
/usr/lib/firmware/intel/sof-tplg/sof-whl-rt5682.tplg
/usr/lib/firmware/intel/sof/community/sof-apl.ri
/usr/lib/firmware/intel/sof/community/sof-cfl.ri
/usr/lib/firmware/intel/sof/community/sof-cml.ri
/usr/lib/firmware/intel/sof/community/sof-cnl.ri
/usr/lib/firmware/intel/sof/community/sof-ehl.ri
/usr/lib/firmware/intel/sof/community/sof-glk.ri
/usr/lib/firmware/intel/sof/community/sof-icl.ri
/usr/lib/firmware/intel/sof/community/sof-jsl.ri
/usr/lib/firmware/intel/sof/community/sof-tgl-h.ri
/usr/lib/firmware/intel/sof/community/sof-tgl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-apl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-cfl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-cml.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-cnl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-ehl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-glk.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-icl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-jsl.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-tgl-h.ri
/usr/lib/firmware/intel/sof/intel-signed/sof-tgl.ri
/usr/lib/firmware/intel/sof/sof-apl.ldc
/usr/lib/firmware/intel/sof/sof-apl.ri
/usr/lib/firmware/intel/sof/sof-bdw.ldc
/usr/lib/firmware/intel/sof/sof-bdw.ri
/usr/lib/firmware/intel/sof/sof-byt.ldc
/usr/lib/firmware/intel/sof/sof-byt.ri
/usr/lib/firmware/intel/sof/sof-cfl.ldc
/usr/lib/firmware/intel/sof/sof-cfl.ri
/usr/lib/firmware/intel/sof/sof-cht.ldc
/usr/lib/firmware/intel/sof/sof-cht.ri
/usr/lib/firmware/intel/sof/sof-cml.ldc
/usr/lib/firmware/intel/sof/sof-cml.ri
/usr/lib/firmware/intel/sof/sof-cnl.ldc
/usr/lib/firmware/intel/sof/sof-cnl.ri
/usr/lib/firmware/intel/sof/sof-ehl.ldc
/usr/lib/firmware/intel/sof/sof-ehl.ri
/usr/lib/firmware/intel/sof/sof-glk.ldc
/usr/lib/firmware/intel/sof/sof-glk.ri
/usr/lib/firmware/intel/sof/sof-icl.ldc
/usr/lib/firmware/intel/sof/sof-icl.ri
/usr/lib/firmware/intel/sof/sof-jsl.ldc
/usr/lib/firmware/intel/sof/sof-jsl.ri
/usr/lib/firmware/intel/sof/sof-tgl-h.ldc
/usr/lib/firmware/intel/sof/sof-tgl-h.ri
/usr/lib/firmware/intel/sof/sof-tgl.ldc
/usr/lib/firmware/intel/sof/sof-tgl.ri

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sof-bin/b052da06a67e96a1d3ca22f4630bf7956ea88d5a
/usr/share/package-licenses/sof-bin/b428069e1aa2a6a89fc188a63dc40e861236a2e2
