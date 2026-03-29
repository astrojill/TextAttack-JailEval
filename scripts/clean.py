"""
Script to clean the raw results.csv that comes out of promptfoo file and keep only the relevant columns for the chosen jailbreak category.
Change th output file to your desired category
"""

import pandas as pd

df = pd.read_csv("results.csv")

keep = [
    "id",
    "technique",
    "quest",
    "[groq:llama-3.3-70b-versatile] {{quest}}",
    "[groq:openai/gpt-oss-120b] {{quest}}",
    "[groq:qwen/qwen3-32b] {{quest}}"
]

df = df[keep].to_csv("resultsCHANGEME.csv", index=False)
