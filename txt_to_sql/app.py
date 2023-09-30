import openai
import tkinter as tk
from tkinter import ttk, messagebox

# Load your OpenAI API key from an environment variable
openai.api_key = "enter your api-key here"

# Function to convert natural language text to SQL
def txt_to_sql():
    try:
        # Get input text from the user
        txt = input_text.get("1.0", tk.END).strip()
        if txt:
            # Prepare prompt for OpenAI API
            prompt = f"Convert the following natural language text into SQL code: {txt}"
            # Call OpenAI API to generate SQL code
            response = openai.Completion.create(
                engine="text-davinci-003",  # set desired model here
                prompt=prompt,
                max_tokens=150,
            )
            # Extract SQL code from API response and display it in the output_text widget
            sql_code = response.choices[0].text.strip()
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, sql_code)
            output_text.config(state=tk.DISABLED)
        else:
            # Display an error message if no input is provided
            messagebox.showerror("Error", "Please Enter Query First!.")
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors and show appropriate error message
        messagebox.showerror("Error", f"OpenAI API Error: {str(e)}")
    except Exception as e:
        # Handle other exceptions and show a generic error message
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to copy SQL code to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    root.update()

# Function to handle the window close event
def on_close():
    root.destroy()

# Create a tkinter window
root = tk.Tk()
root.title("RecallSQL: Text to SQL Syntax Aid")
root.configure(bg='#2E2E2E')

# Configure styles for widgets
style = ttk.Style()
style.configure('TLabel', background='#2E2E2E', font=('Arial', 14, 'bold'), foreground='#FFFFFF')
style.configure('TButton', font=('Arial', 10), foreground='#2E2E2E', background='#4CAF50')
style.configure('TFrame', background='#2E2E2E')

# Create input frame and widgets
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, pady=10, padx=10, sticky=(tk.W, tk.E, tk.N, tk.S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

input_label = ttk.Label(input_frame, text="Enter your query:")
input_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
input_text = tk.Text(input_frame, height=10, width=40, font=('Arial', 12))
input_text.grid(row=1, column=0, pady=10, padx=10, sticky=(tk.W, tk.E))
generate_button = ttk.Button(input_frame, text="Convert", command=txt_to_sql)
generate_button.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)

# Create output frame and widgets
output_frame = ttk.Frame(root)
output_frame.grid(row=0, column=1, pady=10, padx=10, sticky=(tk.W, tk.E, tk.N, tk.S))
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

output_label = ttk.Label(output_frame, text="Generated SQL Query:")
output_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
output_text = tk.Text(output_frame, height=10, width=40, state=tk.DISABLED, font=('Arial', 12))
output_text.grid(row=1, column=0, pady=10, padx=10, sticky=(tk.W, tk.E))

copy_button = ttk.Button(output_frame, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=2, column=0, pady=5, padx=5, sticky=(tk.W, tk.S))

# Set the close event handler for the window
root.protocol("WM_DELETE_WINDOW", on_close)
# Start the tkinter main loop
root.mainloop()