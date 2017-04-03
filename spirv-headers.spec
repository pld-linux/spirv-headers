
%define commit	c470b68225a04965bf87d35e143ae92f831e8110

Summary:	SPIR-V headers
Name:		spirv-headers
Version:	1.1_rev4
Release:	4
License:	distributable
Group:		Libraries
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{commit}/%{name}-%{commit}.tar.gz
# Source0-md5:	a230473aae8366730509fc023c69116b
URL:		https://github.com/KhronosGroup/SPIRV-Headers
Conflicts:	spirv-tools-devel < v2016.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains machine-readable files from the SPIR-V Registry.
This includes:

- Header files for various languages.
- JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.

%prep
%setup -qn SPIRV-Headers-%{commit}

%build

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
