from conans import ConanFile, CMake, tools


prefix_patch = '''diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index f74b8d16..c398da6c 100644
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
 
diff --git a/src/OpcUaStackClient/CMakeLists.txt b/src/OpcUaStackClient/CMakeLists.txt
index 651e649d..96aad9b5 100644
--- a/src/OpcUaStackClient/CMakeLists.txt
+++ b/src/OpcUaStackClient/CMakeLists.txt
@@ -16,8 +16,7 @@ file(
 )
 
 add_library(
-    OpcUaStackClient 
-    SHARED 
+    OpcUaStackClient  
     ${OpcUaStackClient_SRC}
 )
 
diff --git a/src/OpcUaStackCore/CMakeLists.txt b/src/OpcUaStackCore/CMakeLists.txt
index 904bc49f..c8086a40 100644
--- a/src/OpcUaStackCore/CMakeLists.txt
+++ b/src/OpcUaStackCore/CMakeLists.txt
@@ -17,8 +17,7 @@ file(
 )
 
 add_library(
-    OpcUaStackCore 
-    SHARED 
+    OpcUaStackCore  
     ${OpcUaStackCore_SRC}
 )
 
diff --git a/src/OpcUaStackPubSub/CMakeLists.txt b/src/OpcUaStackPubSub/CMakeLists.txt
index 181f5370..f9956089 100644
--- a/src/OpcUaStackPubSub/CMakeLists.txt
+++ b/src/OpcUaStackPubSub/CMakeLists.txt
@@ -17,8 +17,7 @@ file(
 )
 
 add_library(
-    OpcUaStackPubSub 
-    SHARED 
+    OpcUaStackPubSub  
     ${OpcUaStackPubSub_SRC}
 )
 
diff --git a/src/OpcUaStackServer/CMakeLists.txt b/src/OpcUaStackServer/CMakeLists.txt
index a7eb71fa..f24623fe 100644
--- a/src/OpcUaStackServer/CMakeLists.txt
+++ b/src/OpcUaStackServer/CMakeLists.txt
@@ -16,8 +16,7 @@ file(
 )
 
 add_library(
-    OpcUaStackServer 
-    SHARED 
+    OpcUaStackServer
     ${OpcUaStackServer_SRC}
 )
 
'''

class opcuastackConan(ConanFile):
    name = "opcuastack"
    version = "3.8.1"
    commit = version
    license = "Apache 2.0"
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
        "openssl/1.1.1d",
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
        self.run("ls {}/include/OpcUaStack3/OpcUaStackCore/Base/".format(install_path))
        self.copy("*.h", dst="include/", src="{}/include/OpcUaStack3/".format(install_path), keep_path=True)
        self.copy("*.txx", dst="include/", src="{}/include/OpcUaStack3/".format(install_path), keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['OpcUaStackClient', 'OpcUaStackPubSub', 'OpcUaStackCore', "OpcUaStackServer"]
        self.cpp_info.includedirs = ['./include/']

