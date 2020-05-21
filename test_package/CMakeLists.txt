cmake_minimum_required(VERSION 3.0)
project	(ASNeGDemo CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


include_directories(
    "${CMAKE_CURRENT_LIST_DIR}"
)

set(
    OpcUaClient_SRC
    ./OpcUaClient/Client/Client.cpp
    ./OpcUaClient/ClientService/ClientServiceNodeSetServer.cpp
    ./OpcUaClient/ClientService/ClientServiceNodeSetFilter.cpp
    ./OpcUaClient/ClientService/ClientServiceRead.cpp
    ./OpcUaClient/ClientService/ClientServiceReadH.cpp
    ./OpcUaClient/ClientService/ClientServiceGetEndpoint.cpp
    ./OpcUaClient/ClientService/ClientServiceManager.cpp
    ./OpcUaClient/ClientService/ClientServiceDisconnect.cpp
    ./OpcUaClient/ClientService/ClientAccessObject.cpp
    ./OpcUaClient/ClientService/ClientServiceWrite.cpp
    ./OpcUaClient/ClientService/ClientServiceWriteH.cpp
    ./OpcUaClient/ClientService/ClientServiceBrowsePathToNodeId.cpp
    ./OpcUaClient/ClientService/ClientServiceFunction.cpp
    ./OpcUaClient/ClientService/ClientServiceFindServer.cpp
    ./OpcUaClient/ClientService/ClientServiceConnect.cpp
    ./OpcUaClient/ClientService/ClientServiceExecute.cpp
    ./OpcUaClient/ClientService/ClientServiceDelay.cpp
    ./OpcUaClient/ClientService/ClientServiceRegisterServer.cpp
    ./OpcUaClient/ClientService/ClientServiceBase.cpp
    ./OpcUaClient/ClientService/ClientServiceBrowse.cpp
    ./OpcUaClient/ClientCommand/CommandGetEndpoint.cpp
    ./OpcUaClient/ClientCommand/CommandSubscriptionStop.cpp
    ./OpcUaClient/ClientCommand/ParameterFlags.cpp
    ./OpcUaClient/ClientCommand/CommandDelay.cpp
    ./OpcUaClient/ClientCommand/CommandDisconnect.cpp
    ./OpcUaClient/ClientCommand/CommandNodeSetFilter.cpp
    ./OpcUaClient/ClientCommand/CommandBrowse.cpp
    ./OpcUaClient/ClientCommand/CommandReadH.cpp
    ./OpcUaClient/ClientCommand/CommandParser.cpp
    ./OpcUaClient/ClientCommand/CommandMonitorItemStop.cpp
    ./OpcUaClient/ClientCommand/CommandRead.cpp
    ./OpcUaClient/ClientCommand/CommandFindServer.cpp
    ./OpcUaClient/ClientCommand/CommandWrite.cpp
    ./OpcUaClient/ClientCommand/CommandNodeSetServer.cpp
    ./OpcUaClient/ClientCommand/CommandFunction.cpp
    ./OpcUaClient/ClientCommand/CommandBase.cpp
    ./OpcUaClient/ClientCommand/CommandWriteH.cpp
    ./OpcUaClient/ClientCommand/CommandSubscriptionStart.cpp
    ./OpcUaClient/ClientCommand/CommandMonitorItemStart.cpp
    ./OpcUaClient/ClientCommand/CommandRegisterServer.cpp
    ./OpcUaClient/ClientCommand/CommandBrowsePathToNodeId.cpp
    ./OpcUaClient/ClientCommand/CommandConnect.cpp
    ./OpcUaClient/Client/ClientApplication.cpp
)

add_executable(
    OpcUaClient_check
    ${OpcUaClient_SRC}
)

target_link_libraries(OpcUaClient_check ${CONAN_LIBS})
set_target_properties(OpcUaClient_check PROPERTIES LINKER_LANGUAGE CXX)


