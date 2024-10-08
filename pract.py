# Assuming your DataFrame is named df and has columns 'shipment_id' and 'weight'

# Calculate the total weight for each shipment
df['total_weight'] = df.groupby('shipment_id')['weight'].transform('sum')

# Display the DataFrame with the new column
print(df)
Explanation:

df.groupby('shipment_id')['weight'].transform('sum') groups 
the DataFrame by 'shipment_id' and calculates the sum of 'weight' 
for each group. The transform('sum') method ensures that the result
 is aligned with the original DataFrame, meaning each row in the original 
DataFrame gets the total weight of its corresponding shipment.
The new column 'total_weight' is added to the DataFrame, showing the total weight for each shipment.
 
She was good girl in my life.