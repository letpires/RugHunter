from mech_client.marketplace_interact import marketplace_interact
import nest_asyncio
from mech_client.interact import interact
from mech_client.interact import ConfirmationType
import asyncio

# Apply nest_asyncio at the module level
nest_asyncio.apply()

PREDICTION_PROMPT = """\
You are an advanced AI system specialized in analyzing cryptocurrency token transactions to determine their legitimacy and detect pump and dump schemes.

Question: {question}  

Instructions:
1. Analyze the transaction patterns and identify key indicators of pump and dump activity. Focus on:
   - Rapid buy/sell patterns (wallets buying and selling within short timeframes)
   - Coordinated trading (multiple wallets trading in similar patterns)
   - Volume manipulation (sudden spikes followed by drops)
   - Wallet clustering (groups of wallets with similar behavior)
   - Transaction timing patterns (suspiciously regular intervals)
   Place this analysis in <pattern_analysis> tags.

2. List potential indicators of human/organic trading based on database metrics. Rate each indicator's strength on a scale of 1-10. Look for:
   - Natural holding periods (not immediate sells)
   - Varied transaction sizes
   - Irregular trading intervals
   - Diverse wallet behaviors
   - Reasonable profit-taking patterns
   Use <human_indicators> tags.

3. List potential indicators of pump and dump activity based on database metrics. Rate each indicator's strength on a scale of 1-10. Look for:
   - Quick buy/sell cycles
   - Coordinated price movements
   - Artificial volume spikes
   - Wallet clustering
   - Suspicious timing patterns
   Use <pump_indicators> tags.

4. Provide a detailed analysis of how these factors interact and their implications for token legitimacy. Consider:
   - Pump and dump scheme characteristics
   - Natural vs artificial trading patterns
   - Wallet behavior analysis
   - Volume and price correlation
   - Transaction timing analysis
   Use <analysis> tags.

5. Output an initial probability of the token being legitimate (human-driven) as a number between 0 and 1, taking into account database metrics. Use <initial_prediction> tags.

6. Perform a critical review of your analysis:
   - Check for confirmation bias
   - Consider alternative explanations
   - Evaluate the reliability of the patterns
   - Assess the completeness of the analysis
   - Verify database metrics consistency
   Use <reflection> tags.

7. Output your final prediction (a number between 0 and 1 with an asterisk at the beginning and end of the decimal) in <final_prediction> tags.

8. Provide a detailed explanation of why the token is flagged as legitimate or not legitimate. Include:
   - Specific evidence from transaction patterns
   - Analysis of wallet behaviors
   - Identification of pump and dump indicators
   - Confidence level in each piece of evidence
   - Potential alternative explanations
   Use <explanation> tags.

OUTPUT FORMAT
--------------
* Your output response must be only a single JSON object parsable by `json.loads()`.
* The JSON must have five fields: `"p_legitimate"`, `"p_bot"`, `"confidence"`, `"info_utility"`, and `"explanation"`.
* Each probability value must be between 0 and 1, and `"p_legitimate" + "p_bot" == 1`.
* The `"explanation"` field should contain a detailed explanation of why the token is flagged as legitimate or not legitimate, including specific evidence and confidence levels.
"""

async def askMech(
    prompt_text: str,
    priority_mech: str = "0x77af31de935740567cf4ff1986d04b2c964a786a",
    tool_name: str = "openai-gpt-4",
    chain_config: str = "gnosis",
    use_offchain: bool = False,
    private_key_path: str = "ethereum_private_key.txt"
) -> str:
    """
    Ask a question to the Mech marketplace and get a prediction.
    
    Args:
        prompt_text (str): The question to ask
        priority_mech (str): The priority mech address (default: "0x77af31de935740567cf4ff1986d04b2c964a786a")
        tool_name (str): The tool to use (default: "deepseek-prediction-online")
        chain_config (str): The chain configuration (default: "gnosis")
        use_offchain (bool): Whether to use offchain confirmation (default: False)
        private_key_path (str): Path to the private key file (default: "ethereum_private_key.txt")
    
    Returns:
        str: The result of the interaction
    """
    try:

        prompt = PREDICTION_PROMPT.format(
            question=prompt_text
        )
        print("prompt",prompt)


        # Run the interaction in a separate thread to avoid blocking the event loop
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: interact(
                prompt=prompt,
                agent_id=6,
                tool=tool_name,
                chain_config=chain_config,
                private_key_path=private_key_path
            )
        )
        print(result)
        return result
    except Exception as e:
        return f"Error getting prediction: {str(e)}"
