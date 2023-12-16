from agents import csv_agent, house_buy_agent
from langchain.tools import BaseTool


class CSV_FUNCTION_TOOL(BaseTool):
    name = "CSV FUNCTION TOOL"
    description = """
                Use this tool if you want to get house details from the CSV file
                """
    return_direct = True
    verbose = True

    def _run(self, query):
        response = csv_agent.run(query)
        return response

    def _arun(self):
        raise NotImplementedError("CSV_FUNCTION_TOOL does not support async")


class BUY_PROPERTY_TOOL(BaseTool):
    name = "BUY PROPERTY TOOL"
    description = """
                Use this tool if you want to initiate the process of buying the house
                """
    return_direct = True

    def _run(self, query):
        response = house_buy_agent.run(query)
        return response

    def _arun(self):
        raise NotImplementedError("BUY_PROPERTY_TOOL does not support async")


class SELL_PROPERTY_TOOL(BaseTool):
    name = "SELL PROPERTY TOOL"
    description = """
                Use this tool if you want to initiate the process of selling the house
                """
    return_direct = True

    def _run(self, query):
        return "Sell the property"

    def _arun(self):
        raise NotImplementedError("SELL_PROPERTY_TOOL does not support async")

tools = [
    CSV_FUNCTION_TOOL(),
    BUY_PROPERTY_TOOL(),
    SELL_PROPERTY_TOOL()
]