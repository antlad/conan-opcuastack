
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
#include "OpcUaClient/ClientCommand/CommandMonitorItemStop.h"

using namespace OpcUaStackCore;

namespace OpcUaClient
{

	CommandMonitorItemStop::CommandMonitorItemStop(void)
	: CommandBase(CommandBase::Cmd_MonitorItemStop)
	{
	}

	CommandMonitorItemStop::~CommandMonitorItemStop(void)
	{
	}

	CommandBase::SPtr
	CommandMonitorItemStop::createCommand(void)
	{
		CommandBase::SPtr commandBase = constructSPtr<CommandMonitorItemStop>();
		return commandBase;
	}

	bool
	CommandMonitorItemStop::validateCommand(void)
	{
		return true;
	}

	bool
	CommandMonitorItemStop::addParameter(const std::string& parameterName, const std::string& parameterValue)
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
	CommandMonitorItemStop::help(void)
	{
		std::stringstream ss;
		ss << "  -MonitorItemStop: Starts a subscription\n"
		   << "    -MonitorItemId (1): Identifier of the subscription\n";
		return ss.str();
	}

}
