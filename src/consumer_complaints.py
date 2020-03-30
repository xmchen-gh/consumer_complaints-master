"""
Created on Sun Mar 29 2020

@author: xiaoqianchen
Insight data coding challenge
"""


import sys
import csv


#This function takes oniginal CSV input file and build a structure 'product' using dictionary
#in the format {product:{year:{company:occurernce}}}
#It returns dictionary structure 
def structCSV(input_file_name): 
    
    product = {}     # initiate dictionary   {product:{year:{company:occurernce}}}
    
    lineNum = 0 # tracks row # in csv file
    with open(input_file_name, newline='', encoding= 'unicode_escape') as f: #open file as f
        reader = csv.reader(f)
        newline = next(reader) #exclude header
        lineNum += 1

        
        for newline in reader: # for (newline <- each row) in CSV file
            lineNum += 1
            # extract relavent data: newdate <-date in year, newproduct <- product name, newcompany <- company name
            
            try:
                newdate = newline[0][:4]
                newproduct = newline[1].lower()
                newcompany = newline[7]
            except Exception as e:
                print('row = '+ str(lineNum) + ' Error: ', e)
                continue
            
            # exceptions
            try: # in case date is not numbers
                int(newdate)
            except ValueError as e:
                print('row = ' + str(lineNum) + ' Error: ', e)
                continue
            if newproduct == '' or int(newdate)<2010 or int(newdate)>2020: # in case no product name and nonexistant year (CFPB formed in 2010)
                print('row = ' + str(lineNum) + ' Error: no product name or non-existant year')                
                continue

            # place extracted info in dictionary
            if newproduct in product:                                   # if newproduct already exists in dictionary = product
                if newdate in product[newproduct]:                          # if newdate already exists for newproduct
                    if newcompany in product[newproduct][newdate]:              # if newcompany already exist under newdate
                        product[newproduct][newdate][newcompany] += 1               # occurence of complaints +=1
                    else:                                                       # else if newcompany is not under newdate
                        product[newproduct][newdate][newcompany] = 1                # insert new company name {new company:occurence} = {newcompany:1}
                else:                                                       # else if newdate do not exists for new product
                    product[newproduct][newdate] = {newcompany:1}               # insert new date  {new date:{new company: occurence}} = {newdate:{newcompany:1}}
            else:                                                       # else if newproduct is not in dictionary
                product[newproduct] =  {newdate:{newcompany:1}}             # insert new product {new product:{new date:{new company: occurence}}} = {newproduct:{newdate:{newcompany:1}}}
    
    return product



#This function calculate total number of complaints 'TotNumCpt', total number of companies 'TotNumcpn', highest percentage 'MaxPerccent'
#as it sort product name and year
#in the inner loop, it writes output line by line in file 'output_file_name'
def sortCSV(product, output_file_name):
    with open(output_file_name, 'w', newline='') as file: # open file
        writer = csv.writer(file)

        for product_key in sorted(product.keys()):                                  # for each sorted product
            for date_key in sorted(product[product_key].keys()):                        # for each year in one product
                stat =  list(product[product_key][date_key].values())                       # convert {companies:occurence} to list
                TotNumCpt = sum(stat)                                                       # calculate total number of complaints
                TotNumCpn = len(stat)                                                       # calculate total number of companies
                MaxPercent = round(100*max(stat)/TotNumCpt)                                 # calculate highest percentage
                writer.writerow([product_key, date_key, TotNumCpt, TotNumCpn, MaxPercent])  # write result in file



                
#External input
if __name__ == '__main__':
    input_file_name, output_file_name = sys.argv[1:3]
    #structCSV(input_file_name) returns dictionary 
    #sortCSV(structCSV(input_file_name), output_file_name) writes result in output file
    sortCSV(structCSV(input_file_name), output_file_name)
