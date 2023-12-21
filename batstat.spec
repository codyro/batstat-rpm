Name:           batstat
Version:        0^20230808gite107193
Release:        %autorelease
Summary:        CLI battery status for Linux

License:        None
URL:            https://github.com/Juve45/%{name}
Source0:        %{name}-0_20230808gite107193.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ncurses-devel

%description
%{summary}


%prep
%autosetup -n %{name}-0_20230808gite107193


%build
%make_build CCFLAGS="%{optflags}"


%install
mkdir -p %{buildroot}/usr/bin
%make_install PREFIX=%{_prefix}


%check


%files
%{_bindir}/%{name}
%doc README.md


%changelog
* Fri Sep 15 2023 Cody Robertson <cody@nerdymuffin.com> - 0^20230808gite107193-0
- Initial package creation

