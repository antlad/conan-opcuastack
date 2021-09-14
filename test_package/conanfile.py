from conans import ConanFile, CMake, tools
import os

class opcuastackTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
        }
    default_options = {
        "fPIC": True,
        "shared": False,
        # "opcuastack:shared": False,
        # "opcuastack:fPIC": True,
        }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "OpcUaClient_check -help")
            self.run(bin_path, run_environment=True)
