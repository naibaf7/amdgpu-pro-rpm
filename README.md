# amdgpu-pro-rpm
Spec file for building RPM's for amdgpu pro (untested!)

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
