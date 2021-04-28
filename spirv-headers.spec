Summary:	SPIR-V headers
Summary(pl.UTF-8):	Pliki nagłówkowe SPIR-V
Name:		spirv-headers
Version:	1.5.4
%define	subver	raytracing.fixed
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-Headers/releases
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{version}.%{subver}/%{name}-%{version}.%{subver}.tar.gz
# Source0-md5:	f49a22584eeb2609169970c2c3c1eb6e
URL:		https://github.com/KhronosGroup/SPIRV-Headers
Conflicts:	spirv-tools-devel < v2016.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains machine-readable files from the SPIR-V Registry.
This includes:
- header files for various languages,
- JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.

%description -l pl.UTF-8
Ten pakiet zawiera czytelne dla maszyny pliki z rejestru SPIR-V.
Obejmują one:
- pliki nagłówkowe dla różnych języków,
- pliki JSON opisujące gramatykę podstawowego zestawu instrukcji
  SPIR-V oraz rozszerzonego zestawu instrukcji GLSL.std.450.

%prep
%setup -qn SPIRV-Headers-%{version}.%{subver}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
cp -a include/spirv $RPM_BUILD_ROOT%{_includedir}/spirv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/spirv
