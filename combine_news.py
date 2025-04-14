import pandas as pd

def combine_news(static_file='news.csv', live_file='live_news.csv', output_file='combined_news.csv'):
    # Load the original and live news, ignoring problematic rows
    df_static = pd.read_csv(static_file, on_bad_lines='skip', encoding='utf-8')
    df_live = pd.read_csv(live_file, on_bad_lines='skip', encoding='utf-8')

    # Combine and drop duplicates based on title or content
    combined_df = pd.concat([df_static, df_live], ignore_index=True)
    combined_df.drop_duplicates(subset=['title'], inplace=True)

    # Save the combined file
    combined_df.to_csv(output_file, index=False)
    print(f"✅ Combined dataset saved as {output_file}")

if __name__ == "__main__":
    combine_news()
