from conans import ConanFile, CMake, tools


prefix_patch = '''diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index f74b8d16..b489171a 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -198,7 +198,7 @@ find_package (Threads)
 #
 # -----------------------------------------------------------------------------
 # -----------------------------------------------------------------------------
-set (INSTALL_PREFIX "/usr")        
+set (INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
 if (WIN32)
     if (MSVC)
         set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")
'''

class opcuastackConan(ConanFile):
    name = "opcuastack"
    version = "3.8.1"
    commit = version
    license = "MIT"
    author = "Vladislav Troinich antlad@icloud.com"
    url = "https://github.com/ASNeG/OpcUaStack"
    description = "ASNeG OPC UA Stack is an open source framework for development and distribution of OPC UA client\server applications"
    topics = ("opcua")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"
    build_policy = "missing"
    requires = (
        "OpenSSL/1.1.1c@conan/stable",
        "boost/1.71.0@conan/stable"
    )

    def source(self):
        self.run('git clone --recursive -b {commit} --depth 1 {url}'.format(commit=self.commit,
                                                                url=self.url))
        tools.patch(base_path="./OpcUaStack", patch_string=prefix_patch)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_dir="./OpcUaStack/src", args=[])
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

        self.copy("*.h", dst="include", src="./src/", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['OpcUaStackClient', 'OpcUaStackPubSub', 'OpcUaStackCore', "OpcUaStackServer"]
        self.cpp_info.includedirs = ['include/OpcUaStack3']

