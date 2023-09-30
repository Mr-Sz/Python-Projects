import openai

openai.api_key = "enter your API key here"

def txt_to_sql(txt):
    prompt = f"Convert the following natural language text into SQL code: {txt}"

    # Generate SQL code using ChatGPT
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,  # Adjust the max tokens based on the response length you want
    )

    # Extract and return SQL code from the API response
    sql_code = response.choices[0].text.strip()
    return sql_code

if __name__ == "__main__":
    input_txt = input("Enter natural language text: ")
    sql_code = txt_to_sql(input_txt)
    print("Generated SQL Code:")
    print(sql_code)