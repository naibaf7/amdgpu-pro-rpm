#No debug file
%global debug_package %{nil}

%ifarch x86_64
%global archname x86_64
%global archname2 amd64
%else
%global archname i386
%global archname2 i386
%endif

Name:           amdgpu-pro
Version:        16.30.3
Release:        306809
License:        AMD EULA
URL:            http://www.amd.com
Source0:        https://www2.ati.com/drivers/linux/%{name}_%{version}-%{release}.tar.xz
ExclusiveArch:  x86_64 %ix86

%ifarch x86_64
Requires:       %{name}-graphics%{?_isa} = %{version}-%{release}
Requires:       %{name}-computing%{?_isa} = %{version}-%{release}
Summary:        This package install all amdgpu-pro components.
%description
AMDGPU-Pro Driver
%else
Requires:       libgles2-%{name}%{?_isa} = %{version}-%{release}
Requires:       libgl1-%{name}-devel%{?_isa} = %{version}-%{release}
Requires:       libgl1-%{name}-dri%{?_isa} = %{version}-%{release}
Requires:       libgbm1-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-opencl-icd%{?_isa} = %{version}-%{release}
Requires:       %{name}-libopencl-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-vulkan-driver%{?_isa} = %{version}-%{release}
Requires:       libvdpau-%{name}%{?_isa} = %{version}-%{release}
Summary:        This package contains x86 libs for x86_64 machine usage.
%description
This package contains x86 libs for x86_64 machine usage.
%endif

%ifarch x86_64
%package clinfo
Requires:       %{name}-libopencl1%{?_isa} = %{version}-%{release}
Summary:        AMD OpenCL info utility

%package computing
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-clinfo%{?_isa} = %{version}-%{release}
Requires:       %{name}-opencl-icd%{?_isa} = %{version}-%{release}
Requires:       %{name}-libopencl-devel%{?_isa} = %{version}-%{release}
Summary:        This package install amdgpu-pro OpenCL components.

%package core
Requires:       linux-firmware
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Summary:        This package switchs the GPU stack to amdgpu-pro with basic

%package dkms
Summary:        amdgpu-pro driver in DKMS format.
BuildArch:      noarch
Requires:       dkms

%package graphics
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       libgles2-%{name}%{?_isa} = %{version}-%{release}
Requires:       libgl1-%{name}-devel%{?_isa} = %{version}-%{release}
Requires:       libgl1-%{name}-dri%{?_isa} = %{version}-%{release}
Requires:       xserver-xorg-video-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-vulkan-driver%{?_isa} = %{version}-%{release}
Requires:       libvdpau-%{name}%{?_isa} = %{version}-%{release}
Summary:        This package install amdgpu-pro graphics components.

%package -n xserver-xorg-video-%{name}
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Requires:       libgbm1-%{name}%{?_isa} = %{version}-%{release}
Requires:       libgl1-%{name}-glx%{?_isa} = %{version}-%{release}
Summary:        X.Org X server -- AMD/ATI amdgpu-pro display driver

%package -n libdrm-%{name}-tools
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Summary:        testing tools for libdrm-amdgpu-pro

%description clinfo
 OpenCL (Open Computing Language) is a multivendor open standard for
 general-purpose parallel programming of heterogeneous systems that include
 CPUs, GPUs and other processors.
 .
 This package contains the clinfo utility provided by AMD. It reports status
 information for all ICDs (installable client drivers) that are installed in
 the system.

%description computing
This package install amdgpu-pro OpenCL components.

%description core
This package install amdgpu-pro OpenCL components.

This package switchs the GPU stack to amdgpu-pro with basic

%description dkms
amdgpu-pro DKMS kernel driver

%description graphics
This package install amdgpu-pro graphics components.

%description -n xserver-xorg-video-%{name}
X.Org X server -- AMD/ATI %{name} display driver

%description -n libdrm-%{name}-tools
testing tools for libdrm-amdgpu-pro
%endif

%package libopencl-devel
Requires:       %{name}-libopencl1%{?_isa} = %{version}-%{release}
Summary:        AMD OpenCL ICD Loader library

%package libopencl1
Summary:        AMD OpenCL ICD Loader library

%package opencl-icd
Summary:        non-free AMD OpenCL ICD Loaders

%package vulkan-driver
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Summary:        AMDGPU Pro Vulkan driver

%package -n libdrm-%{name}-amdgpu1
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Summary:        Userspace interface to amdgpu-specific kernel DRM services -- runtime

%package -n libdrm-%{name}-devel
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Summary:        Userspace interface to kernel DRM services -- development files

%package -n libdrm2-%{name}
Summary:        Userspace interface to kernel DRM services -- runtime

%package -n libegl1-%{name}
Summary:        implementation of the EGL API -- runtime

%package -n libegl1-%{name}-devel
Requires:       libegl1-%{name}%{?_isa} = %{version}-%{release}
Summary:        implementation of the EGL API -- development files

%package -n libgbm-%{name}-devel
Requires:       libgbm1-%{name}%{?_isa} = %{version}-%{release}
Summary:        generic buffer management API -- development files

%package -n libgbm1-%{name}
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Summary:        generic buffer management API -- runtime

%package -n libgl1-%{name}-devel
Requires:       libgl1-%{name}-glx%{?_isa} = %{version}-%{release}
Summary:        implementation of the OpenGL API -- GLX development files

%package -n libgl1-%{name}-dri
Summary:        implementation of the OpenGL API -- DRI modules

%package -n libgl1-%{name}-glx
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Summary:        implementation of the OpenGL API -- GLX runtime

%package -n libgles2-%{name}
Requires:       libegl1-%{name}%{?_isa} = %{version}-%{release}
Summary:        implementation of the OpenGL|ES 2.x API -- runtime

%package -n libgles2-%{name}-devel
Requires:       libgles2-%{name}%{?_isa} = %{version}-%{release}
Summary:        implementation of the OpenGL|ES 2.x API -- development files

%package -n libvdpau-%{name}
Requires:       libdrm-%{name}-amdgpu1%{?_isa} = %{version}-%{release}
Requires:       libdrm2-%{name}%{?_isa} = %{version}-%{release}
Summary:        AMDGPU Pro VDPAU driver

%description libopencl-devel
 OpenCL (Open Computing Language) is a multivendor open standard for
 general-purpose parallel programming of heterogeneous systems that include
 CPUs, GPUs and other processors.
 .
 The OpenCL installable client driver loader (ICD Loader) acts as a dispatcher
 between an OpenCL application and one (or more) installable client drivers
 (ICD) that can be from any vendor. At least one ICD (and the corresponding
 hardware) is required to run OpenCL applications.
 .
 This package contains the development file for ICD Loader library provided
 by AMD.

%description libopencl1
 OpenCL (Open Computing Language) is a multivendor open standard for
 general-purpose parallel programming of heterogeneous systems that include
 CPUs, GPUs and other processors.
 .
 The OpenCL installable client driver loader (ICD Loader) acts as a dispatcher
 between an OpenCL application and one (or more) installable client drivers
 (ICD) that can be from any vendor. At least one ICD (and the corresponding
 hardware) is required to run OpenCL applications.
 .
 This package contains the ICD Loader library provided by AMD.

%description opencl-icd
 OpenCL (Open Computing Language) is a multivendor open standard for
 general-purpose parallel programming of heterogeneous systems that include
 CPUs, GPUs and other processors.
 .
 This package provides the AMD installable client driver (ICD) for OpenCL
 which supports AMD GPUs (requires the amdgpu-pro driver) as well as CPUs (from
 any vendor, no driver required).

%description vulkan-driver
AMDGPU Pro Vulkan driver

%description -n libdrm-%{name}-amdgpu1
 This library implements the userspace interface to the amdgpu-specific kernel
 DRM services.  DRM stands for "Direct Rendering Manager", which is the
 kernelspace portion of the "Direct Rendering Infrastructure" (DRI). The DRI is
 currently used on Linux to provide hardware-accelerated OpenGL drivers.

%description -n libdrm-%{name}-devel
 This library implements the userspace interface to the kernel DRM
 services.  DRM stands for "Direct Rendering Manager", which is the
 kernelspace portion of the "Direct Rendering Infrastructure" (DRI).
 The DRI is currently used on Linux to provide hardware-accelerated
 OpenGL drivers.
 .
 This package provides the development environment for libdrm.

%description -n libdrm2-%{name}
 This library implements the userspace interface to the kernel DRM
 services.  DRM stands for "Direct Rendering Manager", which is the
 kernelspace portion of the "Direct Rendering Infrastructure" (DRI).
 The DRI is currently used on Linux to provide hardware-accelerated
 OpenGL drivers.
 .
 This package provides the runtime environment for libdrm.

%description -n libegl1-%{name}
implementation of the EGL API -- runtime

%description -n libegl1-%{name}-devel
implementation of the EGL API -- development files

%description -n libgbm-%{name}-devel
generic buffer management API -- development files

%description -n libgbm1-%{name}
generic buffer management API -- runtime

%description -n libgl1-%{name}-devel
implementation of the OpenGL API -- GLX development files

%description -n libgl1-%{name}-dri
implementation of the OpenGL API -- DRI modules

%description -n libgl1-%{name}-glx
implementation of the OpenGL API -- GLX runtime

%description -n libgles2-%{name}
implementation of the OpenGL|ES 2.x API -- runtime

%description -n libgles2-%{name}-devel
implementation of the OpenGL|ES 2.x API -- development files

%description -n libvdpau-%{name}
AMDGPU Pro VDPAU driver

%prep
%setup -q -n %{name}-driver

%build
#no build

%install
%ifarch x86_64
#amdgpu-pro package
mkdir %{name}_%{version}-%{release}_amd64
cd %{name}_%{version}-%{release}_amd64
ar x ../%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-clinfo package
mkdir %{name}-clinfo_%{version}-%{release}_amd64
cd %{name}-clinfo_%{version}-%{release}_amd64
ar x ../%{name}-clinfo_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-computing package
mkdir %{name}-computing_%{version}-%{release}_amd64
cd %{name}-computing_%{version}-%{release}_amd64
ar x ../%{name}-computing_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-core package
mkdir %{name}-core_%{version}-%{release}_amd64
cd %{name}-core_%{version}-%{release}_amd64
ar x ../%{name}-core_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz

mv %{buildroot}/lib %{buildroot}%{_prefix}/
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
ln -s %{_prefix}/lib/%{name}/ld.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/10-%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
ln -s %{_prefix}/lib/%{name}/modprobe.conf %{buildroot}%{_sysconfdir}/modprobe.d/%{name}.conf
cd ..

#amdgpu-pro-dkms package
mkdir %{name}-dkms_%{version}-%{release}_all
cd %{name}-dkms_%{version}-%{release}_all
ar x ../%{name}-dkms_%{version}-%{release}_all.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-graphics package
mkdir %{name}-graphics_%{version}-%{release}_amd64
cd %{name}-graphics_%{version}-%{release}_amd64
ar x ../%{name}-graphics_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#xserver-xorg-video-amdgpu-pro package
mkdir xserver-xorg-video-%{name}_%{version}-%{release}_amd64
cd xserver-xorg-video-%{name}_%{version}-%{release}_amd64
ar x ../xserver-xorg-video-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-tools package
mkdir libdrm-%{name}-tools_%{version}-%{release}_%{archname2}
cd libdrm-%{name}-tools_%{version}-%{release}_%{archname2}
ar x ../libdrm-%{name}-tools_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

%else

#amdgpu-pro (32bit) package
mkdir %{name}-lib32_%{version}-%{release}_i386
cd %{name}-lib32_%{version}-%{release}_i386
ar x ../%{name}-lib32_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

%endif

#amdgpu-pro-libopencl-devel package
mkdir %{name}-libopencl-dev_%{version}-%{release}_%{archname2}
cd %{name}-libopencl-dev_%{version}-%{release}_%{archname2}
ar x ../%{name}-libopencl-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-libopencl1 package
mkdir %{name}-libopencl1_%{version}-%{release}_%{archname2}
cd %{name}-libopencl1_%{version}-%{release}_%{archname2}
ar x ../%{name}-libopencl1_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-opencl-icd package
mkdir %{name}-opencl-icd_%{version}-%{release}_%{archname2}
cd %{name}-opencl-icd_%{version}-%{release}_%{archname2}
ar x ../%{name}-opencl-icd_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-vulkan-driver package
mkdir %{name}-vulkan-driver_%{version}-%{release}_%{archname2}
cd %{name}-vulkan-driver_%{version}-%{release}_%{archname2}
ar x ../%{name}-vulkan-driver_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-amdgpu1 package
mkdir libdrm-%{name}-amdgpu1_%{version}-%{release}_%{archname2}
cd libdrm-%{name}-amdgpu1_%{version}-%{release}_%{archname2}
ar x ../libdrm-%{name}-amdgpu1_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-devel package
mkdir libdrm-%{name}-dev_%{version}-%{release}_%{archname2}
cd libdrm-%{name}-dev_%{version}-%{release}_%{archname2}
ar x ../libdrm-%{name}-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm2-amdgpu-pro package
mkdir libdrm2-%{name}_%{version}-%{release}_%{archname2}
cd libdrm2-%{name}_%{version}-%{release}_%{archname2}
ar x ../libdrm2-%{name}_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro package
mkdir libegl1-%{name}_%{version}-%{release}_%{archname2}
cd libegl1-%{name}_%{version}-%{release}_%{archname2}
ar x ../libegl1-%{name}_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro-devel package
mkdir libegl1-%{name}-dev_%{version}-%{release}_%{archname2}
cd libegl1-%{name}-dev_%{version}-%{release}_%{archname2}
ar x ../libegl1-%{name}-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm-amdgpu-pro-devel package
mkdir libgbm-%{name}-dev_%{version}-%{release}_%{archname2}
cd libgbm-%{name}-dev_%{version}-%{release}_%{archname2}
ar x ../libgbm-%{name}-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm1-amdgpu-pro package
mkdir libgbm1-%{name}_%{version}-%{release}_%{archname2}
cd libgbm1-%{name}_%{version}-%{release}_%{archname2}
ar x ../libgbm1-%{name}_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-devel package
mkdir libgl1-%{name}-dev_%{version}-%{release}_%{archname2}
cd libgl1-%{name}-dev_%{version}-%{release}_%{archname2}
ar x ../libgl1-%{name}-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-dri package
mkdir libgl1-%{name}-dri_%{version}-%{release}_%{archname2}
cd libgl1-%{name}-dri_%{version}-%{release}_%{archname2}
ar x ../libgl1-%{name}-dri_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-glx package
mkdir libgl1-%{name}-glx_%{version}-%{release}_%{archname2}
cd libgl1-%{name}-glx_%{version}-%{release}_%{archname2}
ar x ../libgl1-%{name}-glx_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro package
mkdir libgles2-%{name}_%{version}-%{release}_%{archname2}
cd libgles2-%{name}_%{version}-%{release}_%{archname2}
ar x ../libgles2-%{name}_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro-devel package
mkdir libgles2-%{name}-dev_%{version}-%{release}_%{archname2}
cd libgles2-%{name}-dev_%{version}-%{release}_%{archname2}
ar x ../libgles2-%{name}-dev_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libvdpau-amdgpu-pro package
mkdir libvdpau-%{name}_%{version}-%{release}_%{archname2}
cd libvdpau-%{name}_%{version}-%{release}_%{archname2}
ar x ../libvdpau-%{name}_%{version}-%{release}_%{archname2}.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

%post libopencl1
/sbin/ldconfig

%postun libopencl1
/sbin/ldconfig

%post opencl-icd
/sbin/ldconfig

%postun opencl-icd
/sbin/ldconfig

%post vulkan-driver
/sbin/ldconfig

%postun vulkan-driver
/sbin/ldconfig

%post -n libdrm2-%{name}
/sbin/ldconfig

%postun -n libdrm2-%{name}
/sbin/ldconfig

%post -n libdrm-%{name}-amdgpu1
/sbin/ldconfig

%postun -n libdrm-%{name}-amdgpu1
/sbin/ldconfig

%post -n libegl1-%{name}
/sbin/ldconfig

%postun -n libegl1-%{name}
/sbin/ldconfig

%post -n libgbm1-%{name}
/sbin/ldconfig

%postun -n libgbm1-%{name}
/sbin/ldconfig

%post -n libgl1-%{name}-dri
/sbin/ldconfig

%postun -n libgl1-%{name}-dri
/sbin/ldconfig

%post -n libgl1-%{name}-glx
/sbin/ldconfig

%postun -n libgl1-%{name}-glx
/sbin/ldconfig

%post -n libgles2-%{name}
/sbin/ldconfig

%postun -n libgles2-%{name}
/sbin/ldconfig

%post -n libvdpau-%{name}
/sbin/ldconfig

%postun -n libvdpau-%{name}
/sbin/ldconfig

%ifarch x86_64
%files
%{_datadir}/doc/%{name}

%files clinfo
%{_bindir}/clinfo
%{_datadir}/doc/%{name}-clinfo

%files computing
%{_datadir}/doc/%{name}-computing

%files core
%dir %{_sysconfdir}/amd
%config(noreplace) %{_sysconfdir}/amd/amdapfxx.blb
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/10-%{name}.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/%{name}.conf
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}-core
%{_datadir}/initramfs-tools/hooks/*

%files dkms
%{_datadir}/%{name}-dkms
%{_datadir}/doc/%{name}-dkms
%{_prefix}/src/%{name}-%{version}-%{release}

%files graphics
%config(noreplace) %{_sysconfdir}/amd/amdrc
%config(noreplace) %{_sysconfdir}/gbm/gbm.conf
%{_datadir}/doc/%{name}-graphics
%{_datadir}/X11/xorg.conf.d/*

%files -n xserver-xorg-video-%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/1.15
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/1.16
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/1.17
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/1.18
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/xorg
%{_datadir}/doc/xserver-xorg-video-%{name}
%{_mandir}/*

%files -n libdrm-%{name}-tools
%{_bindir}/amdgpu_test
%{_bindir}/kmstest
%{_bindir}/modeprint
%{_bindir}/modetest
%{_bindir}/proptest
%{_bindir}/vbltest
%{_datadir}/doc/libdrm-%{name}-tools

%else

%files
%{_datadir}/doc/%{name}-lib32

%endif

%files libopencl1
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libOpenCL.so.*
%{_datadir}/doc/%{name}-libopencl1

%files libopencl-devel
%{_prefix}/lib/%{archname}-linux-gnu/libOpenCL.so
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libOpenCL.so
%{_datadir}/doc/%{name}-libopencl-dev

%files opencl-icd
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl*.icd
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libamdocl*.so
%{_datadir}/doc/%{name}-opencl-icd

%files vulkan-driver
%config(noreplace) %{_sysconfdir}/vulkan/icd.d/amd_icd*.json
%{_prefix}/lib/%{archname}-linux-gnu/amdvlk*.so
%{_datadir}/doc/%{name}-vulkan-driver

%files -n libdrm2-%{name}
%dir %{_prefix}/lib/%{archname}-linux-gnu/%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm.so.*
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libkms.so.*
%{_datadir}/doc/libdrm2-%{name}

%files -n libdrm-%{name}-amdgpu1
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm_amdgpu.so.*
%{_datadir}/doc/libdrm-%{name}-amdgpu1

%files -n libdrm-%{name}-devel
%{_includedir}/%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm.la
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm.so
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm_amdgpu.la
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libdrm_amdgpu.so
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/pkgconfig
%{_datadir}/doc/libdrm-%{name}-dev

%files -n libegl1-%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libEGL.so.*
%{_datadir}/doc/libegl1-%{name}

%files -n libegl1-%{name}-devel
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libEGL.so
%{_datadir}/doc/libegl1-%{name}-dev

%files -n libgbm1-%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/gbm
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libgbm.so.*
%{_datadir}/doc/libgbm1-%{name}

%files -n libgbm-%{name}-devel
%{_datadir}/doc/libgbm-%{name}-dev

%files -n libgl1-%{name}-devel
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libGL.so
%{_datadir}/doc/libgl1-%{name}-dev

%files -n libgl1-%{name}-dri
%{_prefix}/lib/%{archname}-linux-gnu/dri
%{_datadir}/doc/libgl1-%{name}-dri

%files -n libgl1-%{name}-glx
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libGL.so.*
%{_datadir}/doc/libgl1-%{name}-glx

%files -n libgles2-%{name}
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libGLESv2.so.*
%{_datadir}/doc/libgles2-%{name}

%files -n libgles2-%{name}-devel
%{_prefix}/lib/%{archname}-linux-gnu/%{name}/libGLESv2.so
%{_datadir}/doc/libgles2-%{name}-dev

%files -n libvdpau-%{name}
%{_prefix}/lib/%{archname}-linux-gnu/vdpau
%{_datadir}/doc/libvdpau-%{name}

%changelog

