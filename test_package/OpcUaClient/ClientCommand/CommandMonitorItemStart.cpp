
/*
   Copyright 2016 Kai Huebl (kai@huebl-sgh.de)

   Lizenziert gemäß Apache Licence Version 2.0 (die „Lizenz“); Nutzung dieser
   Datei nur in Übereinstimmung mit der Lizenz erlaubt.
   Eine Kopie der Lizenz erhalten Sie auf http://www.apache.org/licenses/LICENSE-2.0.

   Sofern nicht gemäß geltendem Recht vorgeschrieben oder schriftlich vereinbart,
   erfolgt die Bereitstellung der im Rahmen der Lizenz verbreiteten Software OHNE
   GEWÄHR ODER VORBEHALTE – ganz gleich, ob ausdrücklich oder stillschweigend.

   Informationen über die jeweiligen Bedingungen für Genehmigungen und Einschränkungen
   im Rahmen der Lizenz finden Sie in der Lizenz.

   Autor: Kai Huebl (kai@huebl-sgh.de)
 */

#include <boost/lexical_cast.hpp>
#include <sstream>
#include "OpcUaStackCore/Base/ObjectPool.h"
#include "OpcUaClient/ClientCommand/CommandMonitorItemStart.h"

using namespace OpcUaStackCore;

namespace OpcUaClient
{

	CommandMonitorItemStart::CommandMonitorItemStart(void)
	: CommandBase(CommandBase::Cmd_MonitorItemStart)
	{
	}

	CommandMonitorItemStart::~CommandMonitorItemStart(void)
	{
	}

	CommandBase::SPtr
	CommandMonitorItemStart::createCommand(void)
	{
		CommandBase::SPtr commandBase = constructSPtr<CommandMonitorItemStart>();
		return commandBase;
	}

	bool
	CommandMonitorItemStart::validateCommand(void)
	{
		return true;
	}

	bool
	CommandMonitorItemStart::addParameter(const std::string& parameterName, const std::string& parameterValue)
	{
		if (parameterName == "-MonitorItemId") {
		}
		else {
			std::stringstream ss;
			ss << "invalid parameter " << parameterName;
			errorMessage(ss.str());
			return false;
		}
		return true;
	}

	std::string
	CommandMonitorItemStart::help(void)
	{
		std::stringstream ss;
		ss << "  -MonitorItemStart: Starts a subscription\n"
		   << "    -MonitorItemId (1): Identifier of the subscription\n";
		return ss.str();
	}

}
