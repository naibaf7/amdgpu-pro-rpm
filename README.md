# amdgpu-pro-rpm
Spec file for building RPM's for amdgpu pro.

##Disclamer

AMDGPU Pro is compiled for Ubuntu, not Fedora or variants, thus it may not work. Caution is advised when installing this software, so backup anything important as it may render your OS unusable.

Furthermore, it is advised to use the 4.7 kernel or later rather than the dkms package. If you can, use the latest version of linux-firmware.

##Build Instructions:

1) Download the binaries:

```
spectool -g amdgpu-pro.spec
```

2) Copy the binaries into ~/rpmbuild/SOURCES

```
cp amdgpu-pro_*.tar.xz ~/rpmbuild/SOURCES
```

3) Build:

```
QA_RPATHS=2 rpmbuild -ba amdgpu-pro.spec
```

4) OPTIONAL: Build i386 packages:

```
QA_RPATHS=2 setarch i386 rpmbuild -ba amdgpu-pro.spec
```
