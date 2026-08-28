
## Installing software from source on Linux involves downloading the raw source code, satisfying its dependencies, compiling it into executable binary files, and placing those binaries into your system path.

---

## Prerequisites

Before compiling software, you need a C/C++ compiler, build toolchains, and basic header files installed on your system.

**Debian / Ubuntu:**

```bash
sudo \
  apt \
  update

sudo \
  apt \
  install \
  build-essential \
  cmake \
  git \
  autoconf \
  automake \
  libtool \
  pkg-config
```

**Fedora / RHEL / CentOS:**

```bash
sudo \
  dnf \
  groupinstall \
  "Development Tools"

sudo \
  dnf \
  install \
  cmake \
  git \
  autoconf \
  automake \
  libtool \
  pkgconfig
```

**Arch Linux:**

```bash
sudo \
  pacman \
  -S \
  --needed \
  base-devel \
  cmake \
  git \
  autoconf \
  automake \
  libtool \
  pkgconf
```

---

## Step-by-Step Installation Guides

Different projects use different build systems. Identify the primary build file in the repository (e.g., `Makefile`, `CMakeLists.txt`, `meson.build`, or `configure`) to determine which build method to use.

### 1. Clone or Download the Source Code
Obtain the source files directly from GitHub or a tarball archive.

**From GitHub:**

```bash
git \
  clone \
  --recursive \
  [https://github.com/username/repository.name.git](https://github.com/username/repository.name.git)

cd \
  repository.name
```

*Note: Using `--recursive` ensures git fetches any required submodules inside the project.*

**From a Source Tarball Archive (`.tar.gz`, `.tar.bz2`, `.tar.xz`):**

```bash
tar \
  -xvf \
  software-name-1.0.0.tar.gz

cd \
  software-name-1.0.0
```

### 2. Check for Dependencies and Build Instructions
Always inspect project documentation before running build scripts. Read the project's documentation files to identify required library dependencies and specific build flags:

```bash
cat \
  README.md
```
*or*
```bash
cat \
  INSTALL
```

Install any missing development packages (usually named with a `-dev` suffix on Debian/Ubuntu or `-devel` on Fedora) via your package manager.

### 3. Compile and Install Using the Project's Build System
Follow the method matching the repository's configuration files. Choose **one** of the following sub-methods based on what files exist in the repository root:

#### Option A: GNU Autotools (`./configure`)
*Used if the project contains a `configure` or `autogen.sh` file.*

```bash
# Generate the configure script if only autogen.sh or bootstrap.sh exists
./autogen.sh

# Configure the build environment and check dependencies
./configure \
  --prefix=/usr/local

# Compile the software using available CPU cores
make \
  -j$(nproc)

# Install binaries to the system
sudo \
  make \
  install
```

#### Option B: CMake
*Used if the project contains a `CMakeLists.txt` file.*

```bash
# Create and enter a dedicated build directory
mkdir \
  build && \
cd \
  build

# Generate native build files
cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/usr/local \
  ..

# Compile the binaries
cmake \
  --build \
  . \
  -j$(nproc)

# Install binaries to the system
sudo \
  cmake \
  --install \
  .
```

#### Option C: Meson & Ninja
*Used if the project contains a `meson.build` file.*

```bash
# Set up the build directory
meson \
  setup \
  build \
  --buildtype=release \
  --prefix=/usr/local

# Enter build directory and compile
cd \
  build

ninja

# Install binaries to the system
sudo \
  ninja \
  install
```

#### Option D: Standard `Makefile` Only
*Used if the project only contains a plain `Makefile` without a configure step.*

```bash
# Compile directly
make \
  -j$(nproc)

# Install binaries
sudo \
  make \
  install
```

### 4. Update Shared Library Cache and Verify
Ensure your system links new libraries and binary paths correctly. If the installation added shared libraries (`.so` files), refresh the system dynamic linker cache:

```bash
sudo \
  ldconfig
```

Verify that the executable is accessible in your standard system path:

```bash
which \
  program-name

program-name \
  --version
```

---

## Key Concepts and Flags Explained

* **`--prefix=/usr/local`**: Controls where the software gets installed. Installing to `/usr/local` is standard practice for software compiled from source so it does not overwrite distribution-managed system files in `/usr/bin` or `/usr/lib`.
* **`-j$(nproc)`**: Passes the total count of available CPU processing cores to the build tool, compiling multiple files concurrently to reduce build time.
* **`checkinstall` (Safer Uninstallation Alternative)**: Running `sudo checkinstall` instead of `sudo make install` creates a native package (`.deb` or `.rpm`) and registers it with your system package manager. This makes cleanly uninstalling the software easier later using standard package manager commands.

---

## How to Uninstall Source Software

If installed directly via `make install`, return to the project's `build` or source directory:

```bash
sudo \
  make \
  uninstall
```

If the original `Makefile` lacks an `uninstall` target, manually remove the installed binary and associated files:

```bash
sudo \
  rm \
  /usr/local/bin/program-name
```
