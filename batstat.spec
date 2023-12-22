%global commit      e107193e99fb8d461050358f05aa8343e2fd5bc9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           batstat
Version:        0~^1.%{shortcommit}
Release:        %autorelease
Summary:        CLI battery status for Linux

License:        None
URL:            https://github.com/Juve45/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc-c++
BuildRequires: ncurses-devel

%description
%{summary}


%prep
%autosetup -n %{name}-%{commit}


%build
%make_build CCFLAGS="%{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}


%files
%{_bindir}/%{name}
%doc README.md


%changelog
%autochangelog

