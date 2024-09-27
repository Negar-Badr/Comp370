import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Count complaints by borough and date range.")
    parser.add_argument('-i', '--input', required=True, help='Input CSV file')
    parser.add_argument('-s', '--start_date', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('-e', '--end_date', required=True, help='End date (YYYY-MM-DD)')
    parser.add_argument('-o', '--output', help='Output file (CSV)')
    
    args = parser.parse_args()
    
    # Load data
    data = pd.read_csv(args.input)
    
    # Filter by date range
    data['created_date'] = pd.to_datetime(data['created_date'])
    filtered_data = data[(data['created_date'] >= args.start_date) & (data['created_date'] <= args.end_date)]
    
    # Group by complaint type and borough
    result = (filtered_data.groupby(['complaint_type', 'borough'])
                         .size()
                         .reset_index(name='count'))
    
    if args.output:
        result.to_csv(args.output, index=False)
    else:
        print(result.to_csv(index=False))

if __name__ == "__main__":
    main()
