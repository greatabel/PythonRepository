def main():
    print('-'*20,'\n'*5)
    patient_id =  55
    for i in range(1,12):
        for j in range(1,30):
            print("insert into measures(`data`,`created_date`,`patient_id`,`right_eye`) values({0},'2016-{1}-{2} 00:00:00',{3},{4});"\
                .format( i+j+100 , str(i % 12).zfill(2), str(j % 30).zfill(2), patient_id, j % 2  ))
    print('/** test ** /')
    for i in range(1,4):
        for j in range(1,20):
            print("insert into measures(`data`,`created_date`,`patient_id`,`right_eye`) values({0},'2017-{1}-{2} 00:00:00',{3},{4});"\
                .format( i+j+100 , str(i % 12).zfill(2), str(j % 30).zfill(2), patient_id, j % 2  ))
if __name__ == "__main__":
    main()
# "insert into measures(`data`,`created_date`,`patient_id`,`right_eye`) values(100,'2017-03-20 00:00:00',3,1);"