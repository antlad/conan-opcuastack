from conans import ConanFile, CMake, tools


prefix_patch = '''diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index f74b8d16..ad1a3bc9 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -21,6 +21,8 @@ set(OPENSSL_VERSION_MAJOR "1" CACHE STRING "major version")
 set(OPENSSL_VERSION_MINOR "0" CACHE STRING "minor version")
 set(OPENSSL_VERSION_PATCH "0" CACHE STRING "patch version")
 
+include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
+conan_basic_setup()
 
 # -----------------------------------------------------------------------------
 # -----------------------------------------------------------------------------
@@ -168,9 +170,9 @@ message(STATUS "  libraries: ${Boost_LIBRARIES}")
 # -----------------------------------------------------------------------------
 # -----------------------------------------------------------------------------
 find_package(
-    OpenSSL 
-    "${OPENSSL_VERSION_MAJOR}.${OPENSSL_VERSION_MINOR}.${OPENSSL_VERSION_PATCH}" 
-    REQUIRED
+   OpenSSL 
+   "${OPENSSL_VERSION_MAJOR}.${OPENSSL_VERSION_MINOR}.${OPENSSL_VERSION_PATCH}" 
+   REQUIRED
 )
 
 message(STATUS "OpenSSL library")
@@ -198,7 +200,7 @@ find_package (Threads)
 #
 # -----------------------------------------------------------------------------
 # -----------------------------------------------------------------------------
-set (INSTALL_PREFIX "/usr")        
+set (INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})        
 if (WIN32)
     if (MSVC)
         set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")
diff --git a/src/OpcUaClient/ClientCommand/CommandBase.h b/src/OpcUaClient/ClientCommand/CommandBase.h
index c4b12b2d..ae06ee90 100644
--- a/src/OpcUaClient/ClientCommand/CommandBase.h
+++ b/src/OpcUaClient/ClientCommand/CommandBase.h
@@ -20,6 +20,7 @@
 
 #include <boost/shared_ptr.hpp>
 #include <stdint.h>
+#include <string>
 #include <vector>
 #include <map>
 #include "OpcUaClient/ClientCommand/ParameterFlags.h"
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
 
diff --git a/src/OpcUaStackCore/BuildInTypes/OpcUaExtensionObject.cpp b/src/OpcUaStackCore/BuildInTypes/OpcUaExtensionObject.cpp
index 6eb4477f..f7f16fab 100644
--- a/src/OpcUaStackCore/BuildInTypes/OpcUaExtensionObject.cpp
+++ b/src/OpcUaStackCore/BuildInTypes/OpcUaExtensionObject.cpp
@@ -347,7 +347,7 @@ namespace OpcUaStackCore
 
 		OpcUaNodeId xmlNodeIdType;
 		std::string s = *identifier;
-		s.erase(s.begin(), std::find_if(s.begin(), s.end(), std::not1(std::ptr_fun<int, int>(std::isspace))));
+		s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](int c) {return !std::isspace(c);}));
 		bool rc = xmlNodeIdType.fromString(s);
 		if (!rc) {
 			Log(Error, "value format error")
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
 
diff --git a/src/OpcUaStackCore/StandardDataTypes/Argument.cpp b/src/OpcUaStackCore/StandardDataTypes/Argument.cpp
index 23b5f206..bc6f59f9 100644
--- a/src/OpcUaStackCore/StandardDataTypes/Argument.cpp
+++ b/src/OpcUaStackCore/StandardDataTypes/Argument.cpp
@@ -199,7 +199,7 @@ namespace OpcUaStackCore
 		}
 
 		std::string s = *identifier;
-		s.erase(s.begin(), std::find_if(s.begin(), s.end(), std::not1(std::ptr_fun<int, int>(std::isspace))));
+		s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](int c) {return !std::isspace(c);}));
 		bool rc = dataType_.fromString(s);
 		if (!rc) {
 			Log(Error, "value format error")
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
 
diff --git a/src/OpcUaStackServer/NodeSet/NodeSetValueParser.cpp b/src/OpcUaStackServer/NodeSet/NodeSetValueParser.cpp
index c30c9103..649a4853 100644
--- a/src/OpcUaStackServer/NodeSet/NodeSetValueParser.cpp
+++ b/src/OpcUaStackServer/NodeSet/NodeSetValueParser.cpp
@@ -327,9 +327,9 @@ namespace OpcUaStackServer
 				.parameter("Tag", addxmls("Identifier"));
 			return false;
 		}
-
+		
 		std::string s = *sourceValue;
-		s.erase(s.begin(), std::find_if(s.begin(), s.end(), std::not1(std::ptr_fun<int, int>(std::isspace))));
+		s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](int c) {return !std::isspace(c);}));
 		bool rc = destValue->fromString(s);
 		if (!rc) {
 			Log(Error, "value format error")

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

