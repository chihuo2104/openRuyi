# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-metrics
%define go_import_path  github.com/hashicorp/go-metrics
%define go_compat_import_path  github.com/armon/go-metrics
# Circonus, Prometheus and local socket sink tests are incompatible with
# packaged dependency versions or the OBS build environment. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/circonus
    %{go_import_path}/prometheus
}

Name:           go-github-hashicorp-go-metrics
Version:        0.7.0
Release:        %autorelease
Summary:        Metrics instrumentation library for Go
License:        MIT
URL:            https://github.com/hashicorp/go-metrics
#!RemoteAsset:  sha256:cfa7c21e9ae96332435c2559e80b8041fc926a53aa53e263c6d0d32df263719e
Source0:        https://github.com/hashicorp/go-metrics/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/datadog-go) >= 4.8.3
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/circonus-labs/circonus-gometrics)
BuildRequires:  go(github.com/circonus-labs/circonusllhist)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/pascaldekloe/goe)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/tv42/httpunix)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/armon/go-metrics) = %{version}
Provides:       go(github.com/hashicorp/go-metrics) = %{version}
Provides:       go-github-armon-go-metrics = %{version}-%{release}

Obsoletes:      go-github-armon-go-metrics

Requires:       go(github.com/DataDog/datadog-go)
Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/circonus-labs/circonus-gometrics)
Requires:       go(github.com/circonus-labs/circonusllhist)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-immutable-radix)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(github.com/matttproud/golang_protobuf_extensions)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/tv42/httpunix)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description
This library provides a metrics package which can be used to instrument
code, expose application metrics, and profile runtime performance in a
flexible manner.

# Upstream moved from github.com/armon/go-metrics to
# github.com/hashicorp/go-metrics at v0.5.0. Install a compatibility copy for
# consumers that still import the old path. The check section is left to the
# golangmodules default: no package in the module imports the old path anymore.
%install -a
mkdir -p %{buildroot}%{go_sys_gopath}/$(dirname %{go_compat_import_path})
cp -a %{buildroot}%{go_sys_gopath}/%{go_import_path} \
      %{buildroot}%{go_sys_gopath}/%{go_compat_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/%{go_compat_import_path}

%changelog
%autochangelog
