from mech_client.marketplace_interact import marketplace_interact
import asyncio

async def askMech(
    prompt_text: str,
    priority_mech: str = "0xbead38e4C4777341bB3FD44e8cd4D1ba1a7Ad9D7",
    tool_name: str = "deepseek-prediction-online",
    chain_config: str = "gnosis",
    use_offchain: bool = False,
    private_key_path: str = "ethereum_private_key.txt"
) -> str:
    """
    Ask a question to the Mech marketplace and get a prediction.
    
    Args:
        prompt_text (str): The question to ask
        priority_mech (str): The priority mech address (default: "0xbead38e4C4777341bB3FD44e8cd4D1ba1a7Ad9D7")
        tool_name (str): The tool to use (default: "deepseek-prediction-online")
        chain_config (str): The chain configuration (default: "gnosis")
        use_offchain (bool): Whether to use offchain confirmation (default: False)
        private_key_path (str): Path to the private key file (default: "ethereum_private_key.txt")
    
    Returns:
        str: The result of the interaction
    """
    try:
        # Get the current event loop
        loop = asyncio.get_running_loop()
        
        # Run the marketplace interaction in the current loop
        result = await marketplace_interact(
            prompt=prompt_text,
            priority_mech=priority_mech,
            use_offchain=use_offchain,
            tool=tool_name,
            chain_config=chain_config,
            private_key_path=private_key_path,
        )
        return result
    except Exception as e:
        return f"Error getting prediction: {str(e)}"