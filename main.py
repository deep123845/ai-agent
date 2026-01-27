import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_functions import *


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("No api key found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt, temperature=0
        ),
    )

    if response.usage_metadata == None:
        raise RuntimeError("Api request failed")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    function_results = []
    print("Response:")
    if response.function_calls and len(response.function_calls) > 0:
        for function_call in response.function_calls:
            result = call_function(function_call, args.verbose)
            if result.parts == None:
                raise Exception("Function returned no result")
            if result.parts[0].function_response == None:
                raise Exception("Function response is invalid")
            function_results.append(result)
    if args.verbose:
        for function_call_result in function_results:
            print(f"-> {function_call_result.parts[0].function_response.response}")
    print(response.text)


if __name__ == "__main__":
    main()
