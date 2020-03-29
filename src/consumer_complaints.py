
import sys
import csv

#exceptions
# file input
# error element

#This function takes oniginal CSV input file and build a structure 'product' using dictionary
#in the format {product:{year:{company:occurernce}}}
#It returns dictionary structure 
def structCSV(input_file_name): 
    
    product = {}     # initiate dictionary   {product:{year:{company:occurernce}}}
    
    with open(input_file_name, newline='') as f: #open file as f
        reader = csv.reader(f)
        try:
            newline = next(reader) #exclude header
        except UnicodeDecodeError: 
            print('wrong?')

        for newline in reader: # for (newline <- each row) in CSV file
            # extract relavent data: newdate <-date in year, newproduct <- product name, newcompany <- company name
            newdate = newline[0][:4]
            newproduct = newline[1].lower()
            newcompany = newline[7]
            
            # exceptions
            try: # in case date is not numbers
                int(newdate)
            except ValueError:
                continue
            if newproduct == '': # in case no product name
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

        for product_key in sorted(product.keys()):                                                  # for each sorted product
            for date_key in sorted(product[product_key].keys()):                                        # for each year in one product
                stat =  list(product[product_key][date_key].values())                                       # convert {companies:occurence} to list
                TotNumCpt = sum(stat)                                                                       # calculate total number of complaints
                TotNumCpn = len(stat)                                                                       # calculate total number of companies
                MaxPercent = 100*max(stat)//TotNumCpt                                                       # calculate highest percentage
                if product_key.find(',') != -1:                                                             # write result to file for products with no ',' in their name
                    #print('"'+product_key+'"', date_key, TotNumCpt, TotNumCpn, MaxPercent)
                    writer.writerow(['"'+product_key+'"', date_key, TotNumCpt, TotNumCpn, MaxPercent])      
                else:                                                                                       # write result to file for products with ',' in their name
                    # print(product_key, date_key, TotNumCpt, TotNumCpn, MaxPercent)
                    writer.writerow([product_key, date_key, TotNumCpt, TotNumCpn, MaxPercent])

                
#External input
if __name__ == '__main__':
    input_file_name, output_file_name = sys.argv[1:3]
    #structCSV(input_file_name) returns dictionary 
    #sortCSV(structCSV(input_file_name), output_file_name) writes result in output file
    sortCSV(structCSV(input_file_name), output_file_name)
