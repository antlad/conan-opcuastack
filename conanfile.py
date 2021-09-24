from conans import ConanFile, CMake, tools


prefix_patch = '''diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index 0232a532..f8237900 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -156,7 +156,7 @@ find_package (Threads)
 #
 # -----------------------------------------------------------------------------
 # -----------------------------------------------------------------------------
-set (INSTALL_PREFIX "/usr")        
+set (INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})        
 if (WIN32)
     if (MSVC)
         set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")
diff --git a/src/OpcUaProjectBuilder/ProjectTemplate/src/ProjectName/CMakeLists.txt b/src/OpcUaProjectBuilder/ProjectTemplate/src/ProjectName/CMakeLists.txt
index 6e76b56c..e7ada8ec 100644
--- a/src/OpcUaProjectBuilder/ProjectTemplate/src/ProjectName/CMakeLists.txt
+++ b/src/OpcUaProjectBuilder/ProjectTemplate/src/ProjectName/CMakeLists.txt
@@ -48,7 +48,7 @@ file(
 )
 
 add_library(
-    ProjectName SHARED
+    ProjectName
     ${ProjectName_SRC}
 )
 
diff --git a/src/OpcUaStackCore/CMakeLists.txt b/src/OpcUaStackCore/CMakeLists.txt
index 904bc49f..489b0ea5 100644
--- a/src/OpcUaStackCore/CMakeLists.txt
+++ b/src/OpcUaStackCore/CMakeLists.txt
@@ -18,7 +18,6 @@ file(
 
 add_library(
     OpcUaStackCore 
-    SHARED 
     ${OpcUaStackCore_SRC}
 )
 
diff --git a/src/OpcUaStackPubSub/CMakeLists.txt b/src/OpcUaStackPubSub/CMakeLists.txt
index 181f5370..d6d08991 100644
--- a/src/OpcUaStackPubSub/CMakeLists.txt
+++ b/src/OpcUaStackPubSub/CMakeLists.txt
@@ -18,7 +18,6 @@ file(
 
 add_library(
     OpcUaStackPubSub 
-    SHARED 
     ${OpcUaStackPubSub_SRC}
 )
 
diff --git a/src/OpcUaStackServer/CMakeLists.txt b/src/OpcUaStackServer/CMakeLists.txt
index a7eb71fa..7a1efc63 100644
--- a/src/OpcUaStackServer/CMakeLists.txt
+++ b/src/OpcUaStackServer/CMakeLists.txt
@@ -17,7 +17,6 @@ file(
 
 add_library(
     OpcUaStackServer 
-    SHARED 
     ${OpcUaStackServer_SRC}
 )
 

'''


class opcuastackConan(ConanFile):
    name = "opcuastack"
    version = "master"
    commit = version
    license = "Apache 2.0"
    author = "Vladislav Troinich antlad@icloud.com"
    url = "https://github.com/ASNeG/OpcUaStack"
    description = "ASNeG OPC UA Stack is an open source framework for development and distribution of OPC UA client\server applications"
    topics = ("opcua")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "fPIC": True,
        "shared": True,
        "openssl:shared": False,
        "boost:shared": False,
        "boost:fPIC": True,
        "boost:fPIC": True,
        "boost:shared": False,
        "boost:without_locale": True,
        "boost:without_python": True,
        "boost:without_log": True,
        "boost:without_mpi": True,
        "boost:without_graph_parallel": True,
        "boost:without_fiber": True,
        "boost:without_graph": True,
    }
    generators = "cmake"
    build_policy = "missing"
    requires = (
        "openssl/1.1.1l",
        "boost/1.76.0"
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

        install_path = cmake.definitions.get("CMAKE_INSTALL_PREFIX")
        self.run(
            "ls {}/include/OpcUaStack3/OpcUaStackCore/Base/".format(install_path))
        self.copy("*.h", dst="include/",
                  src="{}/include/OpcUaStack3/".format(install_path), keep_path=True)
        self.copy("*.txx", dst="include/",
                  src="{}/include/OpcUaStack3/".format(install_path), keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [
            'OpcUaStackClient', 'OpcUaStackPubSub', 'OpcUaStackCore', "OpcUaStackServer"]
        self.cpp_info.includedirs = ['./include/']
