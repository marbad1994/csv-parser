import csv


def main():
    A = 'file_one.csv'
    B = 'file_two.csv'
    C = 'file_three.csv'
    with open(A) as f:
        d_data = list(csv.reader(f))

    with open(B) as f:
        c_data = list(csv.reader(f))

    with open(C) as f:
        a_data = list(csv.reader(f))
    b_data = c_data + d_data
    new_csv = []

    for a_row in a_data:
        new_row = a_row[:2] + [""] + a_row[2:]
        for b_row in b_data:
            if a_row[1] == b_row[0] and a_row[0] == b_row[2]:
                new_row = a_row[:2] + [b_row[3]] + a_row[2:]
                break
        new_csv.append(new_row)        
    print(new_csv)
    with open('output.csv', 'a') as f:
        wr = csv.writer(f)
        wr.writerows(new_csv)
   

  





if __name__ == "__main__":
    main()
                
                
