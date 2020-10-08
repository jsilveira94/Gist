from conans import CMake, ConanFile


class GistConan(ConanFile):
    name = "gist"
    version = "0.0.1"
    url = "https://github.com/jsilveira94/Gist"
    description = "C++ based audio analysis library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"
    exports_sources = "include*", "src*", "CMakeLists.txt"

    def requirements(self):
        self.requires.add("fftw/3.3.8")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include/gist", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gist"]
