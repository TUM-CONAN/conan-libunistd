from conans import ConanFile, CMake, tools
import os


class LibUniStdConan(ConanFile):
    name = "libunistd"
    version = "1.2"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
    }

    default_options = (
        "shared=False",
        )

    exports = ["CMakeLists.txt", ]

    url="http://github.com/ulricheck/conan-libunistd"
    license="libunistd MIT"
    description="Compatibility of Posix applications for Windows"
    
    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/robinrowe/libunistd",
        "revision": "v1.2",
    }

    def build(self):
        """ Define your project building. You decide the way of building it
            to reuse it later in any other project.
        """
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        # cmake.install()

    def package(self):
        """ Define your conan structure: headers, libs, bins and data. After building your
            project, this method is called to create a defined structure:
        """
        self.copy("*", src="lib", dst="lib")
        self.copy("*.dll", src="bin", dst="bin")

        #for now we're only interested in the unistd headers ..
        self.copy("*.h", src=os.path.join("sources", "unistd"), dst="include", keep_path=True)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
